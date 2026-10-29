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

    stages {
        stage('download code / checkout code') {
            steps {
                checkout scm
            }
        }
        stage('show python version') {
            steps {
                sh "python3 --version"
            }
        }
        stage('run python program') {
            steps {
                sh "python3 read.py"
            }
        }
    }
}