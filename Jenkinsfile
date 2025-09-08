pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building the Docker image..."
                // The -t flag tags the image with a name and the Jenkins build number for versioning
                sh 'docker build -t feedback-api:$BUILD_NUMBER .'
            }
        }

        stage('Push Docker Image (Placeholder)') {
            steps {
                echo "This stage is a placeholder."
                echo "In a real pipeline, you would log in to a container registry and push the image here."
                /*
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push your-dockerhub-username/feedback-api:$BUILD_NUMBER'
                }
                */
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
