properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any
    options {
        ansiColor('xterm')
    }

    stages {
        stage('Init') {
            steps {
                echo 'Initializing ciLogger test'
                sh 'python3 test/test_init.py -b $BUILD_NUMBER'
            }
        }
        stage('Test') {
            steps {
                echo 'Running ciLogger test'
                sh 'python3 test/test.py'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Finalizing ciLogger test'
                sh 'python3 test/test_final.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts '*.htm'
        }
    }
}