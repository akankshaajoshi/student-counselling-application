from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from django.forms import inlineformset_factory
from .models import Student, TenthGrade, TwelfthGrade
from .forms import StudentForm, TenthGradeForm, TwelfthGradeForm
from django.forms import inlineformset_factory

def get_user_details(user):
    social_info = SocialAccount.objects.filter(user=user).first()
    if social_info:
        email = social_info.user.email
        first_name = social_info.user.first_name
        last_name = social_info.user.last_name
        return email, first_name, last_name
    else:
        return None


def rankings_view(request):
    return render(request, 'registration/rankings.html')

def form_view(request):
    TenthGradeFormSet = inlineformset_factory(Student, TenthGrade, form=TenthGradeForm, extra=1, can_delete=False)
    TwelfthGradeFormSet = inlineformset_factory(Student, TwelfthGrade, form=TwelfthGradeForm, extra=1, can_delete=False)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        tenth_formset = TenthGradeFormSet(request.POST)
        twelfth_formset = TwelfthGradeFormSet(request.POST)
        if form.is_valid() and tenth_formset.is_valid() and twelfth_formset.is_valid():
            student = form.save()
            tenth_formset.instance = student
            twelfth_formset.instance = student
            tenth_formset.save()
            twelfth_formset.save()
    else:
        form = StudentForm()
        tenth_formset = TenthGradeFormSet()
        twelfth_formset = TwelfthGradeFormSet()

    return render(request, 'registration/details.html', {
        'form': form,
        'tenth_formset': tenth_formset,
        'twelfth_formset': twelfth_formset,
    })