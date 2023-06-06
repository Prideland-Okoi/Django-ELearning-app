from django.urls import path

app_name = 'LMS'

urlpatterns = [
    path('homepage', views.homepage, name = 'homepage'),
]