## Макет онлайн магазина

---

Команды для запуска:

1. Зависимости:
`pip install -r requirements.txt`
2. Запуск сервера:
`python manage.py runserver` 
3. Запуск брокера (команда необходима для работы на windows, [инструкция здесь](https://redis.io/docs/getting-started/installation/install-redis-on-windows/)): `sudo service redis-server start` 
4. Наполение БД с помощью фикстур: `python manage.py loaddata catalog_data.json`

---

> Скрытые переменные, необходимые для работы проекта:
>
>DEBUG=
>***
>SECRET_KEY=
>***
>POSTGRESQL_PASSWORD=
>***
>EMAIL_HOST_USER=
> 
>EMAIL_HOST_PASSWORD=
>***
>create_sup_user:
>
>ADMIN_EMAIL=
> 
>ADMIN_PASSWORD=
>***
>REDIS_HOST=