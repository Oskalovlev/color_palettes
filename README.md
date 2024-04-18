# color_palettes
REST API сервис для работы с палитрами цветов


<details><summary>Подготовка проекта к запуску</summary>

1. *Склонировать репозиторий и перейти в него*:

    ```sh
    git clone https://github.com/Oskalovlev/color_palettes.git
    ```
    ```sh
    cd color_palettes/
    ```

    * Создать в директории `infra/` файл `.env` командой:

        ```sh
        touch color_palettes/.env
        ```
        > Заполнить переменные по примеру файла `.env.example`
---
2. *Для работы с PostgreSQL*:

    * Создать в директории `infra/` файл `.env` командой:

        ```sh
        touch infra/.env
        ```
        > Заполнить переменные по примеру файла `.env.example`

</details>

<details><summary>Для запуска в Docker-контейнере использовать инструкцию</summary>

1. *Запустить сборку контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml stop
    ```
3. *Для удаления контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml down (-v опционально, удалит связи)
    ```
</details>

<details><summary>Для локального запуска использовать инструкцию</summary>

1. *Выполните миграции*:

    * Инициализируйте миграции (опционально)
        ```sh
        python color_palettes/manage.py migrate
        ```

    * Создайте миграции
        ```sh
        python color_palettes/manage.py makemigrations user
        ```
        ```sh
        python color_palettes/manage.py makemigrations palette
        ```

    * Примените миграции
        ```sh
        python color_palettes/manage.py migrate
        ```
---
2. *Создайте суперюзера*:

    ```sh
    python color_palettes/manage.py createsuperuser
    ```

    > Для примера, данные суперюзера:

        username: admin
        <!-- mail: admin@admin.ru -->
        password: admin
        password (again): admin

    > При входе логин вводить с большой буквы `Admin` (если не работает `admin`)

---

3. *Соберите статику*:
    ```sh
    python color_palettes/manage.py collectstatic --noinput
    ```
---
4. *Локальный запуск*:

    ```sh
    python color_palettes/manage.py runserver
    ```
</details>

### Автор
- Оскалов Лев (*Telegram*: [@oskalov](https://t.me/oskalov), **Github**: [Oskalovlev](https://github.com/Oskalovlev))