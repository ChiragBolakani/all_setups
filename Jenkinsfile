pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
                    call %python_venv%
                    python hello.py
                    python get_setup_names.py
                """
            }

            steps{
                
            }
        }
    }
}