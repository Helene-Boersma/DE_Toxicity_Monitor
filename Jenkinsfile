pipeline{
    agent any
    
    stages{
        stage('Docker build / Up') {
            steps {
                parallel(
                    docker: {
                        bat "docker-compose up --build"
                    },
                    test: {
                        sleep 30
                        bat "pytest Test/unit_tests.py"
                    }
                )
            }
        }
    }
    post {
      always {
         bat "docker-compose down || true"
      }
   } 
}
