from django.utils import timezone
from .models import ConstructionSite

def global_context(request):
    return {
        'current_date': timezone.now().strftime('%d.%m.%Y'),
        'total_sites_count': ConstructionSite.objects.count(),
        'active_sites_count': ConstructionSite.objects.filter(status='in_progress').count(),
    }
