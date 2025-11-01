---
title: Jenkins integration overview
---

Jenkins is an open-source automation server. Jenkins provides hundreds of plugins to support building, deploying, and automating any project. You can integrate Jenkins with Katalon Studio and execute Katalon tests with Jenkins. 

## Jenkins integration

There are two possible ways to integrate Katalon with Jenkins:
1. Use Katalon Plugin for Jenkins.
   
   Katalon Plugin for Jenkins helps execute Katalon Studio in Jenkins. Katalon Studio will be automatically downloaded and deployed. To integrate Jenkins with Katalon Studio via Katalon Plugin, you can refer to the following documents:
   - [On Window/MacOS](/katalon-studio/integrations/cicd-integrations/jenkins-integration/use-katalon-plugins-for-jenkins-integration/use-katalon-plugins-for-jenkins-integration-on-windowsmacos) 
   - [On Ubuntu](/katalon-studio/integrations/cicd-integrations/jenkins-integration/use-katalon-plugins-for-jenkins-integration/use-katalon-plugins-for-jenkins-integration-on-ubuntu)

2. Use Katalon Studio Docker Image.
   
   This image contains up-to-date browsers, including Google Chrome, Mozilla Firefox, and Katalon Studio. Hence, when running your Katalon Project with Katalon Studio Docker Image, the pre-installed Katalon Studio and Katalon Runtime Engine in your local machine are not required. Docker Image for Katalon Studio is available at the Docker Hub: [katalonstudio/katalon](https://hub.docker.com/r/katalonstudio/katalon/).
   
   To integrate Jenkins with Katalon Studio via Katalon Docker Image, you can refer to the following documents:

   - [Integrate Jenkins Pipeline (Jenkinsfile) with Katalon Studio Docker Image](/katalon-studio/integrations/cicd-integrations/jenkins-integration/use-katalon-docker-image-for-jenkins-integration/integrate-jenkins-pipeline-jenkinsfile-with-katalon-studio-docker-image)
   - [Integrate Jenkins on Docker hosted in Ubuntu](/katalon-studio/integrations/cicd-integrations/jenkins-integration/use-katalon-docker-image-for-jenkins-integration/integrate-jenkins-on-docker-hosted-in-ubuntu)

## Execute Katalon Studio tests in Jenkins

The following documents are tutorials and tips that can help you   execute Katalon Studio tests after Jenkins integration.
- [Passing feature file and scenario tags at runtime when building with Jenkins](/katalon-studio/integrations/cicd-integrations/jenkins-integration/passing-scenario-tags-at-runtime-when-building-with-jenkins#task-8549)
- [Execute Katalon Studio tests with Jenkins Pipeline Script (Jenkinsfile)](/katalon-studio/integrations/cicd-integrations/jenkins-integration/execute-katalon-studio-tests-with-jenkins-pipeline-script-jenkinsfile)
