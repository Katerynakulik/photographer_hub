from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(
        attrs={'placeholder': 'Your First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(
        attrs={'placeholder': 'Your Last Name'}))
    # Наша "галочка" для розсилки
    subscribe_newsletter = forms.BooleanField(
        label='I want to receive updates on new sessions and special offers',
        required=False,
        initial=True  # за замовчуванням стоятиме "так"
    )

    def save(self, request):
        # Спочатку зберігаємо стандартні поля (email, password)
        user = super(CustomSignupForm, self).save(request)
        # Додаємо наші кастомні імена
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
