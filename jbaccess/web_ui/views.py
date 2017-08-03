from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from jba_core.service import PersonService
from .commons import BaseView
from .forms import PersonForm


class IndexController(BaseView):
    def get(self, request):
        return render(request, 'page/index.html')


class PersonsController(BaseView):
    def get(self, request):
        form = PersonForm()
        personnel = PersonService.get_all()

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
        return render(request, 'page/person.html', {'person': person})

    def delete(self, request, person_id):
        PersonService.delete(person_id)
        return HttpResponse('success')
