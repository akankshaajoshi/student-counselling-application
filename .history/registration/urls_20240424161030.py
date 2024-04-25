from django.contrib import admin
from django.urls import include, path
from .views import form_view
from django.views.generic import TemplateView

urlpatterns = [
        path('details/', form_view, name="student_registration"),
        path('rankings/', form_view, name="student_rankings"),
]
