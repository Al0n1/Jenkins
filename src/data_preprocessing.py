import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import joblib

def preprocess_data():
    """
    Загружает сырые данные, выполняет предобработку и сохраняет результаты
    """
    # Создаем директорию для обработанных данных
    os.makedirs('data/processed', exist_ok=True)
    
    # Загружаем данные
    df = pd.read_csv('data/raw/iris_dataset.csv')
    
    # Разделяем признаки и целевую переменную
    X = df.drop(['target', 'target_names'], axis=1)
    y = df['target_names']
    
    # Разделяем на тренировочную и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Масштабирование признаков
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Сохраняем обработанные данные
    np.save('data/processed/X_train.npy', X_train_scaled)
    np.save('data/processed/X_test.npy', X_test_scaled)
    np.save('data/processed/y_train.npy', y_train)
    np.save('data/processed/y_test.npy', y_test)
    
    # Сохраняем scaler для последующего использования
    joblib.dump(scaler, 'data/processed/scaler.joblib')
    
    print("Preprocessing completed. Files saved in data/processed/")

if __name__ == "__main__":
    preprocess_data()
