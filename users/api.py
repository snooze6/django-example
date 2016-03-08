from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserListAPI(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        users = User.objects.all()
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        return paginator.get_paginated_response(serializer_users)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    """
    Pk es la variable que me pasa la URL
    """

    def get(self, request, var):
        user = get_object_or_404(User, pk=var)

        serializer = UserSerializer(user)
        serializer_users = serializer.data
        return Response(serializer_users)

    def put(self, request, var):
        user = get_object_or_404(User, pk=var)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, var):
        user = get_object_or_404(User, pk=var)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)