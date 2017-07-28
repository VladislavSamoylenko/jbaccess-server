from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexController.as_view(), name="index"),
    url(r'^personnel/$', views.PersonsController.as_view(), name="personnel"),
    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
]
