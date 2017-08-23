from django.conf.urls import url
from web_ui import key_views

urlpatterns = [
    url(r'^add$', key_views.AddKeyController.as_view(), name="add_key"),
    url(r'^(?P<key_id>\d+)$', key_views.KeyController.as_view(), name="keys"),
]