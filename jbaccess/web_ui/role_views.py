from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from jba_core.service import PersonService, RoleService
from web_ui.commons import BaseView
from web_ui.forms import RoleForm, AttachRoleForm


class RolesController(BaseView):
    def get(self, request):
        form = RoleForm()
        roles = RoleService.get_all()
        return render(request, 'page/roles.html', {'roles': roles, 'form': form})


class RoleController(BaseView):
    def delete(self, request, role_id):
        RoleService.delete(role_id)
        return HttpResponse('success')


class AddRoleController(FormView):
    form_class = RoleForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        RoleService.create(name)
        return redirect('roles')


class AttachRoleToPerson(FormView):
    form_class = AttachRoleForm

    def form_valid(self, form):
        person_id = form.cleaned_data['person_id']
        role_id = form.cleaned_data['role']
        PersonService.attach_role(person_id, role_id)
        return redirect('person', person_id)