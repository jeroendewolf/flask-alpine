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

    stage "Build"
        sh "docker build -t ${imageName} ."
    stage "Push"
        sh "docker push ${imageName}"
    stage "Deploy"
    sed 's#127.0.0.1:30400/hello-python:$BUILD_TAG#127.0.0.1:30400/hello python:'$BUILD_TAG'#' python-deploy.yaml | kubectl apply -f -
        sh "kubectl create -f python-deploy.yaml"
}
        
