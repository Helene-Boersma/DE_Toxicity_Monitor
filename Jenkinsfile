pipeline{
    agent any
    
    stages{
        stage('Docker build / Up') {
            steps {
                parallel(
                    docker: {
                        sh "docker-compose up --build"
                    },
                    unit_tests: {
                        sleep 20
                        sh "python3 -m pytest model/unit_tests.py"
                    },
                    stress_test: {
                        sleep 40
                        sh "python3 -m pytest Test/stress_test.py"
                    },
                    shutdown: {
                        sleep 60
                        sh "docker-compose down"
                    }
                )
            }
        }
    }
    
}

