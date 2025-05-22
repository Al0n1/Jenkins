import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_model():
    """
    Загружает обработанные данные, обучает модель и сохраняет её
    """
    # Создаем директорию для моделей
    os.makedirs('models', exist_ok=True)
    
    # Загружаем обработанные данные
    X_train = np.load('data/processed/X_train.npy', allow_pickle=True)
    X_test = np.load('data/processed/X_test.npy', allow_pickle=True)
    y_train = np.load('data/processed/y_train.npy', allow_pickle=True)
    y_test = np.load('data/processed/y_test.npy', allow_pickle=True)
    
    # Создаем и обучаем модель
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Оцениваем качество модели
    y_pred = model.predict(X_test)
    print("\nModel Performance Report:")
    print(classification_report(y_test, y_pred))
    
    # Сохраняем модель
    model_path = 'models/rf_model.joblib'
    joblib.dump(model, model_path)
    print(f"\nModel saved to {model_path}")

if __name__ == "__main__":
    train_model()
