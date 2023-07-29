pipeline {
    
    agent any
    
    stages {
        stage ("clone code"){
            steps {
                echo "cloning the code"
                git url:"https://github.com/LondheShubham153/django-notes-app.git", branch:"main"
            }
            
        }
        stage("build"){
            steps {
                echo "building the image"
                sh "docker build -t notes-app_git ."
               
            }
            
        }
        
        stage ("dockerhub")
        {
            steps {
                echo "pushing the image to dockerhub"
                withCredentials([usernamePassword(credentialsId:"Dockerhub",passwordVariable:"DockerhubPass",usernameVariable:"DockerhubUser")])
                {
                 sh "docker tag notes-app_git ${env.DockerhubUser}/notes-app_git:latest"
                 sh "docker login -u ${env.DockerhubUser} -p ${env.DockerhubPass}"
                 sh "docker push ${env.DockerhubUser}/notes-app_git:latest"
                }
            }
            
        }
        stage ("deploy")
        {
           steps{
                echo "deploying the image"
                // sh "docker run -d -p 8000:8000 rverma11125/notes-app_git:latest"
                sh "docker-compose down && docker-compose up -d"
                
            }
        }
    }
}
