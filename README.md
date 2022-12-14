# Todolist
## _Приложение "Календарь" для работы с задачами_

[![](https://www.python.org/static/community_logos/python-powered-w-140x56.png)](https://python.org)

### Функции
>* Создавайте доски для размещения ваших задач
>* Формируйте категории задач
>* Назначайте приоритеты и устанавливайте дедлайны
>* Совместно с коллегами создавайте, редактируйте и комментируйте задачи
>* Завершенные задачи отправляйте в архив
>* Авторизуйтесь в приложении с помощью вашего аккаунта ВК 
>* Используйте телеграм-бот для удобного просмотра и создания новых задач

### Cтек технологий

- [Python 3.8.10](https://python.org)
- [Django 4.0.1](https://www.djangoproject.com/)
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/)
- [Postgres 14.5](https://www.postgresql.org/)
- [Docker 20.10.17](https://www.docker.com/)


### Установка
* Скачайте исходники c GitHub
* Заполните файл `.env` в соответствии с шаблоном `.env.example`
* Запустите `docker-compose up -d`
* Создайте приложение в ВК
* Полученный при регистрации `ID` присвойте константе SOCIAL_AUTH_VK_OAUTH2_KEY, а защищённый ключ константе SOCIAL_AUTH_VK_OAUTH2_SECRET в файле `.env` 
* Создайте бота в Telegram
* Полученный при создании бота токен присвойте константе TELEGRAM_BOT_TOKEN в файле `.env` 
* Если приложение развернуто на локальной машине наберите в адресной строке браузера `http://localhost`, если на сервере адрес данного сервера в сети интернет
* При первом использовании бота Telegram, вы получите код верификации, который необходимо ввести в разделе **Верифицировать бота** WEB-приложения   

### Где скачать:
[GitHub](https://github.com/Vikver74/course_work7.git)

### Сайт
[vikver74.ga](http://vikver74.ga)

### Разработчик:

_Виктор Веревкин_

### Лицезия

Free Software