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
                    echo "Construction de l'image Docker........"
                    bat "docker build -t python-sum \"${DIR_PATH}\""
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    echo 'Démarrage du conteneur Docker.........'
                    def output = bat(script: 'docker run -d python-sum tail -f /dev/null', returnStdout: true)
                    CONTAINER_ID = output.trim().split('\r\n')[-1].trim()
                    echo "Conteneur démarré avec l'ID : ${CONTAINER_ID}"
                }
            }
        }

        stage('Test'){
            steps {
                script{
                    echo"Exécution des tests..........."
                    def testLines = readFile("${TEST_FILE_PATH}").split('\n')
                        for (line in testLines) {
                            line = line.trim()
                            if(line && line.split(' ').length == 3) {
                                def vars = line.split(' ')
                                try {
                                    def arg1 = vars[0]
                                    def arg2 = vars[1]
                                    def expectedSum = vars[2].toFloat()

                                    def output = bat(script: "docker exec ${CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}", returnStdout: true)
                                    def result = output.split('\n')[-1].trim().toFloat()

                                    if (result == expectedSum) {
                                        echo "Test réussi pour ${arg1} + ${arg2} = ${expectedSum}"
                                    } else {
                                        error "Échec du test pour ${arg1} + ${arg2}. Résultat attendu : ${expectedSum}, obtenu : ${result}"
                                    }
                                } catch (Exception e){
                                    error "Erreur lors du traitement de la ligne '${line}': ${e.message}"
                                }
                            } else {
                                echo "Ligne ignorée : '${line}' (format incorrect)"
                            }
                        }
                }   
            }
        }
        
    }

}
    
