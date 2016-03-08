from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de user a partir de Validated_data que
        contienen valores deserializados
        :param validated_data:
        :return:
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        #instance.password = validated_data.get('password')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        """
        Valida si existe un usuario con ese username
        :param data:
        :return:
        """
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError('[Creando] Ya existe un usuario con ese username')
        elif self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError('[Modificando] Ya existe un usuario con ese username')
        else:
            return data
