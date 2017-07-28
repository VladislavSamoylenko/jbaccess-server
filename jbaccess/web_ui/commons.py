from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
