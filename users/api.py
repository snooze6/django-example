from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        return Response(serializer_users)

class UserDetailAPI(APIView):

    """
    Pk es la variable que me pasa la URL
    """
    def get(self, request, var):
        user = get_object_or_404(User, pk=var)

        serializer = UserSerializer(user)
        serializer_users = serializer.data
        return Response(serializer_users)