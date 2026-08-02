from .models import ThemeSetting

def site_experience(request):
    theme = ThemeSetting.objects.filter(is_active=True).first()
    return {'active_theme': theme}
