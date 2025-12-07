from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Userlist
from .serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    user = Userlist.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_details(request,pk):
    user = Userlist.objects.get(pk=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request,pk):
    user = Userlist.objects.get(pk=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request,pk):
    user = Userlist.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)