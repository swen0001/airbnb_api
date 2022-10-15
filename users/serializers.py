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


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'superhost',
            'password',
        )
        read_only_fields = ('id', 'superhost', 'avatar',)

    def validated_first_name(self, value):
        return value.upper()

    def create(self, validated_data):
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

