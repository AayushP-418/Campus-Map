from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.campus_map_view, name='campus_map'),
    path('landmark/<int:landmark_id>/', views.landmark_detail, name='landmark_detail'),

    # NEW: Photo upload URLs
    path('landmark/<int:landmark_id>/upload/', views.upload_photo, name='upload_photo'),
    path('landmark/<int:landmark_id>/photos/', views.landmark_photos_api, name='landmark_photos_api'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)