from django.db import models
from django.forms import DateField

def receita_filtro_descricao(descricao):
    return Receita.objects.filter(descricao = descricao).exists()


class Receita(models.Model):
    '''Cria as models de receita'''
    descricao = models.CharField (max_length= 100)
    valor = models.FloatField()
    data = models.DateField()
    
    def save(self, *args, **kwargs):
        if Receita.objects.filter(descricao=self.descricao, data=self.data):
            raise ValueError("Registro Duplicado !")
        
        elif not receita_filtro_descricao(self.descricao):  # Cria/atualiza um registro
            super().save(*args, **kwargs)
        
        elif Receita.objects.filter(data__month=self.data.month,
                                    data__year=self.data.year).exists() and not receita_filtro_descricao(
            self.descricao):   # Cria/atualiza um registro
            super().save(*args, **kwargs)
            super().save(*args, **kwargs)
        
        elif receita_filtro_descricao(self.descricao) and not Receita.objects.filter(
                descricao=self.descricao, data__month=self.data.month, data__year=self.data.year).exists():
            # Atualiza a data do registro
            super().save(*args, **kwargs)
        else:
            raise ValueError("Erro no Registro !")


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
        if Despesa.objects.filter(descricao=self.descricao, data=self.data):
            raise ValueError("Registro Duplicado !")
        
        elif not despesa_filtro_descricao(self.descricao):   # Cria/atualiza um registro
            super().save(*args, **kwargs)
        
        elif Despesa.objects.filter(data__month=self.data.month,
                                    data__year=self.data.year).exists() and not despesa_filtro_descricao(
            self.descricao):   # Cria/atualiza um registro
            super().save(*args, **kwargs)

        elif despesa_filtro_descricao(self.descricao) and not Despesa.objects.filter(
                descricao=self.descricao, data__month=self.data.month, data__year=self.data.year).exists():
            # Atualiza a data do registro
            super().save(*args, **kwargs)
        else:
            raise ValueError("Erro no Registro !")


class Resumo(models.Model):
    receita_total = models.FloatField()
    despesa_total = models.FloatField()
    saldo = models.FloatField()
    gasto_categoria = models.TextField()
    

