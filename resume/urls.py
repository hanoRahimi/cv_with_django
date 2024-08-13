
from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('resume', resume_view, name='resume'),
    path('portfolio', project_view, name='project'),
    path('contact', contact_view, name='contact'),
]
