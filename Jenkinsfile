pipeline {
    agent any
    
    environment {
        // Automatically turns on modern BuildKit without requiring buildx extensions
        DOCKER_BUILDKIT = '0'
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Barsha01p/2-tierflask-app.git'
            }
        }
        
        stage('Build image') {
            steps {
                // CHANGED THIS LINE: Replaced 'buildx build' with 'build'
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Deploy with docker compose') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
    }
}
