from django.forms import ModelForm, fields
from .models import Queries
from django import forms
import sqlite3

class QueryForm(ModelForm):
    class Meta:
        model = Queries
        fields = {'Name', 'EmailID', 'Description'}

        widgets ={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'EmailID': forms.TextInput(attrs={'class':'form-control','type':'email'}),
        }