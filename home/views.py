from django.shortcuts import render

# Create your views here.

def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)
