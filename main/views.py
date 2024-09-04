from django.shortcuts import render
def show_main(request):
    context = {
        'app_name': 'Checkoutify',
        'name' : 'Raffi Dary Hibban',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
