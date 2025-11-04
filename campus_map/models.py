from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    # Keep old field for backward compatibility
    image_url = models.URLField(max_length=500, blank=True, null=True)

    # NEW: File upload field
    image_file = models.ImageField(
        upload_to='landmark_photos/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Upload a photo file"
    )

    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    # NEW: User tracking
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='uploaded_photos'
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)  # Auto-approve for now
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-is_approved', 'order', '-uploaded_at']

    def __str__(self):
        return f"{self.landmark.name} - Photo {self.order + 1}"

    @property
    def image_url_display(self):
        """Return the appropriate image URL"""
        if self.image_file:
            return self.image_file.url
        elif self.image_url:
            return self.image_url
        else:
            return '/static/images/placeholder.jpg'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image_file:
            self.resize_image()

    def resize_image(self):
        """Resize uploaded images"""
        if not self.image_file:
            return
        try:
            with Image.open(self.image_file.path) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                max_size = (1200, 800)
                if img.width > max_size[0] or img.height > max_size[1]:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    img.save(self.image_file.path, optimize=True, quality=85)
        except Exception as e:
            print(f"Error resizing image: {e}")

class PhotoLike(models.Model):
    photo = models.ForeignKey(LandmarkPhoto, on_delete=models.CASCADE, related_name='photo_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('photo', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.photo}"