from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        fields = '__all__',
        exclude = ('confirmation_code',)
        model = User


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации."""

    email = serializers.EmailField(required=True)

    class Meta:
        fields = ('email', 'username')
        model = User

    def validate(self, data):
        """Проверка, что имя 'Me' запрещено."""
        if data.get('username') == 'me':
            raise serializers.ValidationError("Имя не может быть 'me'")
        return data


class RegTokSerializer(serializers.ModelSerializer):
    """Сериализатор токена."""

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=254)
    