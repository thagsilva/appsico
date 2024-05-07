from django.db import models
from users.models import Doctors, Patients

class Medical_Record(models.Model):

    record = models.TextField(
        verbose_name=('Entrada'),
    )

    date_created = models.DateTimeField(
        verbose_name=('Criado em: '),
        auto_now_add=True, 
        help_text=('Data de criação da entrada no prontuário')
    )

    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Prontuário')
        verbose_name_plural = ('Prontuários')
