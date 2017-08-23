from django.conf.urls import url
from web_ui import role_views

urlpatterns = [
    url(r'^$', role_views.RolesController.as_view(), name="roles"),
    url(r'^attach$', role_views.AttachRoleToPerson.as_view(), name="attach_role"),
    url(r'^(?P<role_id>\d+)$', role_views.RoleController.as_view(), name="role"),
    url(r'^add$', role_views.AddRoleController.as_view(), name="add_role"),
]
