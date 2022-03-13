from django.db import models
from django import forms
from contatos.models import Contato


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()