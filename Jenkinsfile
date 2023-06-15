pipeline {
    agent any
    stages{
        stage("git_repo"){
            steps{
                git "https://github.com/noorwa1/DevOps_Project"
            }
        }
        stage("run backend server"){
            steps {
                    bat "start /min python rest_app.py"
            }
        }
        stage("run frontend server"){
            steps{
                bat "start /min python web_app.py"
            }
        }

        stage("testing"){
            steps{
                bat "python backend_testing.py"
                bat "python frontend_testing.py"
                bat "python combined_testing.py"
            }
        }
    }
    post{
        success{
            echo "everything went well"
            bat "python clean_environment.py"
        }
        failure{
            echo "the pipeline has failed"
            bat "python clean_environment.py"
        }

    }
    
}

