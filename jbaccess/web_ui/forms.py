from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='Full Name', required=True, max_length=50, min_length=3)


class KeyForm(forms.Form):
    name = forms.CharField(label='Key', required=True, max_length=30, min_length=3)
    person_id = forms.IntegerField(label='person_id', required=True, widget=forms.HiddenInput())
