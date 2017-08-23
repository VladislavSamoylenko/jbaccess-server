from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views, key_views, role_views

urlpatterns = [
    url(r'^$', views.IndexController.as_view(), name="index"),
    url(r'^personnel/$', views.PersonsController.as_view(), name="personnel"),
    url(r'^person/(?P<person_id>\d+)$', views.PersonController.as_view(), name="person"),
    url(r'^keys/?', include('web_ui.key_urls')),
    url(r'^roles/?', include('web_ui.role_urls')),
    url(r'^places/$', views.PlacesController.as_view(), name="places"),
    url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
]
