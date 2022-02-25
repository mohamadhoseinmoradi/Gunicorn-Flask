pipeline {
    
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: "20"))
        disableConcurrentBuilds()
    }
    
    environment {
        ENV = "DEV"
    }

    parameters {
        string(name: "IMAGE_NAME", description: "IMAGE name to build")
        string(name: "IMAGE_TAG", defaultValue: "latest", description: "image version/tag to build")
    }

    stages {

        stage("Docker Build") {
            steps {
                sh "docker build --file Dockerfile --tag $params.IMAGE_NAME:$params.IMAGE_TAG ."
                }
            }

        stage("Running Tests") {
            steps {
                sh "pytest -v"
            }
        }

        stage ("Docker Login") {
            when {
                environment(name: "ENV", value: "DEV")
            }
            steps {
                withCredentials([usernamePassword(credentialsId: "dockerhub-credentials", usernameVariable: "USERNAME", passwordVariable: "PASSWORD")]) {
                    sh "docker login -u $USERNAME -p $PASSWORD"
                }
            }
        }

        stage("Docker Push Artifacts") {
            steps {
                sh "docker tag $params.IMAGE_NAME:$params.IMAGE_TAG mdmddockergft/$params.IMAGE_NAME:$params.IMAGE_TAG"
                sh "docker push mdmddockergft/$params.IMAGE_NAME:$params.IMAGE_TAG"
            }
        }

         stage("deploy confirmation") {
            options{
                timeout(time: 5, unit: "MINUTES")
            }
            steps {
                input message: "do you want to continue with deployment?", ok: "Confirm"
            }
        }

         stage("deploy to kubernetes") {
            steps {
                sh "helm install app helm/"
            }
        }

    }
}