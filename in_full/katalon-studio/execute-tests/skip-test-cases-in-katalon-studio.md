---
hide_title: true
title: Skip test cases in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Skip test cases in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this article, we demonstrate how to skip test cases in a test   suite by adding a test listener with the   <code className="ph codeph">TestCaseContext.skipThisTestCase()</code> method. To learn   more about the usage of test listeners, see <a className="xref" href="/katalon-studio/create-test-cases/test-fixtures-and-test-listeners-test-hooks-in-katalon-studio#concept-7786">Test Listeners (Test Hooks)</a>.</p> 

## <a id="task-2819" class="anchor_top_offset"/>Skip test cases in a test suite execution

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To skip test cases in a test suite execution, do as follows:</section> 

1. In the **Test Explorer** panel, right-click on **Test Listeners**. Select **New** > **New Test Listener**.
    
    <img src="https://docs.katalon.com/be46a740-64ab-11ed-a602-0242cfbc79b5/ks-new-test-listeners.png" alt="create test listener ks instructions" width="600" /> 
    
    A **New Test Listener** dialog opens.
    
2. Enter the name of the test listener, for example: `SkipTest`. Select **Generate sample Before Test Case method**, then click **OK**.
    
    <img src="https://docs.katalon.com/be351b10-64ab-11ed-a602-0242cfbc79b5/ks-new-test-listener.png" alt="create test listener config" width="600" />
    Katalon Studio generates a sample template with the necessary annotations, libraries and supported functions as below:
    ```jsx
    import internal.GlobalVariable as GlobalVariable
    
    import com.kms.katalon.core.annotation.BeforeTestCase
    import com.kms.katalon.core.annotation.BeforeTestSuite
    import com.kms.katalon.core.annotation.AfterTestCase
    import com.kms.katalon.core.annotation.AfterTestSuite
    import com.kms.katalon.core.context.TestCaseContext
    import com.kms.katalon.core.context.TestSuiteContext
    
    class SkipTest {
        /**
         * Executes before every test case starts.
         * @param testCaseContext related information of the executed test case.
         */
        @BeforeTestCase
        def sampleBeforeTestCase(TestCaseContext testCaseContext) {
        println testCaseContext.getTestCaseId()
        println testCaseContext.getTestCaseVariables()
    }
    
    ```
    
3. Use the `TestCaseContext.skipThisTestCase()` method to skip test cases. See also: [skipThisTestCase()](https://api-docs.katalon.com/com/kms/katalon/core/context/TestCaseContext.html#skipThisTestCase()).
    
    Inside the `SkipTest` Test Listener, copy and paste the following code under the generated sample template.
    
    ```jsx
    // To check for the desired condition and skip the test case if true.
    if(inputyourconditionhere)
    {   testCaseContext.skipThisTestCase()
    }
    
    ```
    For example, we want to skip the Test Case named: "Log in 1" in a test suite. We input the following sample code in the **SkipTest** Listener:

    ```jsx
    class SkipTest {
        /**
         * Executes before every test case starts.
         * @param testCaseContext related information of the executed test case.
         */
        @BeforeTestCase
        def sampleBeforeTestCase(TestCaseContext testCaseContext) {
        println testCaseContext.getTestCaseId()
        println testCaseContext.getTestCaseVariables()
        if ((testCaseContext.getTestCaseId()) == "Test Cases/Log in 1")
            {   testCaseContext.skipThisTestCase()
            }
    }
    
    ```
    
4. Save your test listener.
5. Open and execute a test suite.

<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Check the results in the <span className="ph uicontrol">Results</span> tab to see the final status of your   tests. For the example above, Katalon   successfully skips the test case named: "Log in 1".<p className="p">     <img className="image" src={useBaseUrl("/be1c14d0-64ab-11ed-a602-0242cfbc79b5/ks-skip-log-in-1.png")} /></p></section> 
