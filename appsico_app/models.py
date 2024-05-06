from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators, mail
from django.conf import settings
from django.utils import timezone
import re

class UserManager(BaseUserManager):
    
    use_in_migrations = True
    
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        
        if not username:
            raise ValueError('O campo "Nome" é obrigatório')
        
        if not extra_fields['cpf']:
            raise ValueError('O campo "CPF" é obrigatório')
        
        if not extra_fields['phonenumber']:
            raise ValueError('O campo "Telefone" é obrigatório')
        
        email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=False, is_superuser=False, **extra_fields)
    
    def create_staff(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=True, is_superuser=False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user

class BaseUser(AbstractBaseUser, PermissionsMixin):
    
    user_name = models.CharField(
        verbose_name=('Nome'), 
        max_length=30,
        help_text=('Insira seu nome completo. Ex.: João Santos Silva'), 
        validators=[ validators.RegexValidator(re.compile(r''), ('Insira um nome válido'), ('Inválido'))]
    )
    
    cpf = models.CharField(
        verbose_name=('CPF'),
        primary_key=True,
        max_length=30,
        unique=True,
        help_text=('XXX.XXX.XXX-XX'), 
        validators=[validators.RegexValidator(re.compile(r'^(?:[0-9]{3}[\.|-]){3}[0-9]{2}$'),
                                               ('Insira um número válido'), ('Inválido'))]
    )
    
    USERNAME_FIELD = 'cpf'
    
class Patients(BaseUser):
     
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
    
    email = models.EmailField(('Email'), max_length=255, unique=True)
          
    is_active = models.BooleanField(
        verbose_name=('ativo'), 
        default=True, 
        help_text=('Denota se o usuário está ou não ativo. Possível desativar cammpo ao invés de deletar o usuário')
    )
    
    is_trusty = models.BooleanField(
        ('Validado'), default=False, help_text=('Denota se o usuário confirmou seu email'))
    
    USERNAME_FIELD = 'email' #fazer login com email
    REQUIRED_FIELDS = ['user_name', 'cpf', 'phonenumber']
    
    class Meta:
        verbose_name = ('Paciente')
        verbose_name_plural = ('Pacientes')
           
    def email_user(self, subject, message, from_email='thatha_guaru@hotmail.com'):
        mail.send_mail(subject, message, from_email, [self.email])
        

class Doctors(BaseUser):
          
    crp = models.CharField(
        verbose_name=('CRP'),
        max_length=30,
        unique=True,
        help_text=('XX/XXXXXX'), 
        validators=[validators.RegexValidator(re.compile(r'^[0-9]{2}\/[0-9]{6}$'),
                                               ('Insira um número válido'), ('Inválido'))]
    )
    
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ('Psicólogo')
        verbose_name_plural = ('Psicólogos')
    
    if BaseUser.user_name:
        name = re.findall(r'[A-Z]+', str(BaseUser.user_name))
        
        if len(name) == 2:
            username = f"""Cs#
                            {name[1]}{name[0]}
                        2024"""
        elif len(name) >= 3:
            username = f"""Cs#
                            {name[2]}{name[0]}{name[1]}
                        2024"""
        elif len(name) == 1:
            raise ValueError('É necessário ao menos um Nome e um Sobrenome!')
               
    USERNAME_FIELD = username
        
    REQUIRED_FIELDS = ['user_name', 'cpf', 'crp', 'patient']

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

