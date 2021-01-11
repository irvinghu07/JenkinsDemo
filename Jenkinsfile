pipeline{
	agent{docker{ image 'Python 3.6.12'}}
	stages{
		stage("build"){
			steps{
				echo "Building"
				sh "python build.py"
			}
		}
	}
}