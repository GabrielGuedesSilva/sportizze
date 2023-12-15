from django.urls import path
from professor import views

app_name = 'professor'

urlpatterns = [
    path('professor/', views.professor, name='professor')
]