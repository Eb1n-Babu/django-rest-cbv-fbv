from rest_framework import serializers
from .models import Userlist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlist
        fields = "__all__"