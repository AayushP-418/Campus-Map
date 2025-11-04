from django.db import models
from django.contrib.auth.models import User

class Landmark(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class LandmarkPhoto(models.Model):
    landmark = models.ForeignKey(Landmark, related_name='photos', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    image_file = models.ImageField(upload_to='landmark_photos/%Y/%m/%d/', blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_approved = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-uploaded_at']

    def __str__(self):
        return f"{self.landmark.name} - Photo {self.order + 1}"

    @property
    def image_url_display(self):
        if self.image_file:
            return self.image_file.url
        elif self.image_url:
            return self.image_url
        return '/static/images/placeholder.jpg'