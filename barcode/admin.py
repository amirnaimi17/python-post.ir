from django.contrib import admin
from parler.admin import TranslatableAdmin

# Register your models here.
from barcode.models import StaticTypes


class AdminStaticTypes(TranslatableAdmin):
    list_display = ['type', 'group_type', 'value']
    list_filter = ['group_type']


admin.site.register(StaticTypes, AdminStaticTypes)