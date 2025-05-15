# ML Pipeline для классификации Iris

Этот проект демонстрирует реализацию CI/CD конвейера для проекта машинного обучения с использованием Jenkins. Проект включает в себя полный цикл: от сбора данных до развертывания модели.

## Структура проекта

```
project/
├── data/                      # Директория для данных
│   ├── raw/                  # Сырые данные
│   └── processed/            # Обработанные данные
├── src/                      # Исходный код
│   ├── data_collection.py    # Сбор данных
│   ├── data_preprocessing.py # Обработка данных
│   ├── train_model.py       # Обучение модели
│   └── deploy_model.py      # Развертывание модели
├── models/                   # Директория для моделей
├── tests/                   # Модульные тесты
├── requirements.txt         # Зависимости
└── Jenkinsfile             # Описание CI/CD пайплайна
```

## Этапы конвейера

1. **Setup**: Создание виртуального окружения и установка зависимостей
2. **Data Collection**: Загрузка датасета Iris
3. **Data Preprocessing**: Предобработка данных и разделение на выборки
4. **Model Training**: Обучение модели RandomForest
5. **Testing**: Запуск модульных тестов
6. **Deploy**: Развертывание модели как REST API

## Использование API

После развертывания, API будет доступен по адресу `http://localhost:8000`. 

### Swagger UI

FastAPI автоматически генерирует интерактивную документацию API:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints

#### POST /predict
Предсказание класса ириса по его характеристикам.

Пример запроса:
```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

Пример ответа:
```json
{
    "prediction": "setosa",
    "probability": 0.95
}
```

### Преимущества FastAPI

- Автоматическая OpenAPI документация (Swagger UI)
- Валидация данных через Pydantic
- Асинхронная обработка запросов
- Высокая производительность

## Локальный запуск

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте окружение:
```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Запустите этапы конвейера:
```bash
python src/data_collection.py
python src/data_preprocessing.py
python src/train_model.py
python src/deploy_model.py
```

## Jenkins

1. Создайте новый Pipeline проект в Jenkins
2. Укажите путь к репозиторию с проектом
3. Jenkins автоматически найдет Jenkinsfile и запустит конвейер