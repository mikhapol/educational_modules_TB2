# Образовательные модули "ТВ2"

>Краткое описание: Django-приложение “Образовательные модули” 	без доп функций.
Направление: Backend  
Тэги: FBV/CBV, Git, MVT/MTV, ORM,PEP8, PostgreSQL, Readme, Serialiers, Swagger, Tests, Viewset/Generic

FBV/CBV - При реализации контроллеров в Django можно использовать CBV или FBV  
Git - Использовать для хранения исходного кода один из удаленных Git репозиториев  
MVT/MTV - Задача должна быть реализована согласно паттерну MVC/MTV  
ORM - Использование специальной библиотеки для работы с СУБД, без написания SQL запросов вручную  
PEP8 - Следовать рекомендациям PEP8  
PostgreSQL - Использовать СУБД PostrgeSQL для хранения и обработки данных в реализованном проекте  
Readme - Описать документацию в файле Readme в корне проекта  
Serialiers - Для реализации обработки данных проектом, использовать библиотеки сериализаторов  
Swagger - Для API серверов реализовать доступ к автогенерируемой документации  
Tests - Написать тесты на реализованный функционал  
Viewset/Generic - При работе над API серверами, на основе DRF, использовать специальные базовые классы для создания контроллеров  


## Описание

Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:

- порядковый номер (app_education/models.py:10)
- название (app_education/models.py:11)
- описание (app_education/models.py:12)

## Задача

<aside>
👾 При создании проекта нужно:

1. Реализовать для модели (моделей) все методы CRUD:  
    app_education.views.EducationListAPIView - Просмотр всех  
    app_education.views.EducationCreateAPIView - Создание  
    app_education.views.EducationRetrieveAPIView - Просмотр по ID  
    app_education.views.EducationUpdateAPIView - Редактирование  
    app_education.views.EducationDestroyAPIView - Удаление  

    
2. Полностью покрыть автоматизированными юнит-тестами все модели, сериализаторы, виды.  
    app_education.tests.EducationTestCase - Тестирование образовательного модуля  
    users.tests.UsersTestCase - Тестирование пользователей


</aside>

## Требуемый стэк

- python 3.11 - ОК
- Docker - ОК
- Django - ОК

### Условия приемки

- код размещен в открытом репозитории - Да
- доступна документация - Да
- код покрыт автоматизированными юнит-тестами - Да
- код оформлен согласно pep8 - Да
- оформлен Readme файл - Да
- в проекте использован Docker - Да

>docker compose build - Сборка проекта  
docker compose up - Запуск проекта

Дополнительные команды:  
- sudo systemctl start docker - запуск докера из терминала  
- sudo systemctl status docker - проверка статуса запуска докера  
- docker images - выводит список созданных образов  
- docker rmi -f $(docker images -aq) - удаление всех созданных образов  
- docker ps -а - Посмотреть все контейнеры  

Для запуска проекта локально, необходимо перейти в браузер по ссылке:  
http://localhost:8001  
Так как в [docker-compose.yml](docker-compose.yml) прописан порт 8001 (32 строчка).

>#### Расшифровка тегов:
**PostgreSQL** - Использовать СУБД PostrgeSQL для хранения и обработки данных в реализованном проекте  
**ORM** - Использование специальной библиотеки для работы с СУБД, без написания SQL запросов вручную  
**Serialiers** - Для реализации обработки данных проектом, использовать библиотеки сериализаторов  
**Viewset/Generic** - При работе над API серверами, на основе DRF, использовать специальные базовые классы для создания контроллеров  
**Filter** - Использовать библиотеку django-filter или ее встроенный аналог в DRF  
**CORS** - Настроить работу с доверенными доменными именами или IP адресами  
**Tests** - Написать тесты на реализованный функционал  
**Git** - Использовать для хранения исходного кода один из удаленных Git репозиториев  
**Readme** - Описать документацию в файле Readme в корне проекта  
**PEP8** - Следовать рекомендациям PEP8  
**Swagger** - Для API серверов реализовать доступ к автогенерируемой документации  
**Django** - Использовать для реализации фреймворк Django  
**DRF** - Использовать для реализации библиотеку DRF  
**Docker** - Весь проект оформить для запуска в Docker  
**Docker-Compose** - Весь проект оформить для запуска в Docker-compose  
**MongoDB** - Использовать СУБД MongoDB для хранения и обработки данных в реализованном проекте  
**JSON** - Входные или выходные данные должны быть оформлены в JSON строку/файл  
**FastAPI** - Использовать для реализации фреймворк FastAPI  
**Сторонние** - API	Решение подразумевает интеграцию с удаленными API сервисами  
**OOP** - Для реализации задачи должен быть использован ООП подход  
**Tortoise** - В качестве ORM необходимо использовать Tortoise ORM  
**SQL Alchemy** - В качестве ORM необходимо использовать SQL Alchemy ORM  
**Telegram** - Подразумевается интеграция с Telegram  
**Algorithms** - При решении задания необходимо обращать внимание на оптимальность решения  
**CBV** - При реализации контроллеров в Django использовать CBV  
**Forms** - При реализации интерфейсов заполнения или редактирования данных в Django использовать формы  
**Templates** - При решении задачи реализовать работу с построением шаблонов и шаблонизаторами  
**Permissions** - При реализации задачи важно обратить внимание на разделение прав доступа и введенные роли  
**Auth** - Добавить функционал авторизации  
**Gist** - Реализованное решение должно быть размещено в gist.github.com  
**Parser** - Задание направлено на работу с парсингом данных  
**Regex** - При решении задачи необходимо использовать регулярные выражения  
**Права** - доступа	При реализации задачи важно обратить внимание на разделение прав доступа и введенные роли  
**MVT/MTV** - Задача должна быть реализована согласно паттерну MVC/MTV  
**FBV/CBV** - При реализации контроллеров в Django можно использовать CBV или FBV  
**CSV** - Входные или выходные данные должны быть оформлены в CSV файл  