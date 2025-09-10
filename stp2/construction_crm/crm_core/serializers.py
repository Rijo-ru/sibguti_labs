from rest_framework import serializers
from .models import Employee, ConstructionSite, WorkType, DailyReport, EmployeeWork

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'

class ConstructionSiteSerializer(serializers.ModelSerializer):
    supervisor_name = serializers.CharField(source='supervisor.__str__', read_only=True)
    
    class Meta:
        model = ConstructionSite
        fields = '__all__'

class EmployeeWorkSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.__str__', read_only=True)
    
    class Meta:
        model = EmployeeWork
        fields = '__all__'

class DailyReportSerializer(serializers.ModelSerializer):
    work_type_name = serializers.CharField(source='work_type.name', read_only=True)
    employee_works = EmployeeWorkSerializer(many=True, read_only=True)
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = DailyReport
        fields = '__all__'
