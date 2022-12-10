# url_short_service_drf

# Сервис по сокращению ссылок

Задача: 
Сокращать длинные URL до коротких без потери ее ценности. Это дает лучшую читаемость ссылки для пользователя.

Основные требования к сервису:

- Сервис должен превращать указанную ссылку в короткую, не обрезая при этом ее параметры;
- Короткая ссылка должна гарантированно перенаправлять пользователя на внешний url в течении указанного пользователем срока жизни. В диапазоне от 1 дня до 1 года. По умолчанию 90 дней;
- Ссылка должна быть как можно короче, при этом сохраняя ее уникальность в рамках миллиона одновременно хранимых ссылок. Каждый день может добавляться случайное количество ссылок, каждая из которых может иметь свой срок жизни;
- У сервиса должен быть API интерфейс для взаимодействия с программами.
## Стэк:
Django/Django REST Framework
Python 

## Установка 

-Клонировать репозиторий

```bash
git clone https://github.com/ruslan-kornich/url_short_service_drf.git
```

Создать и активировать виртуально окружение:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Установить зависимости:

```bash
$ pip install -r requirements.txt
```

Запустить сервер:

```bash
$ python3 manage.py runserver
```
## Запуск крон



```bash
$ python manage.py crontab add
```
запустит задачу которая раз в час будет проверять и удалять ссылки из БД дата которых подходит к концу  


Доступ к админ панели по ссылке   
admin/

пароль/логин   admin/admin


## API:
Поддержка запросов GET, POST, PUT, DELETE для взаимодействия с приложениями
## Предполагаемая структура данных

```jsx
// short_url - ссылки хранятся в БД
{
	id: 
	link: String
	short_link: String
	time_create: DateTime
        end_time: DateTime
}
```

### Описание работы API
### GET /api/v1/urls/
```jsx
// Ответ
{
    "short_url": [
        {
            "id": 1,
            "link": "https://pypi.org/project/django-crontab/",
            "short_link": "H4s4d3",
            "time_create": "2022-11-04T16:15:53.842856",
            "end_time": "2022-11-05T16:15:53.841007"
        },
        {
            "id": 2,
            "link": "https://docs.python.org/3/tutorial/index.html",
            "short_link": "v8E2R8",
            "time_create": "2022-11-04T16:16:30.710958",
            "end_time": "2023-11-04T16:16:30.709688"
        },
	],
}
```
### POST /api/v1/urls/
```jsx
// Тело запроса
{
    "link" : "https://docs.djangoproject.com/en/4.1/topics/auth/passwords/",
    "end_time" : "2023-03-08T11:58:38.000315"
}
// Ответ
{
    "pk": 80,
    "link": "https://docs.djangoproject.com/en/4.1/topics/auth/passwords/",
    "short_link": "r7Q0W8",
    "time_create": "2022-12-10T17:42:34.045765",
    "end_time": "2023-03-08T11:58:38.000315"
}

```
### PUT /api/v1/urls/{id}
```jsx
// Тело запроса

{
    "link": "https://docs.djangoproject.com/en/4.1/topics/auth/passwords/tests",
    "end_time": "2024-03-08T11:58:38.000315"
}
// Ответ
{
    "pk": 80,
    "link": "https://docs.djangoproject.com/en/4.1/topics/auth/passwords/tests",
    "short_link": "r7Q0W8",
    "time_create": "2022-12-10T17:42:34.045765",
    "end_time": "2023-03-08T11:58:38.000315"
}
```
### DELETE /api/v1/urls/{id}
```jsx

// Ответ
"Link r7Q0W8 removed"
```

