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
                        sleep 20
                        sh "python3 -m pytest model/unit_tests.py"
                    },
                    shutdown: {
                        sleep 210
                        sh "docker-compose down"
                    }
                )
            }
        }
    }
    
//     post {
//       always {
//          sh "docker-compose down || true"
//       }
//     } 
    
}
