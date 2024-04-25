
from django.urls import path
from .views import form_view, rankings_view

urlpatterns = [
        path('details/', form_view, name="student_registration"),
        path('rankings/', rankings_view, name="student_rankings"),
]
