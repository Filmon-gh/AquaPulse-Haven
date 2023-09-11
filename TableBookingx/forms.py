from django import forms
from django.utils import timezone
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation  
        fields = ['first_name', 'last_name', 'email', 'date', 'time', 'party_size', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'party_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        now = timezone.now().date()
        selected_datetime = timezone.datetime.combine(date, time)

        if date < now:
            raise forms.ValidationError("You cannot book a reservation in the past.")

        # Check if a reservation with the same date and time already exists
        if Reservation.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("A reservation for this date and time already exists.")

        return cleaned_data