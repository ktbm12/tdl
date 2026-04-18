from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'service.html')

def projects(request):
    return render(request, 'project.html')
 