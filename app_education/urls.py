from django.urls import path
from app_education.apps import AppEducationConfig
from app_education.views import EducationListAPIView, EducationCreateAPIView, EducationRetrieveAPIView, \
    EducationUpdateAPIView, EducationDestroyAPIView

app_name = AppEducationConfig.name

urlpatterns = [
    path('', EducationListAPIView.as_view(), name='educations'),
    path('create/', EducationCreateAPIView.as_view(), name='education_create'),
    path('<int:pk>/', EducationRetrieveAPIView.as_view(), name='education'),
    path('update/<int:pk>/', EducationUpdateAPIView.as_view(), name='education_update'),
    path('delete/<int:pk>/', EducationDestroyAPIView.as_view(), name='education_delete'),
]
