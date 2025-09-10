from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ConstructionSite, DailyReport

class ConstructionSiteListView(ListView):
    model = ConstructionSite
    template_name = 'crm_core/construction_site_list.html'
    context_object_name = 'sites'
    paginate_by = 10

class ConstructionSiteDetailView(DetailView):
    model = ConstructionSite
    template_name = 'crm_core/construction_site_detail.html'
    context_object_name = 'site'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = DailyReport.objects.filter(
            construction_site=self.object
        ).select_related('work_type').prefetch_related('employee_works__employee')
        return context

def home_view(request):
    active_sites = ConstructionSite.objects.filter(status='in_progress')[:5]
    recent_reports = DailyReport.objects.select_related(
        'construction_site', 'work_type'
    ).order_by('-date')[:10]
    
    return render(request, 'crm_core/home.html', {
        'active_sites': active_sites,
        'recent_reports': recent_reports,
    })
