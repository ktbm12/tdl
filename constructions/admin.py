from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django import forms
from .models import Service, Project, ContactMessage, SiteSetting, QuoteRequest, Hero

# ─── Liste des icônes Material Symbols les plus utiles en construction ─────────
CONSTRUCTION_ICONS = [
    # Bâtiment & Structure
    ("apartment", "apartment — Immeuble"),
    ("foundation", "foundation — Fondation"),
    ("home", "home — Maison"),
    ("home_work", "home_work — Bureau/Résidence"),
    ("villa", "villa — Villa"),
    ("warehouse", "warehouse — Entrepôt"),
    ("domain", "domain — Bâtiment commercial"),
    ("factory", "factory — Usine"),
    # Ingénierie & Travaux
    ("engineering", "engineering — Ingénierie"),
    ("construction", "construction — Construction"),
    ("handyman", "handyman — Artisan"),
    ("build", "build — Outils"),
    ("architecture", "architecture — Architecture"),
    ("precision_manufacturing", "precision_manufacturing — Fabrication"),
    ("plumbing", "plumbing — Plomberie"),
    ("electrical_services", "electrical_services — Électricité"),
    # Outils & Équipements
    ("hardware", "hardware — Quincaillerie"),
    ("settings", "settings — Paramètres"),
    ("straighten", "straighten — Mesure"),
    ("square_foot", "square_foot — Métré"),
    ("carpenter", "carpenter — Menuiserie"),
    # Environnement & Durabilité
    ("park", "park — Espaces verts"),
    ("water", "water — Eau / Hydraulique"),
    ("forest", "forest — Forêt"),
    ("solar_power", "solar_power — Énergie solaire"),
    ("recycling", "recycling — Recyclage"),
    ("eco", "eco — Écologie"),
    # Transport & Infrastructures
    ("traffic", "traffic — Voirie"),
    ("bridge", "bridge — Pont"),
    ("road", "road — Route"),
    ("train", "train — Rail"),
    # Sécurité & Contrôle
    ("verified", "verified — Certification"),
    ("security", "security — Sécurité"),
    ("shield", "shield — Protection"),
    ("gpp_good", "gpp_good — Qualité certifiée"),
    # Gestion & Planification
    ("calendar_month", "calendar_month — Planning"),
    ("checklist", "checklist — Contrôle qualité"),
    ("assignment", "assignment — Devis/Rapport"),
    ("supervised_user_circle", "supervised_user_circle — Équipe"),
    ("groups", "groups — Équipes"),
    ("handshake", "handshake — Partenariat"),
]

class IconPickerWidget(forms.Select):
    """Widget déroulant avec prévisualisation de l'icône Material Symbol."""
    class Media:
        css = {
            'all': ['https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@400,0&display=swap']
        }

    def create_option(self, name, value, label, selected, index, subgroup=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subgroup, attrs)
        if value:
            option['attrs']['data-icon'] = value
        return option

class ServiceAdminForm(forms.ModelForm):
    icon = forms.ChoiceField(
        choices=[("", "— Choisir une icône —")] + CONSTRUCTION_ICONS,
        widget=forms.Select(attrs={'style': 'font-family: monospace; font-size: 14px;'}),
        label="Icône (Material Symbol)",
        help_text=mark_safe(
            'Choisissez une icône dans la liste. '
            '<a href="https://fonts.google.com/icons" target="_blank" style="color:#fe771b;font-weight:bold;">'
            '→ Voir toutes les icônes Material Symbols</a>'
        )
    )

    class Meta:
        model = Service
        fields = '__all__'


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('icon_preview', 'title', 'reference', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'reference')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<span class="material-symbols-outlined" style="font-family:\'Material Symbols Outlined\'; '
                'font-size:24px; vertical-align:middle; color:#170f66;">{}</span> '
                '<code style="font-size:12px; color:#777;">{}</code>',
                obj.icon, obj.icon
            )
        return "—"
    icon_preview.short_description = "Icône"

    class Media:
        css = {
            'all': (
                'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@400,0&display=swap',
            )
        }


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
    search_fields = ('name', 'email', 'description')
    readonly_fields = ('name', 'email', 'phone', 'project_type', 'budget', 'description', 'created_at')
    list_editable = ('is_read',)

    def has_add_permission(self, request):
        return False


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone')

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()
