from rest_framework import serializers

from app_education.models import Education


class EducationSerializer(serializers.ModelSerializer):
    """Сериализация для модели образовательного модуля"""

    class Meta:
        model = Education
        fields = '__all__'
