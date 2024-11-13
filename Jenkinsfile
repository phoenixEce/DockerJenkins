pipeline {
    agent any
    environment {
    //    CONTAINER_ID = 63a0166e427d
       SUM_PY_PATH = 'E:/Cours/MSC1/Devops/TP_Jenkins/sum.py'
       DIR_PATH = 'E:/Cours/MSC1/Devops/TP_Jenkins'
       TEST_FILE_PATH = 'E:/Cours/MSC1/Devops/TP_Jenkins/test_variables.txt'
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

         stage('Run') {
            steps {
                script {
                   echo 'Démarrage du conteneur Docker...'
                    def output = sh(script: 'docker run -d python-sum tail -f /dev/null', returnStdout: true)
                    CONTAINER_ID = output.trim()
                    echo "Conteneur démarré avec l'ID : ${CONTAINER_ID}"
                }
            }
        }


    }
    
}