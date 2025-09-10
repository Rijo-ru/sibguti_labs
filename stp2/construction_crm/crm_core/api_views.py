from rest_framework import viewsets
from .models import Employee, ConstructionSite, WorkType, DailyReport
from .serializers import EmployeeSerializer, ConstructionSiteSerializer, WorkTypeSerializer, DailyReportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import ConstructionSite

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ConstructionSiteViewSet(viewsets.ModelViewSet):
    queryset = ConstructionSite.objects.all()
    serializer_class = ConstructionSiteSerializer

class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer

@api_view(['GET'])
def site_statistics(request, pk):
    """Статистика по конкретному объекту"""
    site = ConstructionSite.objects.get(pk=pk)
    reports = site.reports.all()
    
    total_volume = reports.aggregate(Sum('volume_completed'))['volume_completed__sum'] or 0
    total_cost = sum(report.total_cost() for report in reports)
    total_hours = EmployeeWork.objects.filter(daily_report__construction_site=site).aggregate(
        Sum('hours_worked')
    )['hours_worked__sum'] or 0
    
    return Response({
        'site_name': site.name,
        'total_volume': total_volume,
        'total_cost': total_cost,
        'total_hours': total_hours,
        'report_count': reports.count()
    })

@api_view(['GET'])
def overall_statistics(request):
    """Общая статистика по всем объектам"""
    total_sites = ConstructionSite.objects.count()
    active_sites = ConstructionSite.objects.filter(status='in_progress').count()
    completed_sites = ConstructionSite.objects.filter(status='completed').count()
    
    total_reports = DailyReport.objects.count()
    total_work_hours = EmployeeWork.objects.aggregate(Sum('hours_worked'))['hours_worked__sum'] or 0
    
    return Response({
        'total_sites': total_sites,
        'active_sites': active_sites,
        'completed_sites': completed_sites,
        'total_reports': total_reports,
        'total_work_hours': total_work_hours
    })