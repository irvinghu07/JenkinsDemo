pipeline{
	agent any
	stages{
		stage("Test"){
		    steps{
		        echo "Running Unit Test"
		        sh "python -m unittest fibo_test"
		    }
		}
		stage("Deploy"){
		    steps{
		        echo "Deploying Server"
		        sh "python app.py 8888"
		    }
		}
	}
	post {
        always {
            echo 'One way or another, I have finished'
//             deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }
}