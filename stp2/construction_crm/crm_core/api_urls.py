from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EmployeeViewSet, ConstructionSiteViewSet, WorkTypeViewSet, DailyReportViewSet
from django.urls import path
from .api_views import site_statistics, overall_statistics

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'sites', ConstructionSiteViewSet)
router.register(r'work-types', WorkTypeViewSet)
router.register(r'reports', DailyReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/overall/', overall_statistics, name='overall-statistics'),
    path('sites/<int:pk>/statistics/', site_statistics, name='site-statistics'),
]
