from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

import posts

admin.autodiscover()


schema_view = get_swagger_view(title='Django Magazine API')

urlpatterns = [

    url(r'^doc/$', schema_view),
    url(r'^api/', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/login', posts.api.Login.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
]
