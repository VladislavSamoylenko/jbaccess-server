from django import forms
from jba_core.service import RoleService


class PersonForm(forms.Form):
    name = forms.CharField(label='Full Name', required=True, max_length=50, min_length=3)


class KeyForm(forms.Form):
    name = forms.CharField(label='Key Name', required=True, max_length=30, min_length=3)
    access_key = forms.CharField(label='Access key', required=True, min_length=1)
    person_id = forms.IntegerField(label='person_id', required=True, widget=forms.HiddenInput())


class RoleForm(forms.Form):
    name = forms.CharField(label='Role Name', required=True, max_length=50, min_length=3)


class AttachRoleForm(forms.Form):
    choices = []
    roles = RoleService.get_all()
    for role in roles:
        choices.append((role.id, role.name))
    role = forms.ChoiceField(label="Role", required=True, choices=choices, widget=forms.Select())
    # TODO change to checkboxes select
    person_id = forms.IntegerField(required=True, widget=forms.HiddenInput())
