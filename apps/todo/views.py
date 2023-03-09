from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters
from .permissions import TodoPermissions
from .serializers import TodoSErializer, Todo
from rest_framework.response import Response
# Create your views here.

class TodoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSErializer
    permission_classes = (TodoPermissions, )

    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'descriptions')

class TodoALLDEL(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSErializer
    permission_classes = (TodoPermissions, )

    def delete(self,request, *args, **kwargs):
        todo = Todo.objects.filter(user = request.user)
        todo = [i for i in todo.delete()]

        return Response({"delete": "Все таски удалены"})