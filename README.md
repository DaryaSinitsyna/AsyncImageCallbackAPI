# Асинхронное Callback API

## Описание

Цель проекта - создать асинхронное API, которое принимает текстовый запрос и callback URL. Оно аутентифицирует запрос с помощью API-ключа и возвращает одно из предварительно выбранных изображений, закодированных в формате base64. Выбор изображения основывается на релевантности тегов, связанных с изображениями, по отношению к запросу. Чем больше тегов изображения соответствуют словам из запроса и чем выше значения этих тегов, отражающие уверенность модели в применимости тега, тем более релевантным считается изображение. Изображение с наибольшей суммированной релевантностью тегов выбирается для отправки пользователю.


## Возможности

1. **Эндпоинт загрузки изображений**: Позволяет загружать изображения и сохранять их данные в базе данных.
2. **Генерация тегов**: Генерирует теги для каждого загруженного изображения с помощью предварительно обученной модели из API Clarifai.
3. **Обработка текстового запроса**: Использует предобученную модель spaCy для извлечения леммы (основной формы слова) из текста, игнорируя морфологические изменения. Эта операция не учитывает контекст запроса и не выполняет какой-либо семантической обработки. Результат представляет собой список лемм из исходного текста.
4. **Выбор изображения**: Выбирает наиболее релевантное изображение на основе совпадения между извлеченными ключевыми словами/фразами и тегами изображений, хранящимися в базе данных.
5. **Callback-ответ**: Отправляет выбранное изображение в формате base64 на предоставленный callback URL.

## Установка

1. Клонируйте репозиторий

git clone https://github.com/DaryaSinitsyna/AsyncImageCallbackAPI.git

2. Установите необходимые зависимости из файла requirements.txt

## Настройка

1. Создайте файл .env с полями как в .env.example
2. Настройте миграции базы данных

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head


## Использование

1. Запустите сервер API:

uvicorn app.main:app --reload

2. Загрузите изображения на эндпоинт /images/upload с API-ключом в заголовке "X-API-Key".
3. Отправьте текстовый запрос и callback URL на эндпоинт /images/tags с API-ключом в заголовке "X-API-Key".
4. API обработает текстовый запрос, выберет наиболее релевантное изображение и отправит его на предоставленный callback URL в формате base64.
