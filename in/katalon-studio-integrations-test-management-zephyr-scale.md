---
hide_title: true
title: Zephyr Scale
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-9550" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Zephyr Scale

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document will cover a step by step guide on integration of Zephyr Scale Cloud in JIRA with Katalon Automation Platform.</p> 

## <a id="task-5778" class="anchor_top_offset"/>Setup Zephyr Scale in Jira

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">Katalon Studio </p></li><li className="li"><p className="p">Zephyr Scale app in Jira Cloud</p></li></ul></div>
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Generate API Access Tokens</span><div className="itemgroup info">You need to generate an access token to use the API for Zephyr Scale.  Each user interacting with the API will need a token for that instance       of Jira.</div><ol type="a" className="ol substeps"><li className="li substep"><span className="ph cmd">Click your Jira profile icon and select <span className="ph uicontrol">Zephyr Scale API Access Tokens</span>.<img className="image" src={useBaseUrl("/15cd42e0-c310-11ed-a4d3-0242cfbc79b5/Zephyr_scale_API_access_token.png")} alt="Zephyr Scale API access tokens" /></span></li><li className="li substep"><span className="ph cmd">Select <span className="ph uicontrol">Create access token</span>. <img className="image" src={useBaseUrl("/1624ffd0-c310-11ed-a4d3-0242cfbc79b5/Zephyr-_create_access_token.png")} alt="Zephyr - create access token" /></span></li><li className="li substep"><span className="ph cmd">The pop-up <span className="ph uicontrol">Access token successfully created</span> appears. Select <span className="ph uicontrol">Copy</span> to copy the access token.</span></li></ol></li><li className="li step stepexpand"><span className="ph cmd">Now you can get started using the REST API. </span><div className="itemgroup info">The URL for API requests is: <pre className="pre codeblock"><code>https://api.zephyrscale.smartbear.com/v2/{"{"}endpoint{"}"}</code></pre>The authorization we use is based on JWT, so you have to use a bearer token. Add the       <span className="ph uicontrol">Authorization</span> header with the value <code className="ph codeph">Bearer {'{'}token{'}'}</code>.<p className="p">You can  refer to the <a className="xref j-external-link" href="https://support.smartbear.com/zephyr-scale-cloud/api-docs/" target="_blank">API documentation</a> for details on available endpoints and data models.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Create sample Test Case, Test Cycle, Test Plan and link them as  per requirements</span></li></ol> 

## <a id="task-8027" class="anchor_top_offset"/>Setup Katalon project

1. Global Variables setup

    Create the following global variable in your package which will be used in API calls for pushing execution results to Zephyr cloud in Jira from Katalon after execution of test cases.
    
    <img src="https://docs.katalon.com/152dce90-c310-11ed-a4d3-0242cfbc79b5/Zephyr_Katalon_global_variables_setup.png" alt="KS global var" />
    
2. Create Test Case and tag

    Script the test case and give name to test case with prefix as Test Case Key from Zephyr Scale then an underscore followed by Test case name, for example: `<<TestCase Key>>_<<Test case name as per your choice>>` 
    
    Also, you need to tag the test case with linked Test Cycle Keys from Zephyr scale as below.
    
    <img src="https://docs.katalon.com/14ba4c40-c310-11ed-a4d3-0242cfbc79b5/Zephyr_test_case_tag.png" alt="Zephyr test case tag" width="700" />
    
3. Create Web Service Request

    In API you need to provide an end point, set authorization with bearer token generated in the step Generating API Access Tokens above, update that to HTTP Header and the HTTP Body with parameterized global variables which will be replaced with actual value in runtime.
    
    Under the Object repository add a new web service request for API [Create test execution](https://support.smartbear.com/zephyr-scale-cloud/api-docs/#tag/Test-Executions/operation/createTestExecution) -This API will be used to push test results by creating a new execution record for each Test case after execution in Katalon.
    
    <img src="https://docs.katalon.com/15f7ae40-c310-11ed-a4d3-0242cfbc79b5/Zephyr_update_to_HTTP_Header.png" alt="Zephyr update to HTTP header" width="600" /> <br/>
    
    <img src="https://docs.katalon.com/15b96cc0-c310-11ed-a4d3-0242cfbc79b5/Zephyr_update_to_HTTP_body.png" alt="Zephyr_update_to_HTTP_body" width="600" />
    
4. Create TestListener

    Create a new test listener with following methods and code given below. This will call the Execution API after each Test case gets executed and push results to Zephyr Scale.
    
    ```jsx
    << default import statements will be here>>
    class NewTestListener {
    	/**
    	* Executes after every test case ends.
    	* @param testCaseContext related information of the executed test case.
    	*/
    	@AfterTestCase
    	def sampleAfterTestCase(TestCaseContext testCaseContext) {
    		//Get Test Case Key from test case name
    		TestCase testCase = findTestCase(testCaseContext.getTestCaseId())
    		GlobalVariable.g_ZS_TestCaseKey=testCase.getName().split("_")[0]
    		//Set Zephyr Status
    		if (testCaseContext.getTestCaseStatus()=="PASSED")
    			GlobalVariable.g_ZS_StatusName="Pass"
    		else if (testCaseContext.getTestCaseStatus()=="FAILED")
    			GlobalVariable.g_ZS_StatusName="Fail"
    		else
    			GlobalVariable.g_ZS_StatusName="Not Executed"
    		//Call API to Push Result to Zephyr by creating Test case execution
    		WS.sendRequest(findTestObject('Create Execution'))
    	}
    }
    ```
    
5. Install Basic Search for Dynamic Test Suite Plugin.
    You can install [Basic Search For Dynamic Test Suite](https://store.katalon.com/product/2/Basic-Search-For-Dynamic-Test-Suite) by login into the Katalon Store and reload the plugin in Katalon Studio.
    
    <img src="https://docs.katalon.com/14f97820-c310-11ed-a4d3-0242cfbc79b5/KS-reload_plugin.png" alt="KS reload plugin" width="700" />
    
6. Create Dynamic Test Suite and Generate Command for Console Mode
    1. In **Test Explorer** panel, right-click at the **Test Suites** folder > **New** > **Dynamic Test Suite** to create a Dynamic Test Suite.
        
        <img src="https://docs.katalon.com/1585b290-c310-11ed-a4d3-0242cfbc79b5/Katalon_Studio_-_Dynamic_Test_Suite.png" alt="create dynamic test suite" />
        
    2. Select **Generate Command** icon near **Run** icon and select Test Suite and other details.
        
        <img src="https://docs.katalon.com/14e33100-c310-11ed-a4d3-0242cfbc79b5/KS-generate_command.png" alt="KS generate command" width="700" />
        
7. Execute Dynamic Test Suite using Console mode command.

    This command can be configured in Katalon TestOps or in CI tool for triggering execution or can be run on cmd using Katalon Runtime Engine.
    
    ```jsx
    ./katalonc -noSplash -runMode=console
    -projectPath="/Users/rupeshsawant/Katalon Studio/Katalon and
    Zephyr Integration/Katalon and Zephyr Integration.prj"
    -retry=0 -testSuitePath="Test Suites/Zephyr TestCycle Dynamic
    Test Suite" -browserType="Chrome" -executionProfile="default"
    -apiKey="<<Your APi Key>>" -orgID=<<Your Org Id>> --config
    -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY
    -proxy.system.applyToDesiredCapabilities=true
    -webui.autoUpdateDrivers=true
    ```

    You need to append two arguments with the Test Cycle Key value which you want to execute:

    - `testSuiteQuery="tag=(<<Your Test Cycle Key)>>)"`: this argument will be used for filtering test cases linked to test cycle for execution in dynamic test suite.
    - `g_ZS_TestCycleKey="<<Your Test Cycle Key)>>"`: this argument will be used for setting global variable value to selected test cycle which will be required in API calls.

    The command will be updated as follows:
    
    ```jsx
    ./katalonc -noSplash -runMode=console
    -projectPath="/Users/rupeshsawant/Katalon Studio/Katalon and
    Zephyr Integration/Katalon and Zephyr Integration.prj"
    -retry=0 -testSuitePath="Test Suites/Zephyr TestCycle Dynamic
    Test Suite" -browserType="Chrome" -executionProfile="default"
    -apiKey="<<Your APi Key>>" -orgID=<<Your Org Id>> --config
    -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY
    -proxy.system.applyToDesiredCapabilities=true
    -webui.autoUpdateDrivers=true -testSuiteQuery="tag=(<<Your
    Test Cycle Key)>>)" -g_ZS_TestCycleKey="<<Your Test Cycle
    Key)>>"
    ```
    
8. Check test results in Jira Zephyr ScaleResults will be updated in Jira Zephyr scale in respective test cycle and test case with new execution record.
    
    <img src="https://docs.katalon.com/157251a0-c310-11ed-a4d3-0242cfbc79b5/Zephyr_test_results.png" alt="Zephyr test result" />