from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_view, name='question_view'),
    path('submit/', views.submit_answers, name='submit_answers'),
]
