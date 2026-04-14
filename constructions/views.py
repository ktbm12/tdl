from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tdl/construction/templates/home/home.html')

def contact(request):
    return render(request, 'contact.html')
