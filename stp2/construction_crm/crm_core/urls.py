from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sites/', views.ConstructionSiteListView.as_view(), name='construction_site_list'),
    path('sites/<int:pk>/', views.ConstructionSiteDetailView.as_view(), name='construction_site_detail'),
]
