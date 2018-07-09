from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from posts.api import CustomAuthToken

admin.autodiscover()


schema_view = get_swagger_view(title='Django Magazine API')

urlpatterns = [

    url(r'^doc/$', schema_view),
    url(r'^api/', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', CustomAuthToken.as_view(), name='get_token')
]
