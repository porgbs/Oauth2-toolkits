from django.conf.urls import url
from django.urls import path
from . import views
# from .api import Userlist

urlpatterns = [
    # url(r'^api/userlist/$', Userlist.as_view(), name='user'),
    # url(r'^api/userlist/(?P<id>\d+)/$', Userlist.as_view(), name='user'),
    path('api/app/', views.AppCreate.as_view())
    # url(r'^api/image/(?P<id>\d+)/$', create_auth.as_view(), name='SignUp'),
]