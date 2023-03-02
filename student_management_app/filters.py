import django_filters

from .models import *


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = '__all__'