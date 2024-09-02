import django_filters

from .models import Task

class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    deadline_year = django_filters.NumberFilter(field_name='deadline', lookup_expr='year')
    deadline_month = django_filters.NumberFilter(field_name='deadline', lookup_expr='month')
    deadline_day = django_filters.NumberFilter(field_name='deadline', lookup_expr='day')

    class Meta:
        model = Task
        fields = ['status', 'deadline_year', 'deadline_month', 'deadline_day']