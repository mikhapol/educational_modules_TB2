from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_education.models import Education
from users.models import User


class EducationTestCase(APITestCase):
    """Тестирование образовательного модуля"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""

        # Создание пользователя для тестирования
        self.user = User.objects.create(email='test@test.ru',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)

        self.user.set_password('qwerty')  # Устанавливаем пароль
        self.user.save()  # Сохраняем изменения пользователя в базе данных

        # Создание привычки для тестирования
        self.education = Education.objects.create(
            user=self.user,
            serial=1,
            title="Простое обучение",
            desc="Тест обучения",
        )

        # Запрос токена для авторизации
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'qwerty'})

        self.access_token = response.data.get('access')  # Токен для авторизации

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Авторизация пользователя

    def test_create_education(self):
        """Тестирование создания образовательного модуля"""

        # Данные для создания образовательного модуля
        data = {
            "user": 1,
            "serial": 2,
            "title": "Тест",
            "desc": "Test",
        }

        response = self.client.post(reverse('app_education:education_create'), data=data)  # Отправка запроса

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        self.assertEqual(Education.objects.all().count(), 2)  # Проверка наличия в базе данных новой записи

    def test_list_education(self):
        """Тестирование списка просмотра образовательных модулей"""

        response = self.client.get(
            reverse('app_education:educations'))  # Запрос на получение списка образовательных модулей

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(), [{
            "user": 1,
            "serial": 1,
            "title": "Простое обучение",
            "desc": "Тест обучения",
        }])

    def test_update_education(self):
        """Тестирование редактирования образовательного модуля"""

        # Данные для обновления образовательного модуля
        data = {
            "user": 1,
            "serial": 1,
            "title": "Простое",
            "desc": "Тест",
        }

        # Запрос на обновление образовательного модуля
        response = self.client.put(reverse('app_education:education_update', args=[self.education.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "user": 1,
                             "serial": 1,
                             "title": "Простое",
                             "desc": "Тест",
                         })

    def test_get_education_by_id(self):
        """Тестирование получения образовательного модуля по id"""

        # Запрос на получение образовательного модуля по id
        response = self.client.get(reverse('app_education:education', args=[self.education.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "user": 1,
                             "serial": 1,
                             "title": "Простое обучение",
                             "desc": "Тест обучения",
                         })

    def test_destroy_education(self):
        """Тестирование удаления образовательного модуля"""

        # Запрос на удаление образовательного модуля
        response = self.client.delete(reverse('app_education:education_delete', args=[self.education.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        self.assertEqual(Education.objects.all().count(), 0)  # Проверка количества записей образовательных модулей в БД
