from django.shortcuts import render
from django.views import View


class IndexController(View):
    def get(self, request):
        return render(request, 'page/index.html')


class PersonsController(View):
    def get(self, request):
        return render(request, 'page/personnel.html')
