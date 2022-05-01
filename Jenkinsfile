pipeline{
    environment {
        imagename = "8285/flask_todo"
        containername = "flask_todo"
        registryCredential = 'docker-hub'
        dockerImage = ''
    }
    agent any
    stages{
        stage("Building Image"){
            steps{
                echo "========Building Image========"
                sh "cd web"
                script {
                    dockerImage = docker.build(imagename)
                }
                sh "cd .."
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
        stage("Pushing Image"){
            steps{
                echo "========Pushing Image========"
                script {
                    docker.withRegistry( "https://registry.hub.docker.com", registryCredential ) {
                    // dockerImage.push("$BUILD_NUMBER")
                    dockerImage.push('latest')
                }
                }
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
        stage("Deploying"){
            steps{
                echo "========Deploying========"
                sh 'docker stop $containername || true && docker rm $containername || true'
                sh 'docker-compose up -d'
                sh 'docker image prune -f'
            }
            // post{
            //     always{
            //         echo "========always========"
            //     }
            //     success{
            //         echo "========A executed successfully========"
            //     }
            //     failure{
            //         echo "========A execution failed========"
            //     }
            // }
        }
    }
    // post{
    //     always{
    //         echo "========always========"
    //     }
    //     success{
    //         echo "========pipeline executed successfully ========"
    //     }
    //     failure{
    //         echo "========pipeline execution failed========"
    //     }
    // }
}