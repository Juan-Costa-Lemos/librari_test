from books.models import Books
from rest_framework import viewsets
from books.api.serializers import BooksSerializers
from books.models import Books


class BooksViewsets(viewsets.ModelViewSet):
    serializer_class = BooksSerializers
    queryset = Books.objects.all() #precisa receber todas as instancias,  e queremos todos os objetos. Tambem poderia puxar só com uma primary_key
