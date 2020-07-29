from app.models import Todo
from app.serializers import TodoSerializer
from rest_framework import generics


class TodoListAndCreate(generics.ListCreateAPIView):  # Classe já imprementa todos os metodos automaticamente.
   queryset = Todo.objects.all()  # Filtro banco de dados
   serializer_class = TodoSerializer


class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()  # Filtro banco de dados
    serializer_class = TodoSerializer