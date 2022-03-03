from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from .models import  Event


class EventForm(ModelForm):
    REQ = (("0","None" ),("1","Weekly"), ( "2","Monthly"),( "3","Yearly"),)
    summ = (('Activiteit','Activiteit'),('Clubactiviteit','Clubactiviteit'),('Wedstrijd','Wedstrijd'),('Dispuutsactiviteit','Dispuutsactiviteit'),('Dispuutsverjaardag','Dispuutsverjaardag')    ,)
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'start_date':NumberInput(attrs={'type': 'date'}),
            'start_time':NumberInput(attrs={'type': 'time'}),
            'end_date':NumberInput(attrs={'type': 'date'}),
            'end_time':NumberInput(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "input"})
    recuring = forms.ChoiceField(choices = REQ)
    summary = forms.ChoiceField(choices = summ)