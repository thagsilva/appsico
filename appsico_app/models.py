from django.db import models
from django.core import validators
from django.contrib.auth.models import User
import re
from enum import Enum


class TRANSACTIONS_STATUS(str, Enum):
    PAYED = "PAYED"
    IN_PAYMENT = "IN_PAYMENT"
    START_PROCESS = "START_PROCESS"
    

class Patients(User):
      
    phonenumber = models.CharField(
    verbose_name= 'Número de telefone', 
    max_length=30,
    unique=True,
    help_text='Ex.: (XX)XXXX-XXXX', 
    validators=[validators.RegexValidator(re.compile(r'^\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}$'),
                                            'Insira um número válido', 'Inválido')]
    )

    address = models.CharField(
        verbose_name='Endereço', 
        max_length=30,
        unique=True,
        help_text='Ex.: Rua/Av. XXX, NºXX, Complemento (se houver) - Bairro, Cidade, Estado - CEP',
    )
     
    user_name = models.CharField(
        verbose_name = 'Nome', 
        max_length = 30,
        help_text = 'Insira seu nome completo. Ex.: João Santos Silva', 
        validators = [ validators.RegexValidator(re.compile(r''), 'Insira um nome válido', 'Inválido')]
    )
    
    cpf = models.CharField(
        verbose_name = 'CPF',
        primary_key = True,
        max_length = 30,
        unique = True,
        help_text = 'XXX.XXX.XXX-XX', 
        validators = [validators.RegexValidator(re.compile(r'^(?:[0-9]{3}[\.|-]){3}[0-9]{2}$'),
                                               'Insira um número válido', 'Inválido')]
    )
    
    is_psicologist = models.BooleanField(default=False)
    
    is_patient = True
    
    is_superuser = False
    
    is_staff = False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'cpf',
        'user_name',
        'phonenumber'
    ]
    
    
    def __str__(self) -> str:
        return self.user_name, self.email, self.cpf
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        
    
class Doctors(User):
       
    phonenumber = models.CharField(
    verbose_name='Número de telefone', 
    max_length=30,
    unique=True,
    help_text='Ex.: (XX)XXXX-XXXX', 
    validators=[validators.RegexValidator(re.compile(r'^\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}$'),
                                            'Insira um número válido', 'Inválido')]
    )
     
    user_name = models.CharField(
        verbose_name = 'Nome', 
        max_length = 30,
        help_text = 'Insira seu nome completo. Ex.: João Santos Silva', 
        validators = [ validators.RegexValidator(re.compile(r''), 'Insira um nome válido', 'Inválido')]
    )
    
    cpf = models.CharField(
        verbose_name ='CPF',
        primary_key = True,
        max_length = 30,
        unique = True,
        help_text ='XXX.XXX.XXX-XX', 
        validators = [validators.RegexValidator(re.compile(r'^(?:[0-9]{3}[\.|-]){3}[0-9]{2}$'),
                                               'Insira um número válido', 'Inválido')]
    )
    
    crp = models.CharField(
        verbose_name='CRP',
        max_length=30,
        unique=True,
        help_text='XX/XXXXXX', 
        validators=[validators.RegexValidator(re.compile(r'^[0-9]{2}\/[0-9]{6}$'),
                                               'Insira um número válido', 'Inválido')]
    )
    
    patient_user = models.ForeignKey(
        Patients,
        on_delete = models.CASCADE
    )
    
    
    is_psicologist = True
    
    is_patient = models.BooleanField(default=False)
      

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'crp',
        'cpf',
        'user_name',
        'phonenumber',
        'patients',
        'is_patient',
        'is_superuser',
        'is_staff'
    ]
    
    
    def __str__(self) -> str:
        return self.user_name, self.email, self.crp
      
    class Meta:
        verbose_name = 'Psicólogo'
        verbose_name_plural = 'Psicólogos'
        
    @classmethod
    def is_patient_true(
        cls,
        is_patient: bool
    ):
    
        """
        It will create a patients user once this field is_patient is setted to true
        """
        
        if is_patient:
            pat = Patients()
            pat.email = cls.email
            pat.phonenumber = cls.phonenumber
            pat.cpf = cls.cpf
            pat.user_name = cls.user_name
            pat.is_psicologist = True
            
            pat.save()
       
        
class Receptionist(User):
          
    user_name = models.CharField(
        verbose_name = 'Nome', 
        max_length = 30,
        help_text = 'Insira seu nome completo. Ex.: João Santos Silva', 
        validators = [ validators.RegexValidator(re.compile(r''), 'Insira um nome válido', 'Inválido')]
    )
    
    cpf = models.CharField(
        verbose_name = 'CPF',
        primary_key = True,
        max_length = 30,
        unique = True,
        help_text = 'XXX.XXX.XXX-XX', 
        validators = [validators.RegexValidator(re.compile(r'^(?:[0-9]{3}[\.|-]){3}[0-9]{2}$'),
                                               'Insira um número válido', 'Inválido')]
    )
      
    is_psicologist = False
    
    is_patient = False
    
    is_superuser = False
    
    is_staff = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'user_name',
        'cpf'
    ]
    
    
    def __str__(self) -> str:
        return self.user_name, self.email
    
    class Meta:
        verbose_name = 'Recepcção'
        verbose_name_plural = 'Recepção'
        

class Medical_Record(models.Model):

    record = models.TextField(
        verbose_name='Relatório',
    )

    date_created = models.DateTimeField(
        verbose_name='Criado em: ',
        auto_now_add=True, 
        help_text='Data de criação da entrada no prontuário'
    )

    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
        

class Calendar(models.Model):
    
    cpf_user = models.ForeignKey(Patients, on_delete=models.CASCADE)
    
    duration = models.DurationField()
    
    data = models.DateField()
    
    class Meta:
        verbose_name = 'Calendário'
        verbose_name_plural = 'Calendários'
    
class Finance(models.Model):
    
    TRANSACTIONS_STATUS_CHOICES = (
        (TRANSACTIONS_STATUS.PAYED, "Processo finalizado: Pago."),
        (TRANSACTIONS_STATUS.IN_PAYMENT, "Boleto gerado e enviado para pagamento"),
        (TRANSACTIONS_STATUS.START_PROCESS, "Boleto a ser gerado"),
    )
    
    user_cpf = models.ForeignKey(Patients, on_delete=models.CASCADE)
    
    transactions_status = models.CharField(
        choices=TRANSACTIONS_STATUS_CHOICES,
        max_length=80,
        help_text="Como estão as Transações",
        verbose_name="Transações"
    )
    
    class Meta:
        verbose_name = 'Finança'
        verbose_name_plural = 'Finanças'