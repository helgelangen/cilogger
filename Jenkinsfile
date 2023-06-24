properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any
    options {
        ansiColor('xterm')
    }

    stages {
        stage('Init') {
            steps {
                printf 'Initializing ciLogger test'
                sh 'python3 test/test_init.py'
            }
        }
        stage('Test') {
            steps {
                printf 'Running ciLogger test'
                sh 'python3 test/test.py'
            }
        }
        stage('Finalize') {
            steps {
                printf 'Finalizing ciLogger test'
                sh 'python3 test/test_final.py'
            }
        }
    }
}