pipeline {
    agent any

    stages {
        stage('Install Python & Dependencies') {
            steps {
                sh '''
                # Update packages
                apt update

                # Install Python3 and venv module
                apt install -y python3 python3-venv python3-pip

                # Create virtual environment
                python3 -m venv venv

                # Activate venv
                source venv/bin/activate

                # Install Python dependencies inside venv
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Build SUCCESS: Tests passed!'
        }
        failure {
            echo '❌ Build FAILED'
        }
    }
}


