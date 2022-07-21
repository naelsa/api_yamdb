from rest_framework import serializers


class NotMeValidator:
    def __call__(self, new_user):
        if new_user.get('username') == 'me':
            raise serializers.ValidationError(
                "Имя не может быть 'me'")
        return new_user
