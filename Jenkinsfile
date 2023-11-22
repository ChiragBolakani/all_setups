pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat "call ml_venv/activate"
                bat "python get_setup_names.py"
            }
        }
    }
}