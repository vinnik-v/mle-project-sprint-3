from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
import joblib

# Модель запроса
class PredictionRequest(BaseModel):
    model_params: Dict[str, float] = Field(
        ..., 
        example={
            "build_year": 2005,
            "building_age": 20,
            "floor": 5,
            "high_ceiling_flag": 1,   # Признак "Высокие потолки"
            "is_central": 0,          # Признак центрального расположения
            "kitchen_area**3": 14.0,
            "latitude": 55.53,
            "longitude": 37.508,
            "rooms": 2
        }
    )

# Класс-обработчик
class FastApiHandler:
    def __init__(self):
        self.required_model_params = [
            "build_year", "building_age", "floor", "high_ceiling_flag",
            "is_central", "kitchen_area**3", "latitude", "longitude", "rooms"
        ]
        try:
            self.model = joblib.load("./models/model.pkl")
        except Exception as e:
            raise RuntimeError(f"Ошибка загрузки модели: {e}")

    def validate_params(self, params: Dict[str, float]) -> bool:
        return set(params.keys()) == set(self.required_model_params)

    def predict(self, features: Dict[str, float]) -> float:
        feature_values = [features[param] for param in self.required_model_params]
        prediction = self.model.predict([feature_values])[0]
        return round(float(prediction), 2)

# Создание FastAPI-приложения
app = FastAPI(
    title="Price Predictor API",
    description="API для предсказания стоимости квартиры на основе признаков",
    version="1.0"
)

handler = FastApiHandler()

# Экспортер метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Счётчик запросов
prediction_requests_total = Counter(
    "prediction_requests_total",
    "Общее количество запросов"
)

# Гистограмма предсказаний
prediction_values_histogram = Histogram(
    "prediction_values_histogram",
    "Гистограмма прогнозируемых значений",
    buckets=(1e6, 5e6, 1e7, 1.5e7, 2e7, 2.5e7, 3e7, 5e7)
)

@app.post(
    "/predict",
    summary="Предсказание стоимости квартиры",
    description="Функция для предсказания цены жилой недвижимости на основе входных признаков"
)
def predict_price(request: PredictionRequest):
    if not handler.validate_params(request.model_params):
        raise HTTPException(status_code=400, detail="Ошибка в параметрах запроса")
    
    prediction_requests_total.inc()  # увеличиваем счётчик
    prediction = handler.predict(request.model_params)
    prediction_values_histogram.observe(prediction)  # записываем в гистограмму
    return {"prediction": prediction}
