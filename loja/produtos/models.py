from django.db import models

# Create your models here.

class Especiaria(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    disponibilidade = models.BooleanField()
    descricao= models.TextField(blank=True, verbose_name="descrição")

    def __str__(self):
        return "{} - {} - {} - {}".format(self.nome, self.valor, self.disponibilidade, self.descricao)

class Quadro(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    disponibilidade = models.BooleanField()
    descricao= models.TextField(blank=True)
    autor = models.CharField(max_length=50)

    
    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.nome, self.valor, self.disponibilidade, self.descricao, self.autor)

class Artefato(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    disponibilidade = models.BooleanField()
    descricao= models.TextField(blank=True)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.nome, self.valor, self.disponibilidade, self.descricao, self.tipo)

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    disponibilidade = models.BooleanField()
    descricao= models.TextField(blank=True)
    isbn = models.CharField(max_length=50)    

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.nome, self.valor, self.disponibilidade, self.descricao, self.isbn)
