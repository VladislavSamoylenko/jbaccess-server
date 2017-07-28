from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='Full Name', required=True, max_length=50, min_length=3)
