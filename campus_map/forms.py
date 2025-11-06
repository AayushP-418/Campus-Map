from django import forms
from django.core.exceptions import ValidationError
from .models import LandmarkPhoto

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = LandmarkPhoto
        fields = ['image_file', 'caption']
        widgets = {
            'image_file': forms.FileInput(attrs={'accept': 'image/*'}),
            'caption': forms.TextInput(attrs={'placeholder': 'Add a caption (optional)', 'maxlength': '200'})
        }

    def __init__(self, *args, **kwargs):
        self.landmark = kwargs.pop('landmark', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['image_file'].required = True

    def clean_image_file(self):
        image_file = self.cleaned_data.get('image_file')
        if image_file and image_file.size > 5 * 1024 * 1024:
            raise ValidationError("Image file too large. Maximum size is 5MB.")
        return image_file

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.landmark:
            instance.landmark = self.landmark
        if self.user:
            instance.uploaded_by = self.user
        instance.is_approved = True
        
        if commit:
            # Save the instance (this will automatically save the file to disk)
            instance.save()
        return instance