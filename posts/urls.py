from django.conf.urls import url
from posts import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^<int:post_id>/', views.detail, name='detail'),
]
