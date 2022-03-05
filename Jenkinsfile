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
                  //      bat "pip install pytest"
                        bat "python -m pytest Test/unit_tests.py"
                    }
                )
                // bat "docker-compose up"
                // echo 'Testing'
                // // bat "docker-compose down"
            }
        }
        // stage('Unit Test'){
        //     steps{
        //         bat "pip install pytest"
        //         bat "python -m pytest Test/unit_tests.py"
        //         //bat "pip install selenium"
        //         //bat "python3 -m pytest Test/test_web_page.py"
        //     }
        // }
    }
}
