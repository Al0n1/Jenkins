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
                    sh """
                        python3 -m venv ${VENV}
                        . ${VENV}/bin/activate
                        python3 -m pip install --upgrade pip
                        python3 -m pip install "setuptools<69" wheel
                        pip install -r requirements.txt
                    """
                }
            }
        }
        
        stage('Data Collection') {
            steps {
                script {
                    sh """
                        . ${VENV}/bin/activate
                        python3 src/data_collection.py
                    """
                }
            }
        }
        
        stage('Data Preprocessing') {
            steps {
                script {
                    sh """
                        . ${VENV}/bin/activate
                        python3 src/data_preprocessing.py
                    """
                }
            }
        }
        
        stage('Model Training') {
            steps {
                script {
                    sh """
                        . ${VENV}/bin/activate
                        python3 src/train_model.py
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    // Запуск FastAPI приложения через uvicorn
                    sh """
                        . ${VENV}/bin/activate
                        uvicorn src.deploy_model:app --host 0.0.0.0 --port 8000 &
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
