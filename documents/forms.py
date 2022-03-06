from django import forms
from django.forms import ModelForm
from django.forms.widgets import  NumberInput
from .models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'senate_year': NumberInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'show': field.widget.attrs.update({'class': "input"})
            else: field.widget.attrs.update({'class': "checkbox"})
        

