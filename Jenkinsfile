node('code_to_manual') {
    checkout scm

    stage('Build') {
        docker.build('gen_manual')
    }

    stage('Test') {
        sh 'ls -al'
    }
}