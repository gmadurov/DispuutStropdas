from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput, CheckboxSelectMultiple

from users.models import Lid
from .models import Decla


class DeclaForm(ModelForm):
    class Meta:
        model = Decla
        fields = "__all__"
        exclude = ["owner", "id", "created", "senate_year"]
        widgets = {
            "senate_year": NumberInput(),
            "present": CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(DeclaForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not name in ["verwerkt", "present"]:
                field.widget.attrs.update({"class": "input"})
            elif name == "present":
                field.widget.attrs.update({"class": "CheckboxSelectMultiple"})
            else:
                field.widget.attrs.update({"class": "checkbox"})
class FicusForm(ModelForm):
    class Meta:
        model = Decla
        fields = ["verwerkt"]

    def __init__(self, *args, **kwargs):
        super(DeclaForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "checkbox"})

