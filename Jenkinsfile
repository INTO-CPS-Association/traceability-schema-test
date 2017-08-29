node {

	// Only keep one build
	properties([[$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '5']]])

	stage('Test') {
		checkout scm
		sh 'git submodule update --init'
		sh 'python check.py'
	}
}


