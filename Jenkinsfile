pipeline {
  agent any
  stages {
    stage('ejecutar') {
      steps {
        sh 'python3 --version'
        sh 'ls -la'
        sh 'python3 back.py'
      }
    }
  }
}
