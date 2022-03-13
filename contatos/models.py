from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nte = models.CharField(max_length=6)
    nome = models.CharField(max_length=255)
    gestor = models.CharField(max_length=255)
    telefoneprinc = models.CharField(max_length=255)
    telefonesecun = models.CharField(max_length=255, blank=True)
    emailprinc = models.CharField(max_length=255)
    emailsecun = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    observacao = models.CharField(max_length=500, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nte