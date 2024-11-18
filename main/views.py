from django.shortcuts import render, redirect
from main.forms import AttributeForm
from main.models import Attribute
from django.http import HttpResponse
from django.core import serializers

# Tugas 4
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Tugas 6
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    user = request.user

    new_product = Attribute(
        name=name, price=price, description=description,
        stock=stock, user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


def show_xml(request):
    data = Attribute.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Attribute.objects.filter(user=request.user)
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
    context = {
        'app_name': 'Checkoutify',
        'name': request.user.username,
        'class': 'PBP E',
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

# Tugas 5
def edit_product(request, id):
    attribute_entries = Attribute.objects.get(pk = id)

    form = AttributeForm(request.POST or None, instance=attribute_entries)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    attribute_entries = Attribute.objects.get(pk = id)
    attribute_entries.delete()
    return HttpResponseRedirect(reverse('main:show_main'))




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
        messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = AttributeForm.objects.create(
            name=data["name"],
            price=int(data["price"]),
            description=data["description"],
            stock=data["stock"],
            user=request.user,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)