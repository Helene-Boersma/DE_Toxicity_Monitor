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
                        sleep 12
                        bat "python -m pytest Test/unit_tests.py"
                    }
                )
            }
        }
        stage('Docker Down'){
            steps{
                sleep 60
                bat "docker-compose down"
            }
        }
    }
}
