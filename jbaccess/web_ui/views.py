from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView

from jba_core.service import KeyService, PersonService, RoleService
from .commons import BaseView
from .forms import PersonForm, KeyForm, RoleForm, AttachRoleForm

# TODO refactor: separate to different files


class IndexController(BaseView):
    def get(self, request):
        return render(request, 'page/index.html')


class PersonsController(BaseView):
    def get(self, request):
        form = PersonForm()
        personnel = PersonService.get_all()

        for person in personnel:
            person.keys = len(PersonService.get_keys(person.id))

        return render(request, 'page/personnel.html', {
            'persons': personnel,
            'form': form
        })

    def post(self, request):
        form = PersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            PersonService.create(name)

        return redirect(reverse('personnel'))


class PlacesController(BaseView):
    def get(self, request):
        return render(request, 'page/places.html')


class PersonController(BaseView):
    def get(self, request, person_id):
        person = PersonService.get(person_id)
        keys = PersonService.get_keys(person_id)

        key_form = KeyForm()
        key_form.fields.get('person_id').initial = person_id

        roles = PersonService.get_roles(person_id)
        role_form = AttachRoleForm()
        role_form.fields.get('person_id').initial = person_id
        if len(roles):
            role_form.fields.get('role').initial = PersonService.get_roles(person_id)[0]
        else:
            role_form.fields.get('role').initial = 7  # 7 is "empty", no roles attached

        return render(request, 'page/person.html',
                      {'person': person,
                       'keys': keys,
                       'form': key_form,
                       'role_form': role_form
                       })

    def delete(self, request, person_id):
        PersonService.delete(person_id)
        return HttpResponse('success')


class AddKeyController(FormView):
    form_class = KeyForm

    def form_valid(self, form):
        person_id = form.cleaned_data['person_id']
        name = form.cleaned_data['name']
        access_key = form.cleaned_data['access_key']
        KeyService.create(name, access_key, person_id)
        return redirect('person', person_id)


class KeyController(BaseView):
    def delete(self, request, key_id):
        KeyService.delete(key_id)
        return HttpResponse('success')


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
