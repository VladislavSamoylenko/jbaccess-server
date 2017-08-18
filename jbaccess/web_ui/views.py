from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView

from jba_core.service import KeyService
from jba_core.service import PersonService
from .commons import BaseView
from .forms import PersonForm, KeyForm


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
        form = KeyForm()
        form.fields.get('person_id').initial = person_id
        return render(request, 'page/person.html', {'person': person, 'keys': keys, 'form': form})

    def delete(self, request, person_id):
        PersonService.delete(person_id)
        return HttpResponse('success')


class KeyController(FormView):
    form_class = KeyForm

    def form_valid(self, form):
        person_id = form.cleaned_data['person_id']
        name = form.cleaned_data['name']
        access_key = form.cleaned_data['access_key']
        KeyService.create(name, access_key, person_id)
        return redirect('person', person_id)

