from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput, CheckboxSelectMultiple
from .models import Decla


class DeclaForm(ModelForm):
    class Meta:
        model = Decla
        fields = "__all__"
        exclude = ["owner", "id", "created"]
        widgets = {
            "senate_year": NumberInput(),
            "present": CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(DeclaForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not name in ["verwerkt", "present"]:
                field.widget.attrs.update({"class": "input"})
            else:
                field.widget.attrs.update({"class": "checkbox"})
