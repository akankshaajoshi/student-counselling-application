from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

#  = [MinValueValidator(1), MaxValueValidator(100)]

class TenthGrade(models.Model):
    math = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    science = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    english = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    hindi = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    social_science = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    student = models.OneToOneField('Student', on_delete=models.CASCADE, null=True)
     score = models.IntegerField()
    # Add more subjects as needed

class TwelfthGrade(models.Model):
    physics = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    chemistry = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    math = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    english = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    other = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    student = models.OneToOneField('Student', on_delete=models.CASCADE, null = True)
    score = models.IntegerField()

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField()

    # Personal details
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)

    
    @property
    def total_score(self):
        tenth_score = self.tenthgrade.score if hasattr(self, 'tenthgrade') else 0
        twelfth_score = self.twelfthgrade.score if hasattr(self, 'twelfthgrade') else 0
        return tenth_score + twelfth_score

