from .models import SiteSetting

def site_settings(request):
    settings = SiteSetting.objects.first()
    if not settings:
        settings = SiteSetting()
    return {'site_settings': settings}
