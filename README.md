# api_final

## Описание. Что это за проект, какую задачу он решает, в чём его польза

Проект бэкенда на django с использованием DRF для API сервиса yatube, в котором есть возможность
отправлять, получать, создавать, изменять публикации, комментарии.
Можно создавать и получать подписки, получать группы.
Аутентификация производится с помощью JWT+djoser.

## Установка. Как развернуть проект на локальной машине

1. Клонируем репозиторий:

    ```bash
    git clone git@github.com:lanarkk/api_final_yatube.git
    ```

2. Развертываем виртуальное окружение:

    ```bash
    python3 -m venv env
    ```

3. Устанавливаем в venv:

    * Если у вас Linux/macOS

    ```bash
    source env/bin/activate
    ```

    * Если у вас windows

    ```bash
    source env/scripts/activate
    ```

4. Установить зависимости из файла requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

    ```bash
    python3 -m pip install --upgrade pip
    ```

5. Выполнить миграции:

    ```bash
    python3 manage.py migrate
    ```

6. Запустить проект:

    ```bash
    python3 manage.py runserver
    ```

## Примеры. Некоторые примеры запросов к API

### Получение публикаций

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

GET <http://127.0.0.1:8000/api/v1/posts/>

'''application/json
{
  "count": 123,
  "next": "<http://api.example.org/accounts/?offset=400&limit=100>",
  "previous": "<http://api.example.org/accounts/?offset=200&limit=100>",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
'''

### Получение комментариев

Получение всех комментариев к публикации.

GET <http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/>

'''application/json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
'''

### Подписка

Подписка пользователя от имени которого сделан запрос на пользователя
переданного в теле запроса. Анонимные запросы запрещены.

POST <http://127.0.0.1:8000/api/v1/follow/>

'''application/json
{
  "following": "string"
}
'''

Автор Максим федякин
GitHub <https://github.com/lanarkk>
