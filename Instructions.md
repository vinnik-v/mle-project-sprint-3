# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
### Установка зависимостей

- Перейти в папку `/services`
- Выполнить следующие команды
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Запуска сервера

```bash
uvicorn ml_service.main:app --reload --host 0.0.0.0 --port 8081
```
Swagger: `http://localhost:8081/docs`

### Пример curl-запроса к микросервису

```bash
curl -X POST "http://localhost:8081/predict" \
-H "Content-Type: application/json" \
-d '{
  "model_params": {
    "build_year": 2005,
    "building_age": 20,
    "floor": 5,
    "high_ceiling_flag": 1,
    "is_central": 0,
    "kitchen_area**3": 14,
    "latitude": 55.53,
    "longitude": 37.508,
    "rooms": 2
  }
}'
```
Ожидаемый ответ: `{"prediction":11868424.11}`

## 2. FastAPI микросервис в Docker-контейнере
### Сборка образа
```bash
docker image build . -t predictor:latest
```
### Запуск контейнера
```bash
docker container run -p 8081:8081 --env-file .env predictor:latest
```
Swagger: `http://localhost:8081/docs`

### Пример curl-запроса к микросервису

```bash
curl -X POST "http://localhost:8081/predict" \
-H "Content-Type: application/json" \
-d '{
  "model_params": {
    "build_year": 2005,
    "building_age": 20,
    "floor": 5,
    "high_ceiling_flag": 1,
    "is_central": 0,
    "kitchen_area**3": 14,
    "latitude": 55.53,
    "longitude": 37.508,
    "rooms": 2
  }
}'
```
Ожидаемый ответ: `{"prediction":11868424.11}`

## 3. Docker compose для микросервиса и системы моониторинга
### Сборка и запуск
```bash
docker compose up --build
```

### Адреса после запуска:

- Микросервис: `http://localhost:8081/docs`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (логин/пароль: admin/admin)
- Метрики: `http://localhost:8081/metrics`

### Пример curl-запроса к микросервису

```bash
curl -X POST "http://localhost:8081/predict" \
-H "Content-Type: application/json" \
-d '{
  "model_params": {
    "build_year": 2005,
    "building_age": 20,
    "floor": 5,
    "high_ceiling_flag": 1,
    "is_central": 0,
    "kitchen_area**3": 14,
    "latitude": 55.53,
    "longitude": 37.508,
    "rooms": 2
  }
}'
```
Ожидаемый ответ: `{"prediction":11868424.11}`

#### Выгрузка метрик
```bash
curl -X GET "http://localhost:8081/metrics"
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...