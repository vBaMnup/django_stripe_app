# django_stripe_app
Django + Stripe API бэкенд с возможностью получения id сессии.

[Проверить работоспособность (сайт)](http://andrey77.pythonanywhere.com/item/1/)

Доступ в админку:
username: admin
password: admin

### Стек:

- Python 3.10
- Django 4.1.6
- Gunicorn
- Stripe

### Возможности:

- Просмотр информации о товаре
- Получение Stripe Session ID

## Как запустить:
### Docker-compose:

- На удаленном сервере создать папку приложения
- Скопировать файл docker-compose.yml
- Скопировать папки static и templates
- Скопировать папку nginx
- Создать .env файл:
```dotenv
DJANGO_SECRET_KEY='Ваш секретный ключ Django'
STRIPE_PUBLIC_KEY='Ваш публичный ключ Stripe'
STRIPE_SECRET_KEY='Ваш секретный ключ Stripe'
```
- Запустить проект: 
```commandline
docker-compose up -d --build
```
Проект будет доступен по адресу: http://{адрес сервера}/item/1 

### Автор
[Paskov Andrey](https://vk.com/andrey_paskov)