pipeline {
    // agent any
    agent {label 'ec3'}

    
    stages {
        stage('build') {
            steps {
                sh 'sudo docker build . -t omarquraah/nodejs_app_image:v1'
            }
        }        
        stage('push') {
            steps {
               withCredentials([usernamePassword(credentialsId: 'docker_hub', passwordVariable: 'pass', usernameVariable: 'usname')]) {
                   sh 'sudo docker login -u ${usname} -p ${pass} '
                   sh 'sudo docker push omarquraah/nodejs_app_image:v1'
               }
            }
        }
        stage('deployment') {
            steps {
                   sh 'sudo docker run -d --name myapp -p 3000:3000 \
                   -e RDS_HOSTNAME="terraform-20211023234908840400000001.ceyp3zenoqrp.us-east-1.rds.amazonaws.com" \
                   -e RDS_USERNAME=ubuntu \
                   -e RDS_PASSWORD=dalida2021  \
                   -e RDS_PORT=5000 \
                   -e REDIS_HOSTNAME="myecash.hz1yrk.0001.use1.cache.amazonaws.com"  \
                   -e REDIS_PORT="6379" \
                   omarquraah/nodejs_app_image:v1'
            }
        } 
        
    }
}
