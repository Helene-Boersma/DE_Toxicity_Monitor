pipeline{
    agent any
    
    stages{
        stage('Docker build / Up') {
            steps {
                parallel(
                    docker: {
                        sh "docker-compose up --build"
                    },
                    test: {
                        sleep 30
                        sh "pytest"
                    }
                )
            }
        }
    }
    post {
      always {
         sh "docker-compose down || true"
      }
   } 
}
