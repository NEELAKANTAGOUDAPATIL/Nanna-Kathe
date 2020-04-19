from django.conf.urls import url

from . import views

app_name='members'

urlpatterns = [
    url(r"^$", views.MemberList.as_view(), name="all"),
    url(r"^member/new/$", views.CreateMember.as_view(), name="create"),
    # url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"^(?P<username>[-\w]+)/member/(?P<pk>\d+)/$",views.MemberDetail.as_view(),name="single"),
    url(r'^member/(?P<pk>\d+)/finalize/$',views.member_finalize,name='member_finalize'),
    url(r"^(?P<username>[-\w]+)/member/(?P<pk>\d+)/confirm/$",views.finalize,name="finalize"),
    url(r"^delete/(?P<pk>\d+)/$",views.DeleteMember.as_view(),name="delete"),

]
