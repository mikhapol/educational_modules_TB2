from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UsersTestCase(APITestCase):
    """Тестирование пользователей"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""

        # Создание пользователя для тестирования
        self.user = User.objects.create(email='test@test.ru',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)

        self.user.set_password('qwerty')  # Устанавливаем пароль
        self.user.save()  # Сохраняем изменения пользователя в базе данных

        # Запрос токена для авторизации
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'qwerty'})

        self.access_token = response.data.get('access')  # Токен для авторизации

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Авторизация пользователя

    def test_create_users(self):
        """Тестирование создания пользователя"""

        # Данные для создания пользователя
        data = {
            "email": 'tests@test.ru',
            "first_name": "Тест",
            "last_name": "Тестов",
            "password": "Test",
        }

        response = self.client.post('/users/user/', data=data)  # Отправка запроса

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        self.assertEqual(User.objects.all().count(), 2)  # Проверка наличия в базе данных новой записи

    def test_list_users(self):
        """Тестирование списка просмотра пользователей"""

        response = self.client.get('/users/user/')  # Запрос на получение списка пользователей

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(), [{
            "email": 'test@test.ru',
            "first_name": "",
            "last_name": "",
            "phone": None,
            "city": None,
        }])

    def test_update_user(self):
        """Тестирование редактирования пользователя"""

        # Данные для обновления пользователя
        data = {
            "email": 'test@test.ru',
            "first_name": "first_name",
            "last_name": "last_name",
            "phone": "phone",
            "city": "city",
        }

        # Запрос на обновление пользователя
        response = self.client.put('/users/user/1/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "email": 'test@test.ru',
                             "first_name": "first_name",
                             "last_name": "last_name",
                             "phone": "phone",
                             "city": "city",
                         })

    def test_get_user_by_id(self):
        """Тестирование получения пользователя по id"""

        # Запрос на получение пользователя по id
        response = self.client.get('/users/user/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "email": 'test@test.ru',
                             "first_name": "",
                             "last_name": "",
                             "phone": None,
                             "city": None,
                         })

    def test_destroy_user(self):
        """Тестирование удаления пользователя"""

        # Запрос на удаление пользователя
        response = self.client.delete('/users/user/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        self.assertEqual(User.objects.all().count(), 0)  # Проверка количества записей пользователей в БД
