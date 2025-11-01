---
hide_title: true
title: Test case variables
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Test case variables

Test case variables are variables defined in a test case. In Katalon Studio, test case variables are defined in the **Variables** tab.

Instead of running test case with hard-coded values, you can create test case variables and dynamically run the test case with different inputs.

## Add test case variables

In this example, we want to pass variables to the following statement:

```
println "${employee} - ${department}"
```
Follow the steps how to add a new test case variable using the statement above:

1. Navigate to **Tests Explorer** and open a test case from the **Test Cases** folder.

2. In the Test Case Editor, navigate and click the **Variables** tab to view the test case variables.

3. To add variable using grid view, click **Add**. 

4. A new row is automatically added to the variable list. 

    Enter your variables and values.

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/1-test-case-variables.png")} />

The result after running the test case with variables will be the same with hard-coded values:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/2-result.png")} /> 

## Add masked test case variables

Follow the steps how to add a new test case variable using the statement above:

1. Navigate to **Tests Explorer** and open a test case from the **Test Cases** folder.

2. In the Test Case Editor, navigate and click the **Variables** tab to view the test case variables.

3. To add variable using grid view, click **Add** and enter your variables and values. 

4. Navigate the test variable row to the right and check the box under the **Masked** column.

    Enter your variables and values. 

    ![Add masked variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_mask_variables.png)

The result after running the test case with masked variables will be the same with hard-coded values, except that the masked variable is hidden in asterisks.

![Test run result with masked variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_test_run_masked_variables.png)

In the example below, the masked variable is shown in the following:

- **Log Viewer**: 
    <img src="https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_masked_variable_log_viewer.png" alt="Masked variable in Log Viewer" width="700"/>

- **Report (HTML)**: 

    ![Masked variable in HTML Report](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_masked_variable_HTML_report.png)


## View and declare variables in Script mode

Switch to Variable (Script Mode) tab, Katalon Studio will display a Script Editor with XML format. 

For example:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/3-variables-script-mode.png")} />

## Call a test case with variables

The following is an example of dynamically calling a test case with a set of values.

1. Open a test case in **Manual** view, then click **Add** and select option **Call Test Case**.

2. The **Test Case Browser** dialog which shows all existing test cases within the project will be displayed. Select the test case to be called and click **OK**.

    In the following example, we call the "Test Case with variables" test case.

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/4-test-case-browser.png")} />

3. A **Call Test Case** step will be added with the selected test case above as its target.

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/KS-830-call-tc-with-variables.png")} alt="call test case with variables" />

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/6-input.png")} />

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/7-map-input.png")} />

The result after running the test case will be displayed as below:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-variables/8-result-after-call-test-case.png")} />
      
### Call Test Case in Script mode

In Script tab, the callTestCase method allows users to make a call to another test case. 

Refer to the following example:

```
WebUI.callTestCase(findTestCase('Data-driven Testing/Test Case with variables'), [('employee') : 'John', ('department') : 'Marketing', ('position') : 'Manager'], FailureHandling.STOP_ON_FAILURE)
```
              
    
