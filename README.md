# simple-django-blog

REST API для системы комментариев блога.

## Порядок сборки и запуска проекта

1. Создаем виртуальное окружение Python
```
python -m venv .venv
.venv\scripts\activate
```

2. Устанавливаем зависимости из requirements.txt
```
pip install -r requirements.txt
```

3. Создаем в PostgreSQL базу данных, которая будет использоваться для проекта

4. Меняем настройки подключения к БД в settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simple_blog',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Создаем таблицы в БД
```
python manage.py makemigrations
python manage.py migrate
```

6. Если нужно будет пользоваться админкой, то создаем суперпользователя
```
python manage.py createsuperuser
```

7. Запускаем сервер Django
```
python manage.py runserver
```


Описание API:
```
swagger/
redoc/
```
Админка:
```
admin/
```
