pipeline{
    agent any
    parameters {
        string(name: "IMAGE_NAME", description: "IMAGE name to build")
        string(name: "IMAGE_TAG", defaultValue: "latest", description: "image version/tag to build")
    }
    stages{

        stage("Build"){
            steps {
                sh "docker build --file Dockerfile --tag $params.IMAGE_NAME:$params.IMAGE_TAG"
                }
            }
        }
    }
