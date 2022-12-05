import django_filters
from django.db import models

from goals.models import Goal


class GoalFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Goal
        fields = {'category': ['exact', 'in'],
                  'priority': ['exact', 'in'],
                  'due_date': ['lte', 'gte'],
                  'status': ['exact', 'in']}
        filter_overrides = {
            models.DateTimeField: {"filter_class": django_filters.IsoDateTimeFilter},
        }


# class GoalFilter(django_filters.rest_framework.FilterSet):
#     # category = django_filters.CharFilter()
#     # category__exact = django_filters.CharFilter(field_name='category', lookup_expr='exact')
#     # category__in = django_filters.CharFilter(field_name='category', lookup_expr='in')
#     title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
#
#     class Meta:
#         model = Goal
#         fields = ['title']
#         # fields = ['category__title']
#         # filter_overrides = {
#         #     models.DateTimeField: {"filter_class": django_filters.IsoDateTimeFilter},
#         # }