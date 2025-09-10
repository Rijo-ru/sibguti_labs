from django.core.management.base import BaseCommand
from django.utils import timezone
from crm_core.models import Employee, ConstructionSite, WorkType, DailyReport, EmployeeWork
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Load Mixarium demo data'

    def handle(self, *args, **options):
        self.stdout.write('Creating Mixarium demo data...')
        
        # Очистка старых данных
        EmployeeWork.objects.all().delete()
        DailyReport.objects.all().delete()
        ConstructionSite.objects.all().delete()
        WorkType.objects.all().delete()
        Employee.objects.all().delete()

        # Создание сотрудников-Смешариков
        employees_data = [
            {'first_name': 'Крош', 'last_name': 'Кроликов', 'position': 'Старший прораб', 'phone_number': '+7-900-111-22-33'},
            {'first_name': 'Ёжик', 'last_name': 'Ёжиков', 'position': 'Инженер-сметчик', 'phone_number': '+7-900-222-33-44'},
            {'first_name': 'Бараш', 'last_name': 'Баранов', 'position': 'Поэт-вдохновитель', 'phone_number': '+7-900-333-44-55'},
            {'first_name': 'Нюша', 'last_name': 'Свинкина', 'position': 'Дизайнер интерьеров', 'phone_number': '+7-900-444-55-66'},
            {'first_name': 'Пин', 'last_name': 'Пингвинов', 'position': 'Главный инженер', 'phone_number': '+7-900-555-66-77'},
            {'first_name': 'Лосяш', 'last_name': 'Лосев', 'position': 'Научный консультант', 'phone_number': '+7-900-666-77-88'},
            {'first_name': 'Совунья', 'last_name': 'Сова', 'position': 'Медик и ОТ', 'phone_number': '+7-900-777-88-99'},
            {'first_name': 'Копатыч', 'last_name': 'Медведев', 'position': 'Экскаваторщик', 'phone_number': '+7-900-888-99-00'},
        ]

        employees = {}
        for data in employees_data:
            employee = Employee.objects.create(**data)
            employees[data['first_name']] = employee
            self.stdout.write(f'Created employee: {employee}')

        # Создание видов работ
        work_types_data = [
            {'name': 'Земляные работы', 'unit': 'm3', 'cost_per_unit': 1500.00},
            {'name': 'Фундаментные работы', 'unit': 'm3', 'cost_per_unit': 8500.00},
            {'name': 'Кладка стен', 'unit': 'm2', 'cost_per_unit': 3200.00},
            {'name': 'Монтаж кровли', 'unit': 'm2', 'cost_per_unit': 2800.00},
            {'name': 'Установка окон', 'unit': 'pcs', 'cost_per_unit': 12500.00},
            {'name': 'Электромонтажные работы', 'unit': 'm2', 'cost_per_unit': 1800.00},
            {'name': 'Сантехнические работы', 'unit': 'm2', 'cost_per_unit': 2200.00},
            {'name': 'Отделочные работы', 'unit': 'm2', 'cost_per_unit': 2500.00},
        ]

        work_types = {}
        for data in work_types_data:
            work_type = WorkType.objects.create(**data)
            work_types[data['name']] = work_type
            self.stdout.write(f'Created work type: {work_type}')

        # Создание строительных объектов
        sites_data = [
            {
                'name': 'Дом Совуньи', 
                'address': 'Улица Совиная, 1', 
                'customer': 'Совунья Сова',
                'start_date': datetime(2024, 1, 15).date(),
                'end_date_plan': datetime(2024, 6, 15).date(),
                'supervisor': employees['Крош'],
                'status': 'in_progress'
            },
            {
                'name': 'Лаборатория Пина', 
                'address': 'Проспект Технический, 42', 
                'customer': 'Пин Пингвинов',
                'start_date': datetime(2024, 2, 1).date(),
                'end_date_plan': datetime(2024, 8, 1).date(),
                'supervisor': employees['Пин'],
                'status': 'in_progress'
            },
            {
                'name': 'Библиотека Лосяша', 
                'address': 'Бульвар Ученый, 7', 
                'customer': 'Лосяш Лосев',
                'start_date': datetime(2024, 3, 10).date(),
                'end_date_plan': datetime(2024, 9, 10).date(),
                'supervisor': employees['Лосяш'],
                'status': 'planning'
            },
            {
                'name': 'Салон красоты Нюши', 
                'address': 'Площадь Модная, 3', 
                'customer': 'Нюша Свинкина',
                'start_date': datetime(2023, 11, 1).date(),
                'end_date_plan': datetime(2024, 5, 1).date(),
                'end_date_actual': datetime(2024, 4, 28).date(),
                'supervisor': employees['Нюша'],
                'status': 'completed'
            },
        ]

        sites = {}
        for data in sites_data:
            site = ConstructionSite.objects.create(**data)
            sites[data['name']] = site
            self.stdout.write(f'Created construction site: {site}')

        # Создание ежедневных отчетов
        today = timezone.now().date()
        reports = []

        # Для завершенного объекта (Салон красоты Нюши)
        completed_site = sites['Салон красоты Нюши']
        report_date = completed_site.start_date
        while report_date <= completed_site.end_date_actual:
            if report_date.weekday() < 5:  # Только рабочие дни
                report = DailyReport.objects.create(
                    construction_site=completed_site,
                    date=report_date,
                    work_type=random.choice(list(work_types.values())),
                    volume_completed=random.uniform(10, 50)
                )
                reports.append(report)
            report_date += timedelta(days=1)

        # Для текущих объектов
        for site_name in ['Дом Совуньи', 'Лаборатория Пина']:
            site = sites[site_name]
            report_date = site.start_date
            while report_date <= today:
                if report_date.weekday() < 5 and random.random() > 0.3:  # 70% вероятность отчета в рабочий день
                    report = DailyReport.objects.create(
                        construction_site=site,
                        date=report_date,
                        work_type=random.choice(list(work_types.values())),
                        volume_completed=random.uniform(5, 30)
                    )
                    reports.append(report)
                report_date += timedelta(days=1)

        # Создание записей о работе сотрудников
        for report in reports:
            num_workers = random.randint(2, 5)
            site_workers = random.sample(list(employees.values()), num_workers)
            
            for worker in site_workers:
                EmployeeWork.objects.create(
                    daily_report=report,
                    employee=worker,
                    hours_worked=random.uniform(4, 10)
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created demo data: '
                f'{Employee.objects.count()} employees, '
                f'{ConstructionSite.objects.count()} sites, '
                f'{WorkType.objects.count()} work types, '
                f'{DailyReport.objects.count()} reports, '
                f'{EmployeeWork.objects.count()} work records'
            )
        )
