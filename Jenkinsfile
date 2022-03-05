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
                        sh "python3 -m pytest Test/unit_tests.py"
                    },
                    test2: {
                        sleep 30
                        sh "python3 -m pytest Test/test_web_page.py "
                    },
                    shutdown: {
                        sleep 50
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
