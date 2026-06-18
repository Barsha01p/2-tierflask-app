pipeline {
    agent any
    
    // Defines BuildKit globally for all stages in this pipeline
    environment {
        DOCKER_BUILDKIT = '1'
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Barsha01p/2-tierflask-app.git'
            }
        }
        
        stage('Build image') {
            steps {
                // No raw variable assignments allowed here anymore
                sh 'docker buildx build -t flask-app .'
            }
        }
        
        stage('Deploy with docker compose') {
            steps {
                // Existing containers are torn down safely
                sh 'docker compose down || true'
                // Start app components, building via modern Docker mechanics
                sh 'docker compose up -d --build'
            }
        }
    }
}


