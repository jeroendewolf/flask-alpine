node {
    
    stage('Checkout SCM') {
    
        checkout scm
    
        env.DOCKER_API_VERSION="1.23" 
    
        sh "git rev-parse --short HEAD > commit-id"
        tag = readFile('commit-id').replace("\n", "").replace("\r", "")
        appName = "hello-python:"
        registryHost = "127.0.0.1:30400/"
        imageName = "${registryHost}${appName}${tag}"
  
        echo imageName
        echo tag

        env.BUILDIMG=imageName
        env.BUILD_TAG=tag
    }
    
    stage('SonarQube') {
       
        def scannerHome = tool 'scanner';
        
        withSonarQubeEnv('SonarQube') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=PythonWebapp -Dsonar.sources=."
        }
    }
    
    stage ('Build') {
        sh "docker build -t ${imageName} ."
    }
    
    stage('Test') {
        sh "sudo aptitude install flask"
    }
    
    stage ('Push') {
        sh "docker push ${imageName}"
    }
    stage ('Deploy') {
        sh "sed 's#127.0.0.1:30400/hello-python:bla#127.0.0.1:30400/hello-python:'$BUILD_TAG'#' python-deploy.yaml | kubectl apply -f -"
    }
}
        
