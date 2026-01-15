pipeline {
    agent any

    stages {
        stage('Install Python & Dependencies') {
            steps {
                sh '''
                # Update package list
                apt update

                # Install Python3 and pip
                apt install -y python3 python3-pip

                # Install required Python packages
                pip3 install -r requirements.txt
                '''
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

