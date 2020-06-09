from django.conf.urls import url
from django.urls import path
from . import views

# from .api import Userlist

urlpatterns = [
    # url(r'^api/userlist/$', Userlist.as_view(), name='user'),
    # url(r'^api/userlist/(?P<id>\d+)/$', Userlist.as_view(), name='user'),
    path('api/app/', views.AppCreate.as_view()),
    path('api/refreshtoken/', views.RefreshTokenCreate.as_view()),
    path('api/accesstoken/', views.AccessTokenCreate.as_view()),
    url(r'^api/accesstoken/update/(?P<id>\d+)/$', views.AccessTokenUpdate.as_view()),
    # url(r'^api/image/(?P<id>\d+)/$', create_auth.as_view(), name='SignUp'),
]
