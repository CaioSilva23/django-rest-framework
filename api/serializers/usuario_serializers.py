from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super(UsuarioSerizalizer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user