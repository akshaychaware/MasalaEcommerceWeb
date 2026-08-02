from typing import Any
from django.views.generic import TemplateView
from gallery.models import Photo
from letters.models import BirthdayLetter
from music.models import Track
from surprise.models import Reason, SecretMessage
from timeline.models import TimelineEvent
from .models import HomeExperience

class HomeView(TemplateView):
    template_name = 'core/home.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'experience': HomeExperience.objects.filter(is_active=True).first() or HomeExperience(),
            'letter': BirthdayLetter.objects.filter(is_active=True).first(),
            'hero_photo': Photo.objects.filter(is_hero=True).first(),
            'photos': Photo.objects.all()[:8],
            'events': TimelineEvent.objects.filter(is_published=True),
            'reasons': Reason.objects.filter(is_published=True),
            'secret': SecretMessage.objects.filter(is_active=True).first(),
            'tracks': Track.objects.filter(is_active=True),
        })
        return context
