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
                sh "pip install pytest"
                sh "python3 -m pytest Test/unit_tests.py"
                sh "python3 -m pytest Test/test_web_page.py"
            }
        }
    }
}