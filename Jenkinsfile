pipeline{
    agent any
    
    stages{
        stage('NPM Build'){
            steps{
                sh "docker-compose up --build"
            }
        }
    stage('Unit Test'){
            steps{
                sh "python -m pytest Test/unit_tests.py"
            }
        }
    }
}
