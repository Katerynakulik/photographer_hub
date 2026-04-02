from django import forms
from .models import PhotoProduct
from bookings.models import Photoshoot

class PhotoProductForm(forms.ModelForm):
    class Meta:
        model = PhotoProduct
        fields = ['title', 'description', 'price', 'preview_image', 'digital_file', 'is_active']
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
        fields = ['title', 'description', 'image', 'expected_dates', 'deposit_price', 'total_price', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'expected_dates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Late June 2026'}),
        }