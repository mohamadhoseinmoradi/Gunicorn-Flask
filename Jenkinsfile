pipeline{
    agent any
    parameters {
        string(name: "IMAGE_NAME", description: "IMAGE name to build")
        string(name: "IMAGE_TAG", defaultValue: "latest", description: "image version/tag to build")
    }
    stages{

        stage("Build"){
            steps {
                echo "$params.IMAGE_NAME"
                echo "$params.IMAGE_TAG"
                sh "docker build --file Dockerfile --tag $params.IMAGE_NAME:$params.IMAGE_TAG"
                }
            }
        }
    }
