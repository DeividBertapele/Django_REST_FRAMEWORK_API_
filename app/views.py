from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


class TodoViewsSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    





    
#TODO: É opcional

#from rest_framework import generics
# from rest_framework.views import APIView


# class TodoListAndCreate(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
    
# class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
    
