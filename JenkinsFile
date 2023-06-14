pipeline {
    agent any
    stages{
        stage("git_repo"){
            steps{
                git "https://github.com/noorwa1/DevOps_Project"
            }
        }
        stage("Build"){

                steps {
                    bat "python rest_app.py"

                }
        }
    }
}
