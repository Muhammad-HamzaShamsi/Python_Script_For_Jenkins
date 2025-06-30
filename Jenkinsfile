pipeline {
    agent { 
        node {
            label 'docker_first_agent_python'
            }
      }
      triggers {
        pollSCM '*/5 * * * *' // Runs every 5 minutes
      }
    stages {
        stage('Install Requirements'){
            steps{
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing test stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 hello.py
                python3 hello.py --name=Hamza
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
