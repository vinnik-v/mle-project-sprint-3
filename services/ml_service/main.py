from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
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

@app.post(
    "/predict",
    summary="Предсказание стоимости квартиры",
    description="Функция для предсказания цены жилой недвижимости на основе входных признаков"
)
def predict_price(request: PredictionRequest):
    if not handler.validate_params(request.model_params):
        raise HTTPException(status_code=400, detail="Ошибка в параметрах запроса")

    prediction = handler.predict(request.model_params)
    return {"prediction": prediction}
