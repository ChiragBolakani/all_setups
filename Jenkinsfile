pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat "call %python_venv%"
                bat "python hello.py"
                bat "python get_setup_names.py"
            }
        }
    }
}