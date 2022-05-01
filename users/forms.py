from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from .models import  Lid


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields ='__all__'
        exclude = ['id', 'user', 'lichting', 'vertical']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # self.fields['title']({'class':"input", 'placeholder': 'Add Title'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "input"})


class LidForm(ModelForm):
    class Meta:
        model = Lid
        fields = ['name','birth_date',  'email','phone',  'educations',  'short_intro', 'lid_image']
        widgets = {
            'birth_date': NumberInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(LidForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "input"})




