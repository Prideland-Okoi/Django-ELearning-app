from django.urls import path
from . import views

app_name = 'LMS'

urlpatterns = [
    path('index', views.homepage, name = 'index'),
    path('contact', views.contactview, name = 'contact'),
    path('about', views.aboutview, name = 'about'),
    path('team', views.teamview, name = 'team'),
    path('testimonial', views.testimonialview, name = 'testimonial'),
    path('base', views.baseview, name = 'base'),    
]