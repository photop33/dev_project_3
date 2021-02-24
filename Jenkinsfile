pipeline {
agent any
stages {
    stage('pull from git') {
        steps {
            /* bat 'git.exe reset --hard' */
            /* bat 'git.exe rev-parse --verify HEAD' */
            bat 'git.exe clean -ffdx'
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
			bat 'sleep(time: 30, unit: 'SECONDS')'
            bat 'python backend_testing.py'
        }
    }
    stage('clean environment') {
        steps {
            bat 'python clean_environment.py'
            bat 'git.exe clean -ffdx'
            /* bat 'del /f/q/s *.*' */
        }
    }
    stage('build image') {
        steps {
            bat 'docker build -t "iitzhakk/dev_proj_3" .'
        }
    }
    stage('push image') {
        steps {
            bat 'docker push -q iitzhakk/dev_proj_3'
        }
    }
    stage('docker-compose up') {
        steps {
            bat 'echo IMAGE_TAG=${BUILD_NUMBER} > .env'
            bat 'echo IMAGE_TAG=${BUILD_NUMBER}'
			bat 'echo IMAGE_TAG=${env.BUILD_NUMBER}'
			bat 'echo IMAGE_TAG=$BUILD_NUMBER'
			bat 'docker-compose up -d'
			/* need to wait for the DB to be ready */
			bat 'sleep(240)'
        }
    }
    stage('testing docker-compose') {
        steps {
            bat 'python docker_backend_testing.py'
        }
    }
    stage('clean docker environment') {
        steps {
            bat 'docker-compose down --rmi all'
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