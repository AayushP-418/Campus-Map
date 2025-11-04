from django.urls import path
from . import views

urlpatterns = [
    path('', views.campus_map_view, name='campus_map'),
]

