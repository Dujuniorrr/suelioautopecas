from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nome")
    cpf = models.CharField( max_length=14, verbose_name="CPF")
    phone = models.CharField( max_length=14,  verbose_name="Telefone")
    address = models.CharField(max_length=100, verbose_name="Endereço")

    def __str__(self):
        return self.name