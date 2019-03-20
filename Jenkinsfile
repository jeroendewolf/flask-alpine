node {

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

node {
  stage('SCM') {
    git 'https://github.com/jeroendewolf/pythonwebapp.git'
  }
  stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'scanner';
    withSonarQubeEnv('SonarQube') {
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=PythonWebapp -Dsonar.sources=."
    }
  }
}
    
    stage "Build"
        sh "docker build -t ${imageName} ."
    stage "Push"
        sh "docker push ${imageName}"
    stage "Deploy"
        //sh "kubectl delete -f python-deploy.yaml"
        sh "sed 's#127.0.0.1:30400/hello-python:bla#127.0.0.1:30400/hello-python:'$BUILD_TAG'#' python-deploy.yaml | kubectl apply -f -"
        //sh "kubectl apply -f python-deploy.yaml"
}
        
