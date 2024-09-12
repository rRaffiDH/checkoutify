from django.forms import ModelForm
from .models import Attribute

class AttributeForm(ModelForm):
    class Meta:
        model = Attribute
        fields = ["name", "price", "description", "stock"]