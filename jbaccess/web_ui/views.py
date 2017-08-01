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
