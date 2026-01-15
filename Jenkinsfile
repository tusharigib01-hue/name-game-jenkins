pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                    # Update packages
                    apt update

                    # Install Python and tools if not already installed
                    apt install -y python3 python3-venv python3-pip

                    # Create virtual environment
                    python3 -m venv $VENV_DIR

                    # Activate virtual environment using dot (works in Jenkins sh)
                    . $VENV_DIR/bin/activate

                    # Upgrade pip inside virtual environment
                    pip install --upgrade pip

                    # Install project dependencies (if requirements.txt exists)
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    # Activate virtual environment
                    . $VENV_DIR/bin/activate

                    # Run your tests (example with pytest)
                    if [ -f pytest.ini ] || [ -d tests ]; then
                        pytest
                    else
                        echo "No tests found, skipping"
                    fi
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Build and tests completed successfully!"
        }
        failure {
            echo "❌ Build FAILED"
        }
    }
}




