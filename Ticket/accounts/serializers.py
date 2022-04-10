from rest_framework.serializers import ModelSerializer

from accounts.models import User


class SignupUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
