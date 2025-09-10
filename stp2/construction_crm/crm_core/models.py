from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    position = models.CharField(max_length=150, verbose_name='Должность')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

class ConstructionSite(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Планирование'),
        ('in_progress', 'В работе'),
        ('on_hold', 'На паузе'),
        ('completed', 'Завершен'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название объекта')
    address = models.TextField(verbose_name='Адрес')
    customer = models.CharField(max_length=255, verbose_name='Заказчик')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date_plan = models.DateField(verbose_name='Плановая дата завершения')
    end_date_actual = models.DateField(null=True, blank=True, verbose_name='Фактическая дата завершения')
    supervisor = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='sites', verbose_name='Прораб')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning', verbose_name='Статус')

    class Meta:
        verbose_name = 'Строительный объект'
        verbose_name_plural = 'Строительные объекты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('construction_site_detail', kwargs={'pk': self.pk})

class WorkType(models.Model):
    UNIT_CHOICES = [
        ('m2', 'м²'),
        ('m3', 'м³'),
        ('pcs', 'шт.'),
    ]

    name = models.CharField(max_length=200, verbose_name='Наименование работы')
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, verbose_name='Единица измерения')
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость за единицу')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительский вид работы')

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

    def __str__(self):
        return f"{self.name} ({self.get_unit_display()})"

class DailyReport(models.Model):
    construction_site = models.ForeignKey(ConstructionSite, on_delete=models.CASCADE, related_name='reports', verbose_name='Объект')
    date = models.DateField(verbose_name='Дата отчета')
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, verbose_name='Вид работы')
    volume_completed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Выполненный объем')

    class Meta:
        verbose_name = 'Ежедневный отчет'
        verbose_name_plural = 'Ежедневные отчеты'
        ordering = ['-date']

    def __str__(self):
        return f"Отчет по {self.construction_site} за {self.date}"

    def total_cost(self):
        return self.volume_completed * self.work_type.cost_per_unit
    total_cost.short_description = 'Общая стоимость'

class EmployeeWork(models.Model):
    daily_report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='employee_works')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='Сотрудник')
    hours_worked = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Отработано часов')

    class Meta:
        verbose_name = 'Работа сотрудника'
        verbose_name_plural = 'Работы сотрудников'

    def __str__(self):
        return f"{self.employee} - {self.hours_worked}ч."