# Docker with Jenkins CI/CD

Jenkins is one of the most flexible automation servers, and it works great with Docker.

## 1. Jenkins in Docker
It's often easiest to run Jenkins itself as a container.
```bash
docker run -p 8080:8080 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

## 2. Docker in Jenkins (DinD)
To build images inside a Jenkins pipeline, you can:
- Mount the host's `/var/run/docker.sock` into the Jenkins container.
- Use the **Docker Pipeline** plugin.

## 3. Jenkinsfile Example
```groovy
pipeline {
    agent { docker { image 'mcr.microsoft.com/dotnet/sdk:8.0' } }
    stages {
        stage('Build') {
            steps {
                sh 'dotnet build'
            }
        }
    }
}
```

---
*Back to **[CI/CD Integration](docker-cicd-integration.md)**.*
