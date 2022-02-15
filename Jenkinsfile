pipeline{
    agent{
        label any
    }
    stages{
        stage("SCM"){
            steps{
                git(
                    url: "",
                    credentialsId: ""
                )
            }
        }
        stage("Build"){
            steps{
                script {
                    def image = docker.build("app:$BUILD_TAG")
                }
            }
        }
        stage("Test")
            steps{
                sh "coverage run -m pytest --junitxml=junit.xml"
                sh "coverage html"
                sh "coverage xml"
                junit "junit.xml"
                cobertura (coberturaReportFile: "coverage.xml")
                publishHTML(
                    allowmissing: false,
                    alwaysLinkToLastBuild: false,
                    keepAll: true,
                    reportName: "coverage",
                    reportDir: "htmlcov",
                    reportFiles: "index.html"
                )
            }
        stage("release")
            steps{
                sh ""
            }
    }

    post{
        always{
            echo "========always========"
        }
    }