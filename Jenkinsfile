pipeline{
	agent any
	stages{
		stage("Test"){
		    steps{
		        echo "Running Unit Test"
		        sh "python -m unittest fibo_test"
		    }
		}
	}
	post {
        always {
            echo 'One way or another, I have finished'
//             deleteDir() /* clean up our workspace */
        }
        success {
            echo 'Jenkins Build Succeed'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'Jenkins Build Failed'
        }
        changed {
            echo 'Things were different before...'
        }
    }
}