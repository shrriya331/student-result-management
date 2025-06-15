from django.urls import path
from . import views

urlpatterns = [
    path('add-marks/', views.add_marks, name='add_marks'),
]
