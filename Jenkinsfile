pipeline{
    agent any
    
    stages{
        stage('NPM Build'){
            steps{
                sh "docker-compose build"
            }
        }
        stage('Docker up / down') {
            steps {
                // sh "docker-compose up"
                echo 'Testing'
                // sh "docker-compose down"
            }
        }
        stage('Unit Test'){
            steps{
                sh "python -m pytest Test/unit_tests.py"
            }
        }
    }
}