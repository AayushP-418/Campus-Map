from django.db import models

# Create your models here.


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
    image_url = models.URLField(max_length=500)
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"{self.landmark.name} - Photo {self.order + 1}"

