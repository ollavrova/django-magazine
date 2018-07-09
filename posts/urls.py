from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/approved/$', api.ApprovedPostList.as_view(), name='approved_list'),
    url(r'^posts/$', api.PostList.as_view(), name='posts'),
    url(r'^writerposts/(?P<pk>[0-9]+)/$', api.WritersPostList.as_view(), name='writersposts_by_pk'),
    url(r'^userprofile/(?P<token>[a-zA-Z0-9]+)/$', api.user_detail, name='user_detail'),
    url(r'^userprofile/$', api.user_create, name='user_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
