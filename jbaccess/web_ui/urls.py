from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexController.as_view(), name="index"),
    url(r'^ui/personnel/$', views.PersonsController.as_view(), name="personnel"),
]
