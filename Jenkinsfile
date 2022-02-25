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
//        password(name: "TEST_PASSWORD", description: "Sample password parameter")


    stages {
        stage("Test") {
            when {
                environment(name: "ENV", value: "testing")
    }

    stages{
        stage ("Docker Login") {
            when {
                environment(name: "ENV", value: "DEV")
            }
            steps {
                sh "docker login"
            }
        }
        stage("Build") {
            steps {
                sh "docker build --file Dockerfile --tag $params.IMAGE_NAME:$params.IMAGE_TAG ."
                }
            }

        stage("Running Tests") {
            steps {
                sh "pytest -v"
            }
        }

        stage("Push Artifacts") {
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
                input messsage: "do you want to continue with deployment?", ok: "Confirm"
            }
        }

        stage("deploy to kubernetes") {
            steps {
                sh "something to be done here"
            }
        }
    }
}