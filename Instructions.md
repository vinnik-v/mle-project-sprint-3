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

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:...' \
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
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