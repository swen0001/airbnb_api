from rest_framework import serializers
from .models import User


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id',
                   'email',
                   'groups',
                   'user_permissions',
                   'password',
                   'last_login',
                   'is_superuser',
                   'is_staff',
                   'is_active',
                   'date_joined',
                   'favs',)


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups',
                   'user_permissions',
                   'password',
                   'last_login',
                   'is_superuser',
                   'is_staff',
                   'is_active',
                   'favs',
                   'date_joined',)


class WriteUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def validated_first_name(self, value):
        return value.upper()
