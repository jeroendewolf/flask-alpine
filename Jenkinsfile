node {
    stage('Checkout SCM') {
        checkout scm
        sh "git rev-parse --short HEAD > commit-id"
        tag = readFile('commit-id').replace("\n", "").replace("\r", "")
        appname = "flask-alpine:"
        // registryHost name modified to use DockerHub
        registryHost = "wolfjde/" //"127.0.0.1:30400/"
        env.imageName = "${registryHost}${appname}${tag}"
        env.BUILD_TAG=tag
    }

    stage ('Build') {
        sh "docker build -t flask-alpine:1 ."
    }
    // Requires the Docker-pipeline plugin to be installed
    docker.image('flask-alpine:1').inside {
        stage('Test') {
            sh 'pytest --junitxml=reports/results.xml'
            junit 'reports/*.xml' // after this, test results are shown in jenkins
            sh 'coverage run test_app.py'
            sh 'coverage xml -o coverage-reports/coverage-.xml'
            cobertura coberturaReportFile: 'coverage-reports/coverage-.xml'
        }
    }
    // Requires the SonarQube plugin and a scanner to be configured in Jenkins System & Global Tool Configuration
    
    stage('SonarQube') {
        def scannerHome = tool 'scanner';
        withSonarQubeEnv('SonarQube') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=flask-alpine -Dsonar.sources=."
        }
    }
    
    
    stage('Rename image') {
        sh "docker tag flask-alpine:1 ${imageName}"
    }
    
    stage ('Push') {
        // modified to use DockerHub
        docker.withRegistry('', 'dockerhub'){
            sh "docker push ${imageName}"
        }
    }
   
    stage ('Deploy') {
        // modified to use DockerHub
        // sh "kubectl create namespace flask-alpine"
        sh "sed 's#127.0.0.1:30400/flask-alpine:version#wolfjde/flask-alpine:'$BUILD_TAG'#' deployment.yaml | kubectl apply -n default -f -"
        
    }
   
    stage ('Clean') {
        sh "docker rmi -f flask-alpine:1"
        sh "docker rmi -f ${imageName}"
    }
    
}
        
