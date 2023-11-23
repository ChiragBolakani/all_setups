pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
                    call %python_venv%
                    python hello.py
                    python get_setup_names.py
                    python get_setup_data_json.py
                    python get_input_data.py
                    python label_encoding.py
                    python fit_model.py
                    python fit_dct.py
                    python empty_directory.py
                """
            }
        }
        stage('Test') {
            steps {
                bat """
                    call %python_venv%
                    python result_analysis.py
                """
            }
        }
    }
} 