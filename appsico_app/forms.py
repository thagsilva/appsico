
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Doctors, Patients, Receptionist

class DoctorRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Doctors
        fields = [
            'patient_user',
            'crp',
        ]

class PatientRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Patients
        fields = ['address']


class CustomUserCreationForm(UserCreationForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['user_name', 'cpf', 'phonenumber', 'email', 'password', 'is_psychologist', 'is_patient', 'is_receptionist']
