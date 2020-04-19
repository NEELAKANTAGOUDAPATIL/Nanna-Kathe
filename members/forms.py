from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        fields = ("name", "phone", "email", "address", "principal_amt", "start_date", "interest")
        model = Member

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["interest"].label = "Interest Rate (% per month)"
        # if user is not None:
        #     self.fields["group"].queryset = (
        #         models.Group.objects.filter(
        #             pk__in=user.groups.values_list("group__pk")
        #         )
        #     )

class FinalizeForm(forms.ModelForm):

    class Meta():
        model =Member
        fields = ("interest_amt", "total_amt", "end_date")
