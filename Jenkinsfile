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
                        bat "python -m pytest Test/unit_tests.py"
                    }
                )
            }
        }
    }
    bat "docker-compose down"
}
