from django import forms
from .models import Student, TenthGrade, TwelfthGrade

class TenthGradeForm(forms.ModelForm):
    class Meta:
        model = TenthGrade
        fields = '__all__'

class TwelfthGradeForm(forms.ModelForm):
    class Meta:
        model = TwelfthGrade
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'