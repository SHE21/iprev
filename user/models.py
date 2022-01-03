
import uuid
import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
										PermissionsMixin

def image_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'

	return os.path.join('uploads/user_foto')


class UserManager(BaseUserManager):

	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('O Email é obrigatorio')

		email = self.normalize_email(email)
		user = self.model(email= email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, cpf, email, password):
		user = self.create_user(cpf, email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user



class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255)
	nome = models.CharField(max_length=255)
	genero = models.CharField('Genero', max_length=10)
	cpf = models.CharField('CPF', max_length=50, unique=True)
	rg = models.CharField('RG', max_length=50)
	cnh = models.CharField('CNH', max_length=50)
	pis_pasep = models.CharField('PIS/PASEP', max_length=100)
	dataNascimento = models.DateField('Data de Nascimento', blank=True, null=True)
	eleitorNumero = models.CharField('Número de eleitor', max_length=50)
	nomeMae = models.CharField('Nome da Mãe', max_length=100)
	nomePai = models.CharField('Nome do Pai', max_length=100)
	naturalidade = models.CharField('Naturalidade', max_length=100)
	cargo = models.CharField('Cargo', max_length=100)
	foto = models.ImageField(null=True, upload_to=image_file_path)
	is_active = models.BooleanField(default= True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'cpf'



class Endereco(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='endereco', on_delete=models.CASCADE)
	estado = models.CharField('Estado', max_length=100)
	cidade = models.CharField('Cidade', max_length=100)
	numero = models.CharField('Número', max_length=10)
	rua = models.CharField('Rua/Avenida', max_length=150)
	bairro = models.CharField('Bairro', max_length=80)
	complemento = models.CharField('Complemento', max_length=100)
	cep = models.CharField('CEP', max_length=15)

	class Meta:
		verbose_name = 'Endereço'



class Contato(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='contato', on_delete=models.CASCADE)
	telefone = models.CharField('Telefone', max_length=50)
	celular = models.CharField('Celular', max_length=50)

	class Meta:
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'

	def __str__(self):
		return self.celular



class Documento(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documento', on_delete=models.CASCADE)
	upload = models.FileField(upload_to='user_documentos', max_length=255)
	nome = models.CharField('Nome Documento', max_length=100)
	tipo = models.CharField('Categoria/Tipo', max_length=80)

	class Meta:
		verbose_name = 'Documento'
		verbose_name_plural = 'Documentos'

	def __str__(self):
		return self.nome


class Ingredient(models.Model):
	name = models.CharField('nome', max_length=255)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	def __srt__(self):
		return self.name

