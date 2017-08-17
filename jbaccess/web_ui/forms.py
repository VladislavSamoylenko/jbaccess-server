from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='Full Name', required=True, max_length=50, min_length=3)


class KeyForm(forms.Form):
    name = forms.CharField(label='Key Name', required=True, max_length=30, min_length=3)
    access_key = forms.CharField(label='Access key', required=True, min_length=1)
    person_id = forms.IntegerField(label='person_id', required=True, widget=forms.HiddenInput())
