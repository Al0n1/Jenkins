pipeline {
    agent any
    
    environment {
        // Путь к виртуальному окружению Python
        VENV = "venv"
    }
    
    stages {
        stage('Setup') {
            steps {
                script {
                    // Создание виртуального окружения
                    bat """
                        python -m venv ${VENV}
                        source ${VENV}\\bin\\activate
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }
        
        stage('Data Collection') {
            steps {
                script {
                    bat """
                        source ${VENV}\\bin\\activate
                        python src/data_collection.py
                    """
                }
            }
        }
        
        stage('Data Preprocessing') {
            steps {
                script {
                    bat """
                        source ${VENV}\\bin\\activate
                        python src/data_preprocessing.py
                    """
                }
            }
        }
        
        stage('Model Training') {
            steps {
                script {
                    bat """
                        source ${VENV}\\bin\\activate
                        python src/train_model.py
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Запуск FastAPI приложения через uvicorn
                    bat """
                        source ${VENV}\\bin\\activate
                        start /B uvicorn src.deploy_model:app --host 0.0.0.0 --port 8000
                    """
                }
            }
        }
    }
    
    post {
        always {
            // Очистка после сборки
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
