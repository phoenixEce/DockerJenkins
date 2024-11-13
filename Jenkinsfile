pipeline {
    agent any
    environment {
       CONTAINER_ID = 63a0166e427d
       SUM_PY_PATH = E:\Cours\MSC1\Devops\TP_Jenkins\sum.py
       DIR_PATH = E:\Cours\MSC1\Devops\TP_Jenkins\Dockerfile
       TEST_FILE_PATH = E:\Cours\MSC1\Devops\TP_Jenkins\test_variables.txt
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