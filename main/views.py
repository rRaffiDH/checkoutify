from django.shortcuts import render, redirect
from main.forms import AttributeForm
from main.models import Attribute
from django.http import HttpResponse
from django.core import serializers
def show_xml(request):
    data = Attribute.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Attribute.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Attribute.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Attribute.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_main(request):
    attribute_entries = Attribute.objects.all()
    context = {
        'app_name': 'Checkoutify',
        'name' : 'Raffi Dary Hibban',
        'class': 'PBP E',
        'attribute_entries': attribute_entries
    }

    return render(request, "main.html", context)

def add_product(request):
    form = AttributeForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')  
    context = {'form': form}
    return render(request, 'add_product.html', context)
# Create your views here.
