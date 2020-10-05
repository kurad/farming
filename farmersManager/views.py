from django.shortcuts import render

def index(request):
    return render(request,'farmers/index.html')

# Create your views here.
