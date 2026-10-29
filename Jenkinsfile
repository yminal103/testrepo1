// pipeline {
//     agent any

//     stages{
//         stage('checkout code') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('run python program') {
//             steps {
//                 sh "python extract.py"
//             }
//         }
//     }
// }



pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'puthon3'
    }

    stages {
        stage('download code / checkout code') {
            steps {
                checkout scm
            }
        }
        stage('show python version') {
            steps {
                sh "$PYTHON_VERSION --version"
            }
        }
        stage('run python program') {
            steps {
                sh "$PYTHON_VERSION read.py"
            }
        }
    }
}