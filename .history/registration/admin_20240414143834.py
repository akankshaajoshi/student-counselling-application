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
    list_display = ('rank', 'first_name', 'last_name', 'total_score',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            total_score=(
                F('tenthgrade__math') + F('tenthgrade__science') + F('tenthgrade__english') + 
                F('tenthgrade__hindi') + F('tenthgrade__social_science') + 
                F('twelfthgrade__physics') + F('twelfthgrade__chemistry') + 
                F('twelfthgrade__math') + F('twelfthgrade__english') + F('twelfthgrade__other')
            )
        )
        qs = qs.annotate(rank=Window(expression=Rank(), order_by=F('total_score').desc()))
        return qs

    def total_score(self, obj):
        return obj.total_score
    total_score.admin_order_field = 'total_score'  # Allows column order sorting


    def rank(self, obj):
        return obj.rank
    rank.admin_order_field = 'rank'  # Allows column order sorting
admin.site.register(Student, StudentAdmin)