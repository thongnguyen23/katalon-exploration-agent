---
hide_title: true
title: AWS Device Farm integration
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id-e0jl5xnz" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>AWS Device Farm integration

<p xmlns="http://www.w3.org/1999/xhtml" className="p">AWS Device Farm only supports running tests written in frameworks such as Appium, so Katalon users cannot directly execute their mobile tests with AWS Device Farm.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">However, you can execute Katalon tests on the AWS platform by using <span className="ph uicontrol">aws-device-farm-integration</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See this AWS document for further information: <a className="xref j-external-link" href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-appium.html" target="_blank">Working with Appium and AWS Device Farm</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial shows you how to configure your Katalon project, update the <span className="ph uicontrol">aws-device-farm-integration</span> project, and create a test project on AWS Device Farm.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">You can clone or download our sample project and iOS application. This step is optional, you can still use your own project in this tutorial.<ul className="ul"><li className="li">Sample Katalon project: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/aws-device-farm-integration/tree/main/aut/KatalonDemoProject" target="_blank">AWS Device Farm integration</a></li><li className="li">Sample iOS application: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/aws-device-farm-integration/blob/main/aut/Coffee%20Timer.ipa" target="_blank">Coffee Timer.ipa</a> </li><li className="li">For CI/CD pipelines with Jenkins, clone or download <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/ci-samples" target="_blank">CI samples</a> from our repository.</li></ul></div>

## <a id="id_2-1bwxlsws" class="anchor_top_offset"/>Integrate with AWS Device Farm

To run your Katalon project with AWS Device Farm, you have to configure your Katalon projects and make updates in the AWS Device Farm integration.

:::tip requirements
- An active Katalon Runtime Engine license.
- [Apache Maven](https://maven.apache.org/download.cgi) version 3.3.9 onwards.
- Java JDK 8 installed (This version is recommended).
- This integration is supported for Mobile app testing on Android, iOS and Web app testing on Android.
:::

### <a id="task-4343" class="anchor_top_offset"/>Configure your Katalon project

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To configure your Katalon project for mobile testing,  follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In Katalon Studio, open your desired Katalon project.</span><div className="itemgroup info">Prepare       your Katalon test cases and test suites that can successfully run       on your local device. This includes verifying that your device is properly connected, the application under test is accessible, and the test scripts are free of errors.<p className="p">Start your mobile test case with the keyword:         <strong className="ph b">Start Existing Application</strong>. This is because AWS         Device Farm already installs the application on devices under test         before every run. To learn more about this mobile keyword, see <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-start-existing-application">[Mobile]           Start Existing Application</a>.</p></div></li><li className="li step stepexpand"><span className="ph cmd">To change the desired capabilities corresponding to your app,       open <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Desired Capabilities</span> &gt;       <span className="ph uicontrol">Remote</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/KS-AWS-Enable-AWS.png")} width={700} alt="configure desired capabilities" /><br /><br /></div><div className="itemgroup info"><ul className="ul"><li className="li">In <span className="ph uicontrol">Remote server URL</span>, enter the Appium server URL: <code className="ph codeph">http://127.0.0.1:4723/wd/hub </code>.</li><li className="li">In <span className="ph uicontrol">Remote server type</span>, select  <span className="ph uicontrol">Appium</span>.</li><li className="li">In <span className="ph uicontrol">Appium driver</span>, select <span className="ph uicontrol">Android Driver</span> for Android devices or <span className="ph uicontrol">iOS Driver</span> for iOS devices.</li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Select <span className="ph uicontrol">Add</span> to create a desired capability named       <code className="ph codeph">platformName</code> with the value <code className="ph codeph">Android</code> for       Android devices, or <code className="ph codeph">iOS</code> for iOS devices.</span></li><li className="li step stepexpand"><span className="ph cmd">Select <span className="ph uicontrol">Apply         and Close</span>.</span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <p className="p">For Android app testing, we need to add two extra desired           capabilities: <code className="ph codeph">appPackage: [app ID]</code> and           <code className="ph codeph">appActivity: [main activity name]</code>. The main activity           can retrieve after uploading the app to AWS Device Farm.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/android-main-activity.png")} width={300} alt="Android main activity" /><br /><br /></p></div></div></li><li className="li step stepexpand"><span className="ph cmd">Package your Katalon project into a <strong className="ph b">.zip</strong> file.</span></li></ol> 

### <a id="task-1449" class="anchor_top_offset"/>Update aws-device-farm-integration project

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">
  To update the aws-device-farm-integration project with your Katalon project settings and prepare it for AWS Device Farm, follow these steps:
</section>

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps">
  <li className="li step stepexpand">
    <span className="ph cmd">
      Clone or download <code className="ph codeph">aws-device-farm-integration</code> from our 
      <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/aws-device-farm-integration" target="_blank">GitHub repository</a>.
    </span>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      Inside <code className="ph codeph">aws-device-farm-integration</code>, place your Katalon project .zip file in this directory: 
      <code className="ph codeph">src/test/resources</code>.
    </span>
    <div className="itemgroup info">
      <img 
        className="image" 
        src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/zip-demo-project.png")} 
        width={400} 
        alt="zip demo project" 
      /><br /><br />
    </div>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      Open the <code className="ph codeph">config.properties</code> file and change the following variables as per your context:
    </span>
    <div className="itemgroup info">
      <ul className="ul">
        <li className="li">
          <code className="ph codeph">KATALON_VERSION</code>: Katalon Runtime Engine version.
        </li>
        <li className="li">
          <code className="ph codeph">KATALON_PROJECT_PACKAGE_FILE</code>: Your package file.
        </li>
        <li className="li">
          <code className="ph codeph">KATALON_EXECUTE_ARGS</code>: The arguments part of your Katalon run command.
          <ul className="ul">
            <li className="li">
              The <code className="ph codeph">-browserType</code> argument must be set to <code className="ph codeph">"Remote"</code>.
            </li>
            <li className="li">
              The <code className="ph codeph">-reportFolder=$DEVICEFARM_LOG_DIR</code> argument allows us to download the execution report in Files/Customer Artifact of the AWS Device Farm Job.
            </li>
            <li className="li">
              For more arguments, refer to <a className="xref" href="https://docs.katalon.com/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine">Command syntax</a>.
            </li>
          </ul>
        </li>
      </ul>
      <p className="p">For example:</p>
      <div className="p">
        <pre className="pre codeblock">
          <code>
KATALON_VERSION=8.1.0
KATALON_PROJECT_PACKAGE_FILE=KatalonDemoProject.zip
KATALON_EXECUTE_ARGS=-retry=0 -testSuitePath="Test Suites/Regression Tests" -executionProfile=default -browserType=Remote -reportFolder=$DEVICEFARM_LOG_DIR -apiKey=xxxxxxxx
          </code>
        </pre>
      </div>
    </div>
  </li>
  
<li className="li step stepexpand">
    <span className="ph cmd">
      Determine the framework for your test.
    </span>
    <div className="itemgroup info">
      <p className="p">If you want to run with <strong>TestNG java-based framework</strong>:</p>
      <ul className="ul">
        <li className="li">
          Go to <code className="ph codeph">aws-device-farm-integration-main/src/test/java/com/kms/example/aws_ios/test/TestIos.java</code>
        </li>
        <li className="li">Enable the line <code className="ph codeph">import org.testng.annotations.Test;</code></li>
        <li className="li">Then comment on the line <code className="ph codeph">import org.junit.Test;</code></li>
      </ul>
      <img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-platform/integration/AWS%20Device%20Farm%20integration/TestNG%20java-based%20framework.png")} width="600" alt="TestNG java-based framework" />
    </div>
    <div className="itemgroup info">
      <p className="p">If you want to run with <strong>JUnit open-source framework</strong>:</p>
      <ul className="ul">
        <li className="li">
          Go to <code className="ph codeph">aws-device-farm-integration-main/src/test/java/com/kms/example/aws_ios/test/TestIos.java</code>
        </li>
        <li className="li">Enable the line <code className="ph codeph">import org.junit.Test;</code></li>
        <li className="li">Then comment on the line <code className="ph codeph">import org.testng.annotations.Test;</code></li>
      </ul>
      <img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-platform/integration/AWS%20Device%20Farm%20integration/JUnit%20open-source%20framework.png")} width="600" alt="JUnit open-source framework" />
    </div>
  </li>

 
  <li className="li step stepexpand">
    <span className="ph cmd">
      Build the <span className="ph uicontrol">aws-device-farm-integration</span>.
    </span>
    <div className="itemgroup info">
      At the folder <code className="ph codeph">aws-device-farm-integration</code>, type this command in the terminal: 
      <code className="ph codeph">mvn clean package -DskipTests=true</code>.
      <p className="p">
        When the build runs successfully, in the <code className="ph codeph">target</code> folder, you will see a .zip file named 
        <code className="ph codeph">zip-with-dependencies.zip</code>.
      </p>
    </div>
    <div className="itemgroup info">
      <img 
        className="image" 
        src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/2-build-project-with-maven.png")} 
        width={500} 
        alt="build project with maven" 
      /><br /><br />
    </div>
  </li>
</ol>

## <a id="task-8427" class="anchor_top_offset"/>Configure a test project on AWS Device Farm

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">After preparing your Katalon Project, sign in to the AWS Console and go to <span className="ph uicontrol">Device Farm</span> &gt; <span className="ph uicontrol">Mobile Device: Projects</span> to create a new project.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-create-test-project.png")} width={700} alt="create test project" /><br /><br /><p className="p">Input your <span className="ph uicontrol">Project Name</span>, then select     <span className="ph uicontrol">Create</span>.</p><p className="p">This section guides you through the steps to configure your     Katalon test project on AWS Device Farm.   </p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Choose between <span className="ph uicontrol">Mobile App</span> and <span className="ph uicontrol">Web         App</span>.</span><div className="itemgroup info"><ul className="ul"><li className="li"><p className="p">For mobile app testing, select <span className="ph uicontrol">Mobile App</span>.             Upload your application under test (.api file for Android or .ipa for iOS). Wait for the             file to upload, then click <span className="ph uicontrol">Next</span>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-upload-mobile-app.png")} width={600} alt="upload mobile app" /><br /><br /></p></li><li className="li"><p className="p">For Web app testing, select <span className="ph uicontrol">Web App</span>. Enter your             run name, then click <span className="ph uicontrol">Next</span>. The             <span className="ph uicontrol">Configure</span> page appears.</p></li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Setup test framework</span> section, do as follows:</span><div className="itemgroup info"><ul className="ul"><li className="li">Select the dropdown button and choose <span className="ph uicontrol">Appium Java JUnit</span>.</li><li className="li"><p className="p">In the <span className="ph uicontrol">Selected File</span> section, upload the             <code className="ph codeph">zip-with-dependencies.zip</code> file.</p></li><li className="li"><p className="p">In the <span className="ph uicontrol">Choose your execution environment</span>,             choose <span className="ph uicontrol">Run your test in a custom environment</span>, then             select               <span className="ph uicontrol">Next</span>.</p></li></ul></div><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-upload-zip-file.png")} width={700} alt="upload zip file" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">Choose a suitable device pool in <span className="ph uicontrol">Select Devices</span>, then select       <span className="ph uicontrol">Next</span>.</span><div className="itemgroup info"><p className="p">The <span className="ph uicontrol">Specify device state</span> page appears. Review         other settings and change when needed, then select         <span className="ph uicontrol">Next</span>.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Review all of the configurations one last time, then select       <span className="ph uicontrol">Confirm and Start Run</span>.</span><div className="itemgroup info">In AWS Console, a new test run is created. Its status is       pending.</div><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-finish-creating-run.png")} width={700} alt="finish creating run" /><br /><br /><p className="p">After the run starts, you can select the test run name and a         specified device to view the test status.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-view-test-run-status.png")} width={700} alt="view test run status" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-test-runs-finish.png")} width={700} alt="test runs finish" /><br /><br /></p><p className="p">After the run finishes, you can download the execution report at         <span className="ph uicontrol">Files</span>/<span className="ph uicontrol">Customer Artifacts</span>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/aws-device-farm-integration/3-download-report.png")} width={700} alt="download report" /><br /><br /></p></div></li></ol> 
