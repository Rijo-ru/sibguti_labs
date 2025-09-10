from django.contrib import admin
from .models import Employee, ConstructionSite, WorkType, DailyReport, EmployeeWork

class EmployeeWorkInline(admin.TabularInline):
    model = EmployeeWork
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'phone_number')
    list_filter = ('position',)
    search_fields = ('last_name', 'first_name')

@admin.register(ConstructionSite)
class ConstructionSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'customer', 'start_date', 'end_date_plan', 'status', 'supervisor')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'address', 'customer')

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'cost_per_unit', 'parent')
    list_filter = ('unit',)

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'construction_site', 'work_type', 'volume_completed', 'total_cost')
    list_filter = ('date', 'construction_site')
    inlines = [EmployeeWorkInline]

@admin.register(EmployeeWork)
class EmployeeWorkAdmin(admin.ModelAdmin):
    list_display = ('daily_report', 'employee', 'hours_worked')
    list_filter = ('daily_report__date', 'employee')