pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest'
            }
        }
    }
}