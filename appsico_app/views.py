# views.py
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, DoctorRegistrationForm, PatientRegistrationForm
from .models import CustomUser, Doctors, Patients

class UserRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')  # Redirect to homepage or any other page after registration

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        # Depending on the selected role, save the corresponding model
        if user.is_doctor:
            doctor_form = DoctorRegistrationForm(self.request.POST)
            if doctor_form.is_valid():
                doctor = doctor_form.save(commit=False)
                doctor.user = user
                doctor.save()
        elif user.is_patient:
            patient_form = PatientRegistrationForm(self.request.POST)
            if patient_form.is_valid():
                patient = patient_form.save(commit=False)
                patient.user = user
                patient.save()
        elif user.is_receptionist:
            pass

        login(self.request, user)  # Automatically log the user in
        return redirect(self.success_url)

class DoctorRegistrationView(CreateView):
    model = Doctors
    form_class = DoctorRegistrationForm
    template_name = 'registration/registration_psico.html'

    def form_valid(self, form):
        doctor = form.save(commit=False)
        user = self.request.user
        doctor.user = user
        doctor.save()
        return redirect('home')

class PatientRegistrationView(CreateView):
    model = Patients
    form_class = PatientRegistrationForm
    template_name = 'registration/registration_patient.html'

    def form_valid(self, form):
        patient = form.save(commit=False)
        user = self.request.user
        patient.user = user
        patient.save()
        return redirect('home')


