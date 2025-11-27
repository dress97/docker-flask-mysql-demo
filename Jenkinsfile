pipeline {
    agent any
    environment {
        COMPOSE_PROJECT_NAME = "poli2"
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dress97/docker-flask-mysql-demo.git', branch: 'main', credentialsId: 'github-token'
            }
        }

        stage('Build images') {
            steps {
                // asegura permisos, ejecuta docker compose build
                sh 'docker compose -f docker-compose.yml build --no-cache'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d --remove-orphans'
            }
        }

        stage('Smoke test') {
            steps {
                // simple test: consulta al endpoint
                sh 'sleep 8' // espera que el servicio arranque
                sh 'curl --fail http://localhost:5000/ || (echo "App no respondió"; exit 1)'
            }
        }
    }

    post {
        success {
            echo 'Deployment exitoso.'
        }
        failure {
            echo 'Algo falló en el pipeline.'
        }
    }
}
