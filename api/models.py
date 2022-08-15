from django.db import models
from django.forms import DateField
from rest_framework.exceptions import ValidationError

def receita_filtro_descricao(descricao):
    return Receita.objects.filter(descricao = descricao).exists()


class Receita(models.Model):
    '''Cria as models de receita'''
    descricao = models.CharField (max_length= 100)
    valor = models.FloatField()
    data = models.DateField()
    
    def save(self, *args, **kwargs):
        if Receita.objects.filter(descricao__icontains=self.descricao, data__month=self.data.month, data__year=self.data.year):
            raise ValidationError(f"A receita {self.descricao} já existe nesse mês") 
        else:
            super().save(*args, **kwargs)


def despesa_filtro_descricao(descricao):
    return Despesa.objects.filter(descricao=descricao).exists()


class Despesa(models.Model):
    '''Cria as models de despesa'''
    CATEGORIAS = (
        ('Alimentação', 'Alimentação'),
        ('Saúde','Saúde'),
        ('Moradia', 'Moradia'),
        ('Transporte', 'Transporte'),
        ('Educação', 'Educação'),
        ('Lazer', 'Lazer'),
        ('Imprevistos', 'Imprevistos'),
        ('Outras', 'Outras')
    )
    
    descricao = models.CharField(max_length= 100)
    valor = models.FloatField()
    data = models.DateField()
    categoria = models.CharField(choices = CATEGORIAS, default = 'Outras', blank = False, null = False, max_length = 15)

    def save(self, *args, **kwargs):
        if Despesa.objects.filter(descricao__icontains=self.descricao, data__month=self.data.month, data__year=self.data.year, categoria = self.categoria):
            raise ValidationError(f"A despesa {self.descricao} já existe nesse mês") 
        else:
            super().save(*args, **kwargs)
    
   


    

