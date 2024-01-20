from django.contrib import admin
from admissions.models import student


class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'fathername', 'classname', 'contact']


# Register your models here.
admin.site.register(student, studentadmin)
