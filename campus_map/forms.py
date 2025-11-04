from django import forms
from django.core.exceptions import ValidationError
from .models import LandmarkPhoto, Landmark
from PIL import Image

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = LandmarkPhoto
        fields = ['image_file', 'caption']
        widgets = {
            'image_file': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'form-control',
                'id': 'photo-file-input'
            }),
            'caption': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a caption for your photo (optional)',
                'maxlength': '200'
            })
        }

    def __init__(self, *args, **kwargs):
        self.landmark = kwargs.pop('landmark', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['image_file'].required = True

    def clean_image_file(self):
        image_file = self.cleaned_data.get('image_file')

        if image_file:
            # Check file size (max 5MB)
            if image_file.size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large. Maximum size is 5MB.")

            # Check file type
            allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            ext = image_file.name.lower().split('.')[-1]
            if f'.{ext}' not in allowed_extensions:
                raise ValidationError("Invalid file type. Please upload JPEG, PNG, GIF, or WebP.")

            # Validate with PIL
            try:
                with Image.open(image_file) as img:
                    img.verify()
                image_file.seek(0)
            except Exception:
                raise ValidationError("Invalid image file.")

        return image_file

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.landmark:
            instance.landmark = self.landmark
        if self.user:
            instance.uploaded_by = self.user

        # Set order
        if instance.landmark:
            max_order = LandmarkPhoto.objects.filter(
                landmark=instance.landmark
            ).aggregate(max_order=models.Max('order'))['max_order']
            instance.order = (max_order or 0) + 1

        instance.is_approved = True  # Auto-approve for now

        if commit:
            instance.save()
        return instance