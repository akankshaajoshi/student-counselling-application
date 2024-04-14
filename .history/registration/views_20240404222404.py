from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render
from django.shortcuts import render
from django.forms import inlineformset_factory
from .models import Student, TenthGrade, TwelfthGrade
from .forms import StudentForm, TenthGradeForm, TwelfthGradeForm

def get_user_details(user):
    social_info = SocialAccount.objects.filter(user=user).first()
    if social_info:
        email = social_info.user.email
        first_name = social_info.user.first_name
        last_name = social_info.user.last_name
        return email, first_name, last_name
    else:
        return None
    

def form_view(request):
    TenthGradeFormSet = inlineformset_factory(Student, TenthGrade, form=TenthGradeForm, extra=1)
    TwelfthGradeFormSet = inlineformset_factory(Student, TwelfthGrade, form=TwelfthGradeForm, extra=1)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            tenth_formset = TenthGradeFormSet(request.POST, instance=student)
            twelfth_formset = TwelfthGradeFormSet(request.POST, instance=student)
            if tenth_formset.is_valid() and twelfth_formset.is_valid():
                tenth_formset.save()
                twelfth_formset.save()
                # Redirect to a new URL:
                # return HttpResponseRedirect('/success/')
    else:
        form = StudentForm()
        tenth_formset = TenthGradeFormSet()
        twelfth_formset = TwelfthGradeFormSet()

    return render(request, 'registration/details.html', {
        'form': form,
        'tenth_formset': tenth_formset,
        'twelfth_formset': twelfth_formset,
    })