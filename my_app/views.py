from django.shortcuts import render

def index(request):
    return render(request, 'my_app/index.html')

def about(request):
    return render(request, 'my_app/about.html')

# Create your views here.
