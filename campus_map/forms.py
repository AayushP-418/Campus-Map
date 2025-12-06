from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
            instance.save()
        return instance

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'your.email@example.com'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = LandmarkPhoto
        fields = ['caption', 'image_file']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Add a caption (optional)', 'maxlength': '200', 'class': 'form-control'}),
            'image_file': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_file'].required = False
        self.fields['caption'].required = False
    
    def clean_image_file(self):
        image_file = self.cleaned_data.get('image_file')
        if image_file and image_file.size > 5 * 1024 * 1024:
            raise ValidationError("Image file too large. Maximum size is 5MB.")
        return image_file