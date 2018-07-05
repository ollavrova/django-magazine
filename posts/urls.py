from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/approved/$', api.ApprovedPostList.as_view()),
    url(r'^posts/$', api.PostList.as_view()),
    url(r'^writerposts/(?P<pk>[0-9]+)/$', api.WritersPostList.as_view()),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', api.user_detail),
    url(r'^userprofile/$', api.user_create),
]

urlpatterns = format_suffix_patterns(urlpatterns)
