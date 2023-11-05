from rest_framework import generics
from app_education.models import Education
from app_education.serializers import EducationSerializer


class EducationListAPIView(generics.ListAPIView):
    """View для получения списка образовательных модулей"""
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class EducationCreateAPIView(generics.CreateAPIView):
    """View для создания образовательного модуля"""
    serializer_class = EducationSerializer


class EducationRetrieveAPIView(generics.RetrieveAPIView):
    """View для просмотра образовательного модуля по идентификатору"""
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class EducationUpdateAPIView(generics.UpdateAPIView):
    """View для редактирования образовательного модуля по идентификатору"""
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class EducationDestroyAPIView(generics.DestroyAPIView):
    """View для удаления образовательного модуля по идентификатору"""
    queryset = Education.objects.all()
