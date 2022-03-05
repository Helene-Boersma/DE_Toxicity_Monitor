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
                sh "python -m pytest /home/my_jenkins_home/workspace/dataeng_final_project_automation/Test/unit_tests.py"
            }
        }
    }
}