pipeline{
    agent any
    
    stages{
        stage('Docker Build'){
            steps{
                sh "docker-compose build"
            }
        }
        stage('Docker up / down') {
            steps {
                parallel(
                    docker: {
                        sh "docker-compose up"
                        sh "y"
                    },
                    test: {
                        sleep 300
                        sh "pip install pytest"
                        sh "python3 -m pytest Test/unit_tests.py"
                    }
                )
                
                // sh "docker-compose up"
                // echo 'Testing'
                // // sh "docker-compose down"
            }
        }
        // stage('Unit Test'){
        //     steps{
        //         sh "pip install pytest"
        //         sh "python3 -m pytest Test/unit_tests.py"
        //         //sh "pip install selenium"
        //         //sh "python3 -m pytest Test/test_web_page.py"
        //     }
        // }
    }
}
