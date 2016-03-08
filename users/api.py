from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.renderers import JSONRenderer

from users.serializers import UserSerializer


class UserListAPI(View):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data
        renderer = JSONRenderer()
        json_users = renderer.render(serializer_users)
        return HttpResponse(json_users)