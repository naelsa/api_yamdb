from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api_yamdb import settings
from api_yamdb.settings import MAX_LENGTH_CONFIRMATION_CODE
from .validators import NotMeValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        fields = (
            'username', 'email', 'bio', 'first_name', 'last_name', 'role',
        )
        model = User


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации."""
    username = serializers.CharField(
        validators=(UniqueValidator(queryset=User.objects.all()),),
        required=True
    )
    email = serializers.EmailField(
        validators=(UniqueValidator(queryset=User.objects.all()),),
        required=True
    )

    class Meta:
        fields = ('email', 'username')
        model = User
        validators = [NotMeValidator(), ]


class RegTokSerializer(serializers.Serializer):
    """Сериализатор токена."""
    username = serializers.CharField(max_length=settings.MAX_LENGTH_USER,
                                     required=True)
    confirmation_code = serializers.CharField(
        max_length=MAX_LENGTH_CONFIRMATION_CODE,
        required=True)
