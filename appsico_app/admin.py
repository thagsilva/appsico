from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Medical_Record)