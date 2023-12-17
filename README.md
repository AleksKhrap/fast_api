# Микросервисы FastAPI
## Описание проекта
Проект представляет собой несколько взаимодействующих между собой сервисов, практически все функции в них асинхронные.
Это вариация работы веб-приложения Заказов.

Тестировал все через Postman. Kafka работает через docker-compose. Документация доступна по адресу
http://127.0.0.1:8000/docs после запуска приложения

## Структура проекта
### Product Service
- Описание функций: CRUD операции с продуктами, подключение к БД Postgresql+asyncpg, 
использование SqlAlchemy, для миграций Alembic.
  
### Order Service
- Описание функций: Создание и отмена заказов, взаимодействие с сервисом Inventory через REST API, 
работа с MongoDB через motor, использование Kafka (producer) для отправки сообщений о статусах заказов.
  
### Inventory Service
- Описание функций: Аналог Product Service с дополнительными полями, CRUD операции, 
использование БД Postgresql+asyncpg.

### Notification Service
- Описание функций: Consumer Kafka, прием и сохранение сообщений о статусах заказов в MongoDB на движке motor.

## Технологии
- FastAPI
- PostgreSQL + asyncpg
- MongoDB (motor)
- SQLAlchemy
- Alembic
- Kafka
- Docker-compose

## Планы по развитию
Сейчас в планах разработать ещё один сервис GraphQL, который объединит Product и Order в единый REST API.

А в конце упаковать все это в Docker и Kubernetes.

## Установка и запуск проекта
### 1. Клонирование репозитория

```bash
git clone https://github.com/AleksKhrap/microservices.git
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка БД
Вам понадобятся установленные PostgreSQL и MongoDB.

Для создания таблиц для сервисов Product и Order используйте Alembic 
(если возникнет ошибка при применении миграции, то смотрите возможное решение в файле 
"microservices/ProductService/alembic/env.py").

Перейдите в каталог Product:
```bash
cd microservices/ProductService
```

Далее примените последнюю миграцию:
```bash
alembic upgrade head
```

Аналогично для Order:
```bash
cd ../OrderService
```

Применение последней миграции:
```bash
alembic upgrade head
```

### 4. Запуск Kafka

Необходимо запустить контейнер с Kafka:
```bash
cd microservices
docker-compose up -d
```

### 5. Запуск сервисов

Можно как с флагом, так и без.
```bash
uvicorn main:app --reload 
```

### 6. Тестирование через Postman

Используйте Postman или встроенный Swagger UI для тестирования API каждого сервиса.

### 7. Запуск через Docker и Kubernetes

В планах использование Docker для упаковки приложения и Kubernetes для его развертывания. 
Подробные инструкции будут добавлены в дальнейшем.