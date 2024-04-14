from django.contrib import admin
from .models import Student, TenthGrade, TwelfthGrade
from django.db.models import F



class TotalScoreOrderingFilter(admin.SimpleListFilter):
    title = 'total score ordering'
    parameter_name = 'total_score_ordering'

    def lookups(self, request, model_admin):
        return (
            ('asc', 'Ascending'),
            ('desc', 'Descending'),
        )

    def queryset(self, request, queryset):
        queryset = queryset.annotate(
            total_score=(
                F('tenthgrade__math') + F('tenthgrade__science') + F('tenthgrade__english') + 
                F('tenthgrade__hindi') + F('tenthgrade__social_science') + 
                F('twelfthgrade__physics') + F('twelfthgrade__chemistry') + 
                F('twelfthgrade__math') + F('twelfthgrade__english') + F('twelfthgrade__other')
            )
        )
        if self.value() == 'asc':
            return queryset.order_by('total_score')
        if self.value() == 'desc':
            return queryset.order_by('-total_score')



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
    list_filter = (TotalScoreOrderingFilter,)

admin.site.register(Student, StudentAdmin)