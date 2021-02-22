pipeline {
agent any
stages {
    stage('pull from git') {
        steps {
            bat 'git clone https://github.com/isaacTadela/dev_project_3'
        }
    }
    stage('rest app') {
        steps {
            bat 'pip install -r requirements.txt'
            bat 'start /min python rest_app.py'
        }
    }
    stage('testing backend') {
        steps {
            bat 'python backend_testing.py'
        }
    }
    stage('clean environment') {
        steps {
            bat 'python clean_environment.py'
        }
    }
    stage('build image') {
        steps {
            bat ' '
        }
    }
    stage('push image') {
        steps {
            bat ' '
        }
    }
    stage('docker-compose up') {
        steps {
            bat ' '
        }
    }
    stage('wait for docker-compose') {
        steps {
            bat ' '
        }
    }
    stage('testing docker-compose') {
        steps {
            bat ' '
        }
    }
 }
 post {
        always {
            echo 'One way or another, I have finished'
            /* deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}