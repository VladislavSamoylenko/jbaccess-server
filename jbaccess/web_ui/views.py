from django.shortcuts import render
from django.views import View

from jba_core.service import PersonService


class IndexController(View):
    def get(self, request):
        return render(request, 'page/index.html')


class PersonsController(View):
    def get(self, request):
        personnel = PersonService.get_all()
        return render(request, 'page/personnel.html', {'persons': personnel})
