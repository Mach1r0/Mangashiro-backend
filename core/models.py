from django.db import models
from django.contrib.auth.models import User 

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao
    
class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()    

    def __str__(self):
        return self.nome

class Autor(models.Model):
    class Meta: 
        verbose_name_plural = "Autores"
    nome = models.CharField(max_length=255)

    def __str__(self): 
        return self.nome
    
class Livro(models.Model):
    titulo =  models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livro")
    editora  = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livro")    
    autores = models.ManyToManyField(Autor, related_name="Livros")
    
    def __str__(self) -> str:
        return "%s (%s)" %(self.titulo, self.editora)

class Compra(models.Model):    
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        Realizado = 2, "Realizado"
        Pago = 3, "Pago"
        Entregue = 4, "Entregue"
        
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField
