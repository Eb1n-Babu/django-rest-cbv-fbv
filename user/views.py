from rest_framework import viewsets
from .models import Userlist
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Userlist.objects.all()
    serializer_class = UserSerializer
