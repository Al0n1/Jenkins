import pandas as pd
from sklearn.datasets import load_iris
import os

def collect_data():
    """
    Загружает датасет Iris и сохраняет его в CSV файл
    """
    # Создаем директорию для данных, если её нет
    os.makedirs('data/raw', exist_ok=True)
    
    # Загружаем датасет
    iris = load_iris()
    
    # Создаем DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target_names'] = df['target'].map({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    })
    
    # Сохраняем в CSV
    output_file = 'data/raw/iris_dataset.csv'
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")

if __name__ == "__main__":
    collect_data()
