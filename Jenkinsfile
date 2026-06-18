pipeline {
    agent any
    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Barsha01p/2-tierflask-app.git'
            }
        }
        
        stage('Build image') {
            steps {
                // 1. INJECT THIS LINE: Tells Docker to use BuildKit
                env.DOCKER_BUILDKIT = '1'
                
                // 2. CHANGE THIS LINE: Uses the modern buildx component
                sh 'docker buildx build -t flask-app .'
            }
        }
        
        stage('Deploy with docker compose') {
            steps {
                // 3. INJECT THIS LINE HERE TOO: Keeps docker compose modern
                env.DOCKER_BUILDKIT = '1'
                
                // existing container if they are running
                sh 'docker compose down || true'
                // start app, rebuilding flask image
                sh 'docker compose up -d --build'
            }
        }
    }
}

