pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "siddharthsinghchaudhari"
        DOCKERHUB_PASS = credentials('dockerhub-pass')
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/siddharthsinghchaudhari/kubernetesNSP.git'
            }
        }

        stage('Set Version') {
            steps {
                script {
                    // Use short git commit hash as version
                    VERSION = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    env.VERSION = VERSION
                    echo "Version set to: ${VERSION}"
                }
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                cd backend
                docker build -t ${DOCKERHUB_USER}/simple-backend:${VERSION} .
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                cd frontend
                docker build -t ${DOCKERHUB_USER}/simple-frontend:${VERSION} .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin
                '''
            }
        }

        stage('Push Images') {
            steps {
                sh '''
                docker push ${DOCKERHUB_USER}/simple-backend:${VERSION}
                docker push ${DOCKERHUB_USER}/simple-frontend:${VERSION}
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/backend backend=${DOCKERHUB_USER}/simple-backend:${VERSION}
                kubectl set image deployment/frontend frontend=${DOCKERHUB_USER}/simple-frontend:${VERSION}
                '''
            }
        }

    }
}

 
