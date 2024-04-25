from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
        path('', RedirectView.as_view(url='student/')), 
        path('admin/', admin.site.urls),
        path('accounts/', include('allauth.urls')),
        path('student/', TemplateView.as_view(template_name='dashboard/student.html'), name="student"),
        path('registration/', include('registration.urls')),
]


