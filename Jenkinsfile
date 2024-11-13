pipeline {
    agent any
    environment {
       CONTAINER_ID = 63a0166e427d
       SUM_PY_PATH = 'sum.py'
       DIR_PATH = 'Dockerfile'
       TEST_FILE_PATH = 'test_variables.txt'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Construction image docker'
                dir("${DIR_PATH}") {
                    sh 'docker build -t python-sum .'
                }
            }
        }

        stage('Run'){
            steps {
                echo 'Running image docker'
            }
        }
    }
}