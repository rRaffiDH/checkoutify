from django.forms import ModelForm
from .models import Attribute
# Tugas 6
from django.utils.html import strip_tags

class AttributeForm(ModelForm):
    class Meta:
        model = Attribute
        fields = ["name", "price", "description", "stock"]
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)