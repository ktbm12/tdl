from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Service, Project, ContactMessage, QuoteRequest, Hero

def index(request):
    services = Service.objects.all()[:3]
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    heroes = Hero.objects.filter(is_active=True)
    return render(request, 'home/home.html', {
        'services': services,
        'projects': featured_projects,
        'heroes': heroes
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

def submit_quote(request):
    if request.method == 'POST':
        name = request.POST.get('nom')
        email = request.POST.get('email')
        phone = request.POST.get('tel')
        project_type = request.POST.get('type')
        budget = request.POST.get('budget')
        description = request.POST.get('description')
        
        if name and email and project_type:
            QuoteRequest.objects.create(
                name=name,
                email=email,
                phone=phone,
                project_type=project_type,
                budget=budget,
                description=description
            )
            return JsonResponse({'status': 'success', 'message': 'Demande envoyée !'})
        return JsonResponse({'status': 'error', 'message': 'Champs manquants.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée.'}, status=405)

def about(request):
    return render(request, 'about.html')

def services(request):
    all_services = Service.objects.all()
    return render(request, 'service.html', {'services': all_services})

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'project.html', {'projects': all_projects})