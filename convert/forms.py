from django import forms
from django.forms import fields
from . models import Convert

class ConvertForm(forms.ModelForm):
    class Meta:
        model = Convert
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ConvertForm,self).__init__(*args,**kwargs)
