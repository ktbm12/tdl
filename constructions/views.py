from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, ContactMessage

def index(request):
    services = Service.objects.all()[:3]
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    return render(request, 'home/home.html', {
        'services': services,
        'projects': featured_projects
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        project_type = request.POST.get('project_type')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                project_type=project_type,
                message=message
            )
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('contact')
        else:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
            
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    all_services = Service.objects.all()
    return render(request, 'service.html', {'services': all_services})

def projects(request):
    all_projects = Project.objects.all()
    # Categorization could be done in template or here
    return render(request, 'project.html', {'projects': all_projects})