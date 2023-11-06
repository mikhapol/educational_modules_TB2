from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация для модели Пользователь"""

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'city')
