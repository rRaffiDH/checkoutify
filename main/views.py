from django.shortcuts import render, redirect
from main.forms import AttributeForm
from main.models import Attribute
from django.http import HttpResponse
from django.core import serializers

# Tugas 4
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


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

# Tugas 4
@login_required(login_url='/login')
def show_main(request):
    attribute_entries = Attribute.objects.filter(user=request.user)
    context = {
        'app_name': 'Checkoutify',
        'name': request.user.username,
        'class': 'PBP E',
        'attribute_entries': attribute_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def add_product(request):
    form = AttributeForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        # Tugas 4
        attribute_entry = form.save(commit=False)
        attribute_entry.user = request.user
        attribute_entry.save()
        return redirect('main:show_main')  
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

# Tugas 4
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response