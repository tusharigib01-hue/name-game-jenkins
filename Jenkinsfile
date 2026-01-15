pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo '🎉 Build SUCCESS: Game logic is correct!'
        }
        failure {
            echo '❌ Build FAILED: Fix the game logic!'
        }
    }
}
