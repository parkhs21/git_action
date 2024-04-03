node('dind') {
    checkout scm

    stage('Build') {
        docker.build('gen_manual')
    }

    stage('Test') {
        sh 'ls -al'
    }
}