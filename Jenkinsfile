pipeline {
    agent any
    environment {
        COMPOSE_PROJECT_NAME = "poli2"
        CODECOV_TOKEN = credentials('codecov-token') // Token de Codecov en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dress97/docker-flask-mysql-demo.git', branch: 'main', credentialsId: 'github-token'
            }
        }

        stage('Build images') {
            steps {
                sh 'docker compose -f docker-compose.yml build --no-cache'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --cov=app tests/'  // Ejecuta tests y genera cobertura
            }
        }

        stage('Upload Coverage') {
            steps {
                sh 'bash <(curl -s https://codecov.io/bash) -t $CODECOV_TOKEN'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d --remove-orphans'
            }
        }

        stage('Smoke test') {
            steps {
                sh 'sleep 8'
                sh 'curl --fail http://localhost:5000/ || (echo "App no respondió"; exit 1)'
            }
        }
    }

    post {
        success {
            echo 'Deployment exitoso y tests pasados ✅'
        }
        failure {
            echo 'Algo falló en el pipeline ❌'
        }
    }
}
