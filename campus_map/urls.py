from django.urls import path
from . import views

urlpatterns = [
    path('', views.campus_map_view, name='campus_map'),
    path('landmark/<int:landmark_id>/', views.landmark_detail, name='landmark_detail'),
    path('landmark/<int:landmark_id>/upload/', views.upload_photo, name='upload_photo'),
    path('landmark/<int:landmark_id>/photos/', views.landmark_photos_api, name='landmark_photos_api'),
    path('accounts/register/', views.register, name='register'),
    path('my-photos/', views.my_photos, name='my_photos'),
    path('photo/<int:photo_id>/edit/', views.edit_photo, name='edit_photo'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
]