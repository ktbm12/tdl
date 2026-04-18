from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    icon = models.CharField(max_length=50, verbose_name="Icône (Material Symbol)", help_text="Ex: apartment, engineering, foundation")
    image = models.ImageField(upload_to='services/', verbose_name="Image", blank=True, null=True)
    reference = models.CharField(max_length=20, verbose_name="Référence", help_text="Ex: TDL-CB")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order']

    def __str__(self):
        return self.title

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('houses', 'Maisons'),
        ('infrastructure', 'Infrastructure'),
        ('renovation', 'Rénovation'),
    ]
    title = models.CharField(max_length=200, verbose_name="Titre du projet")
    location = models.CharField(max_length=200, verbose_name="Localisation")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Catégorie")
    image = models.ImageField(upload_to='projects/', verbose_name="Image")
    is_featured = models.BooleanField(default=False, verbose_name="Mettre en avant")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    project_type = models.CharField(max_length=100, verbose_name="Type de projet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    is_read = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']

    def __str__(self):
        return f"Message de {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class QuoteRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Téléphone", blank=True)
    project_type = models.CharField(max_length=100, verbose_name="Type de projet")
    budget = models.CharField(max_length=100, verbose_name="Budget estimé", blank=True)
    description = models.TextField(verbose_name="Description du projet")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de demande")
    is_read = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        verbose_name = "Demande de devis"
        verbose_name_plural = "Demandes de devis"
        ordering = ['-created_at']

    def __str__(self):
        return f"Devis {self.project_type} - {self.name}"

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="TDL Construction", verbose_name="Nom du site")
    logo = models.ImageField(upload_to='settings/', verbose_name="Logo", blank=True, null=True)
    email = models.EmailField(verbose_name="Email de contact")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp", blank=True)
    address = models.TextField(verbose_name="Adresse")
    description = models.TextField(verbose_name="Description courte", blank=True)
    
    facebook_url = models.URLField(blank=True, verbose_name="Lien Facebook")
    linkedin_url = models.URLField(blank=True, verbose_name="Lien LinkedIn")
    instagram_url = models.URLField(blank=True, verbose_name="Lien Instagram")

    class Meta:
        verbose_name = "Paramètre du site"
        verbose_name_plural = "Paramètres du site"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        if not self.pk and SiteSetting.objects.exists():
            return # Only one instance allowed
        return super().save(*args, **kwargs)
