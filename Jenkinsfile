pipeline {
  agent none
  stages {
    stage('Docker Build') {
      steps {
        sh 'sh "docker-compose build"'
      }
    }

    stage('Docker up') {
      parallel {
        stage('Docker up') {
          steps {
            sh 'docker-compose up'
          }
        }

        stage('Unit_test') {
          steps {
            sh 'python3 -m pytest unit_tests.py'
          }
        }

      }
    }

  }
}