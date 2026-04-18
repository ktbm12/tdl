from django.contrib import admin
from .models import Service, Project, ContactMessage, SiteSetting, QuoteRequest, Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'reference', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'reference')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'location')
    list_editable = ('is_featured',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'is_read', 'created_at')
    list_filter = ('is_read', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'project_type', 'message', 'created_at')
    list_editable = ('is_read',)

    def has_add_permission(self, request):
        return False

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'project_type', 'is_read', 'created_at')
    list_filter = ('is_read', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'message', 'description')
    readonly_fields = ('name', 'email', 'phone', 'project_type', 'budget', 'description', 'created_at')
    list_editable = ('is_read',)

    def has_add_permission(self, request):
        return False

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone')
    
    def has_add_permission(self, request):
        # Only one instance allowed
        return not SiteSetting.objects.exists()
