from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView

from jba_core.service import KeyService
from web_ui.commons import BaseView
from web_ui.forms import KeyForm


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
