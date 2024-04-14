from django.contrib import admin
from .models import Student, TenthGrade, TwelfthGrade

class TenthGradeInline(admin.StackedInline):
    model = TenthGrade
    can_delete = False
    verbose_name_plural = 'Tenth Grade'

class TwelfthGradeInline(admin.StackedInline):
    model = TwelfthGrade
    can_delete = False
    verbose_name_plural = 'Twelfth Grade'

class StudentAdmin(admin.ModelAdmin):
    inlines = (TenthGradeInline, TwelfthGradeInline)
    list_filter= [""]

admin.site.register(Student, StudentAdmin)