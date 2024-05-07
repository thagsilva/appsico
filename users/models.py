from django.db import models
from django.core import validators, mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import re

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name = ('email'),
        unique = True
    )
    
    user_name = models.CharField(
        verbose_name = ('Nome'), 
        max_length = 30,
        help_text = ('Insira seu nome completo. Ex.: João Santos Silva'), 
        validators = [ validators.RegexValidator(re.compile(r''), ('Insira um nome válido'), ('Inválido'))]
    )
    
    cpf = models.CharField(
        verbose_name = ('CPF'),
        primary_key = True,
        max_length = 30,
        unique = True,
        help_text = ('XXX.XXX.XXX-XX'), 
        validators = [validators.RegexValidator(re.compile(r'^(?:[0-9]{3}[\.|-]){3}[0-9]{2}$'),
                                               ('Insira um número válido'), ('Inválido'))]
    )
    
    is_active = models.BooleanField(
        verbose_name = ('Ativo'), 
        default = True, 
        help_text = ('Denota se o usuário está ou não ativo. Possível desativar cammpo ao invés de deletar o usuário')
    )
    
    is_staff = models.BooleanField(
        verbose_name = ('Colaborador'), 
        default = False, 
        help_text = ('Denota se o usuário é ou não um Colaborador.')
    )

    is_trusty = models.BooleanField(
        verbose_name = ('Validado'),
        default = False,
        help_text = ('Denota se o usuário confirmou seu email'))
    
    is_psicologist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(
        verbose_name = ('Data de criação'),
        auto_now_add = True,
        help_text = ('Data de criação do usuário no banco de dados.')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'user_name']
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    def email_user(self, subject, message, from_email='thatha_guaru@hotmail.com'):
        mail.send_mail(subject, message, from_email, [self.email])
    
    class Meta:
        verbose_name = ('Usuário')
        verbose_name_plural = ('Usuários')
        

class Patients(models.Model):
    
    user = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    
    phonenumber = models.CharField(
        verbose_name=('Número de telefone'), 
        max_length=30,
        unique=True,
        help_text=('Ex.: (XX)XXXX-XXXX'), 
        validators=[validators.RegexValidator(re.compile(r'^\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}$'),
                                               ('Insira um número válido'), ('Inválido'))]
    )

    address = models.CharField(
        verbose_name=('Endereço'), 
        max_length=30,
        unique=True,
        help_text=('Ex.: Rua/Av. XXX, NºXX, Complemento (se houver) - Bairro, Cidade, Estado - CEP'),
    )
    
    class Meta:
        verbose_name = ('Paciente')
        verbose_name_plural = ('Pacientes')
        
    
class Doctors(models.Model):
    
    user = models.OneToOneField(
        CustomUser,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    
    crp = models.CharField(
        verbose_name=('CRP'),
        max_length=30,
        unique=True,
        help_text=('XX/XXXXXX'), 
        validators=[validators.RegexValidator(re.compile(r'^[0-9]{2}\/[0-9]{6}$'),
                                               ('Insira um número válido'), ('Inválido'))]
    )
    
    patients = models.ForeignKey(
        Patients,
        on_delete = models.CASCADE
    )
    
    class Meta:
        verbose_name = ('Psicólogo')
        verbose_name_plural = ('Psicólogos')
        