pipeline{
    agent any
    parameters {
        string(name: "IMAGE", description: "IMAGE name to build")
        string(name: "TAG", defaultValue: "latest", description: "image version/tag to build")
    }
    stages{

        stage("Build"){
            steps {
                echo $params.IMAGE
                echo $params.TAG
                }
            }
        }
    }
