from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn
import os

# Модель Pydantic для входных данных
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Модель Pydantic для ответа
class PredictionResponse(BaseModel):
    prediction: str
    probability: float

app = FastAPI(
    title="Iris Classifier API",
    description="API для классификации ирисов с использованием модели RandomForest",
    version="1.0.0"
)

# Глобальные переменные для модели и scaler
model = None
scaler = None

@app.on_event("startup")
async def load_model():
    """Загрузка модели и scaler при запуске приложения"""
    global model, scaler
    try:
        model = joblib.load('models/rf_model.joblib')
        scaler = joblib.load('data/processed/scaler.joblib')
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        raise Exception("Failed to load model or scaler")

@app.post("/predict", response_model=PredictionResponse)
async def predict(features: IrisFeatures):
    """
    Предсказание класса ириса на основе входных характеристик
    
    Args:
        features (IrisFeatures): характеристики ириса
        
    Returns:
        PredictionResponse: предсказанный класс и вероятность
    """
    try:
        # Преобразуем входные данные в массив
        features_array = np.array([
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]).reshape(1, -1)
        
        # Масштабируем данные
        features_scaled = scaler.transform(features_array)
        
        # Получаем предсказание и вероятности
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        max_probability = float(max(probabilities))
        
        return PredictionResponse(
            prediction=prediction,
            probability=max_probability
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("deploy_model:app", host="0.0.0.0", port=port, reload=True)
