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

        stage('Run') {
            steps {
                script {
                    echo 'Démarrage du conteneur Docker...'
                    def output = sh(script: 'docker run -d -python-sum tail -f /dev/null', returnStdout: true)
                    CONTAINER_ID = output.trim()
                    echo "Conteneur démarré avec l’ID : ${CONTAINER_ID}"
                }
            }
        }
    }
}