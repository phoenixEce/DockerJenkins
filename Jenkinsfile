pipeline {
    agent any
    environment {
    //    CONTAINER_ID = 63a0166e427d
       SUM_PY_PATH = 'sum.py'
       DIR_PATH = 'Dockerfile'
       TEST_FILE_PATH = 'test_variables.txt'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Construction de l'image Docker..."
                    bat "docker build -t python-sum \"${DIR_PATH}\""
                }
            }
        }

    }
    
}