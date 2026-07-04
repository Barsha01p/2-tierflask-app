pipeline {
    // 1. Instructs Jenkins to execute this script directly on your EC2 host filesystem
    agent any

    stages {
        stage('Step 1: Pull Code from GitHub') {
            steps {
                // Pulls down the latest code changes automatically from your repository
                checkout scm
            }
        }

        stage('Step 2: Clean Old Containers') {
            steps {
                echo 'Wiping out old deployment boxes...'
                // Shuts down existing running apps to avoid port collision errors
                sh 'sudo docker compose down --remove-orphans'
            }
        }

        stage('Step 3: Build & Deploy New Stack') {
            steps {
                echo 'Compiling and launching fresh containers...'
                // Automatically rebuilds your Dockerfile updates and boots them in background mode
                sh 'sudo docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo '=================================================='
            echo ' SUCCESS: Your Two-Tier App is live on Port 5000! '
            echo '=================================================='
        }
        failure {
            echo '=================================================='
            echo ' FAILURE: Pipeline broke. Check the logs above.   '
            echo '=================================================='
        }
    }
}

