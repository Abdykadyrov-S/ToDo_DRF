from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import User, UserRegisterSerializer, UserSerializers

# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        return UserRegisterSerializer
        
    