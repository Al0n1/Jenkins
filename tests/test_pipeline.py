import pytest
import os
import pandas as pd
import numpy as np
from src.data_collection import collect_data
from src.data_preprocessing import preprocess_data
from src.train_model import train_model

def test_data_collection():
    """Проверка сбора данных"""
    collect_data()
    assert os.path.exists('data/raw/iris_dataset.csv')
    
    df = pd.read_csv('data/raw/iris_dataset.csv')
    assert not df.empty
    assert 'target' in df.columns
    assert 'target_names' in df.columns

def test_data_preprocessing():
    """Проверка предобработки данных"""
    preprocess_data()
    
    # Проверяем существование файлов
    assert os.path.exists('data/processed/X_train.npy')
    assert os.path.exists('data/processed/X_test.npy')
    assert os.path.exists('data/processed/y_train.npy')
    assert os.path.exists('data/processed/y_test.npy')
    assert os.path.exists('data/processed/scaler.joblib')
    
    # Проверяем размерности данных
    X_train = np.load('data/processed/X_train.npy')
    X_test = np.load('data/processed/X_test.npy')
    y_train = np.load('data/processed/y_train.npy')
    y_test = np.load('data/processed/y_test.npy')
    
    assert X_train.shape[1] == X_test.shape[1] == 4  # 4 признака
    assert len(X_train) > len(X_test)  # train больше test

def test_model_training():
    """Проверка обучения модели"""
    train_model()
    assert os.path.exists('models/rf_model.joblib')

if __name__ == '__main__':
    pytest.main([__file__])
