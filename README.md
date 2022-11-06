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
"short_url": [
    	{
            "link": "https://docs.python.org/3/tutorial/index.html", 
            "end_time": "2022-11-05T11:51:45"
        
        
		}
  	]
}
// Ответ
{
    "success":"Url y3L9o3 created successfully"
}

```
### PUT /api/v1/urls/
```jsx
// Тело запроса

{
"short_url":[
    {
		"link": "https://www.django-rest-framework.org/api-guide/fields/",
      	"short_link": "u4n9L1",
        "end_time": "2022-11-05T11:51:45"
	}
  ]
}
// Ответ
{
    "success":"Url 'u4n9L1' updated successfully"
}
```
### DELETE /api/v1/urls/
```jsx
// Тело запроса
{
"short_url":[
    {
      	"short_link": "y3L9o3"
	}
  ]
}
// Ответ
{
    "success": "Url https://docs.python.org/3/tutorial/index.html delete"
}
```

