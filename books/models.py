from ast import AugStore
from platform import release
from pyexpat import model
from uuid import uuid4
from django.db import models
from uuid import uuid4

# id do livro,autor, release year,

class Books(models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False) #chave primaria, não editavel
    titulo = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    release_year = models.IntegerField()
    state = models.CharField(max_length=56)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=256)
    create_at = models.DateField(auto_now_add=True) #criação automatica 