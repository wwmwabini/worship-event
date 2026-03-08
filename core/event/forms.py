from django  import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'phone', 'worship_type', 'payment_transaction', 'payment_number']