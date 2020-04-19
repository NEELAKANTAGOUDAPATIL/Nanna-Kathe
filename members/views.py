from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.db.models import Q

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from datetime import datetime

from . import forms
from .models import Member

from django.contrib.auth import get_user_model
User = get_user_model()


class MemberList(generic.ListView):
    model = Member
    select_related = ("user")

    def get_queryset(self):
        return Member.objects.order_by('name')

class MemberDetail(generic.DetailView):
    model = Member

# class UserMemberList(generic.ListView):
#     model = Member
#     template_name = "posts/user_post_list.html"
#
#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related("posts").get(
#                 username__iexact=self.kwargs.get("username")
#             )
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.posts.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_user"] = self.post_user
#         return context


# class PostDetail(SelectRelatedMixin, generic.DetailView):
#     model = models.Post
#     select_related = ("user", "group")
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(
#             user__username__iexact=self.kwargs.get("username")
#         )


class CreateMember(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ("name", "phone", "email", "address", "principal_amt", "start_date", "interest")
    model = Member
    success_url = reverse_lazy("members:all")

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteMember(LoginRequiredMixin, generic.DeleteView):
    model = Member
    success_url = reverse_lazy("members:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Member Deleted")
        return super().delete(*args, **kwargs)

# class MemberFinalize(LoginRequiredMixin, SelectRelatedMixin, generic.UpdateView):
#     model = Member
#     select_related = ("user")
#     success_url = reverse_lazy("members:single")
#
#     def get_queryset(self):
#         obj = get_object_or_404(Member,pk = self.kwargs['pk'])
#         # for obj in objs:
#         data = {"principal_amt":obj.principal_amt,
#                 "interest":obj.interest,
#                 "start_date":obj.start_date}
#         end_date = timezone.now().date()
#         d1 = data["start_date"]
#         d2 = end_date
#         t = abs((d2-d1).days)
#         p = data["principal_amt"]
#         r = data["interest"]
#         s = p*r*t/(100)
#         total_amt = p + s
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.interest_amt = s
#         self.object.total_amt = total_amt
#         self.object.end_date = data["end_date"]
#         self.object.save()
#         return super().form_valid(form)

def calculate(member):
    startDate = member.start_date
    p = member.principal_amt
    r = member.interest
    endDate = timezone.now().date()

    t = abs((endDate-startDate).days)
    s=p*t*r/(100*30)
    total_amt = s+p

    member.interest_amt = s
    member.total_amt = total_amt
    member.end_date = endDate

@login_required
def member_finalize(request,pk):
    member = get_object_or_404(Member,pk=pk)
    calculate(member)
    return render(request, "members/finalize_form.html", {'pk': member.pk, 'member':member})

@login_required
def finalize(request, username, pk):
    member = get_object_or_404(Member,pk=pk)
    calculate(member)
    member.save()
    return redirect("members:single", username=member.user, pk=pk)
