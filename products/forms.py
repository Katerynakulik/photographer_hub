from django import forms
from .models import PhotoProduct
from bookings.models import Photoshoot
from django.core.exceptions import ValidationError


class PhotoProductForm(forms.ModelForm):
    class Meta:
        model = PhotoProduct
        fields = ['title', 'description', 'price',
                  'preview_image', 'digital_file', 'is_active']
        # Mentor Note: Styling inputs to match our Warm Ivory theme
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'preview_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'digital_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PhotoshootForm(forms.ModelForm):
    class Meta:
        model = Photoshoot
        fields = ['title', 'description', 'image', 'expected_dates',
                  'deposit_price', 'total_price', 'is_active']

        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'id': 'file-upload'
                # Mentor Note: removed 'multiple': True to fix the ValueError
            }),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Session Title'}),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Describe the mood...'
            }),
            'expected_dates': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., December 2026'}),
            'deposit_price': forms.NumberInput(attrs={'class': 'form-input'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-input'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # 10485760 байт = 10 МБ
            if image.size > 10 * 1024 * 1024:
                raise ValidationError("File is too large. Max size is 10MB.")
        return image
