from django.contrib import admin

from .models import AcademicStanding, Student


class AcademicStandingAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'year', 'standing')


admin.site.register(AcademicStanding, AcademicStandingAdmin)
admin.site.register(Student)
