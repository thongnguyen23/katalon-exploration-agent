---
title: "Sample BDD (Cucumber) project in Katalon Studio"
---

## Introduction

Behavior-Driven Development (BDD) is a testing methodology that focuses on describing a product's behavior in plain English. Using Cucumber, a popular BDD framework, you can write test cases in Gherkin, a human-readable syntax.

This document provides an overview of the components in a sample BDD (Cucumber) project using Katalon Studio. 

## Open the sample BDD test project
The application under test (AUT) is a React-based Calculator, accessible at: https://katalon-studio-samples.github.io/calculator.

To access the BDD sample project in Katalon Studio:

Navigate to **File > New Sample Project > Sample BDD Cucumber Tests Project**.
![Katalon Studio interface showing the navigation path: File > New Sample Project > Sample BDD Cucumber Tests Project.](https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Open-sample-project.png)

Or, you can download the sample BDD test project from our GitHub repository: [Sample BDD tests](https://github.com/katalon-studio-samples/calculator-bdd-tests).

### Trust dialog on first open

When you open a sample project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

<img alt=" " src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-pop-up/trust-dialog-bdd-test.png" width="500" />

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.
:::note Notes
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::
- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

## Overview of Sample BDD Project Components

### Profiles

In Katalon Studio, the execution profile is used to manage global variables that can be reused across different test cases in the project. The sample project includes a default execution profile that defines a key global variable:

Go to **Profiles** > **default**

![Katalon Studio interface showing the selection of the Profiles tab and the default profile.](https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Execution-profile.png)

The sample project includes a default execution profile that defines a key global variable:



To learn more about execution profile, you can refer to this document: [Execution profile](https://docs.katalon.com/katalon-studio/data-driven-testing/global-variables-and-execution-profile).

### Feature Files

Feature files define the test scenarios using **Gherkin syntax**. They act as a high-level blueprint for what the test is supposed to do. 
To locate the sample feature files in Katalon Studio:

1. Go to Include > features > operations.

2. Double-click any .feature file to open and view its contents.
<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Feature-files.png" alt="Katalon Studio interface showing the list of feature files located in Include > features > operations" width="350"/>


#### Example: Minus.feature

The **Minus.feature** file defines a test scenario for subtraction operations using three Gherkin steps (Given, When, Then):

```jsx
Feature: Minus3

  Scenario Outline: Minus
    Given The Calculator page is loaded successfully
    When <firstOperand> minus <secondOperand>
    Then I get the result <result>

    Examples: 
      | firstOperand | secondOperand | result |
      | 10           | 20            | -10    |
      | 123          | 456           | -333   |
```

#### Step definitions
Step definitions connect Gherkin steps to executable code, acting as the bridge between written scenarios and the actual test logic. Each step definition is a method that uses either a **regular expression** or a **Cucumber expression** (See the code snippet in Step 2 for examples of both) to map to specific Gherkin steps.


In this sample project, step definitions are organized into two separate packages located under Include > scripts > groovy:

1. Common Package: Contains `Common.groovy`, which defines shared **Given** and **Then** steps for all feature files.

<img src="https://docs.katalon.com/d3227e60-51f3-11ee-bc71-0242c7a41fd4/KS-BDD-Common-step-definitions.png" alt="Katalon Studio interface showing where Common.groovy file is located (Include > scripts > groovy > common)" width="300"/>

2. Operations Package: Contains four step definition files for Minus (-), Plus (+), Divide (÷), and Multiply (x), which define When steps for their corresponding feature files.
For example, the Minus.groovy file defines the When step in the Minus.feature file:
<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-operations-step-definitions.png" alt="Katalon Studio interface showing where all feature files are located (Include > scripts > groovy > operations)" width="300"/>


```jsx
//All the required packages
class Minus 

	//Regular expression
	@When("(\\\\d+) minus (\\\\d+)")
	def minus(long firstOperand, long secondOperand) {
		WebUI.callTestCase(findTestCase("Test Cases/common/Minus number"), 
		[ ('firstOperand') : firstOperand, ('secondOperand') : secondOperand ], 
		FailureHandling.STOP_ON_FAILURE)

	//Or, Cucumber expression
	@When("{long} minus {long}")
	def minus(long firstOperand, long secondOperand) {
		WebUI.callTestCase(findTestCase("Test Cases/common/Minus number"), 
		[ ('firstOperand') : firstOperand, ('secondOperand') : secondOperand ], 
		FailureHandling.STOP_ON_FAILURE)
	}
}
```

#### Executing a Feature File
In Katalon Studio, you can execute feature files directly without linking them to specific test cases, allowing for quick validation of behavior.

To execute a feature file:

1. Open the Test Explorer panel.

2. Navigate to Include > features > operations.

3. Right-click on the desired feature file (e.g., Minus.feature).

4. Select Run Feature File from the context menu.

### Custom Keywords

Custom keywords in Katalon Studio allow you to create reusable actions for your test cases.

In this sample project, the `ClickNumber.clickNumber` keyword is designed to handle number input efficiently. It converts a given number into an integer and inputs it into the React Calculator.

To view the custom keyword, go to **Keywords > sample > ClickNumber.groovy** in the Test Explorer panel.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Custom-keyword.png" alt="drawing" width="300"/>


### Test Listeners (Test Hooks)

Test listeners (test hooks) are test steps created to define events before/after a test case/test suite.

To view the test listeners in this project, in the **Test Explorer** panel, go to the **Test Listeners** folder. We created two test listeners:

- `TestListener`: This test listener opens Katalon Helper before every test suite execution.

- `Listener`: This test listener closes the browser after every test case execution.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Test-listeners.png" alt="drawing" width="300"/>


### Test Case

Test case files, similar to feature files, perform mathematical operations using the React Calculator. They execute the steps defined in their corresponding feature files and validate the results.

To view test cases in this sample project:

1. Open the Test Explorer panel.

2. Navigate to **Test Cases** > **operations**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-operations-test-cases.png" alt="drawing" width="300"/>

The script below illustrates how a test case executes its corresponding feature file (e.g., linking `Minus Test Case` to `Minus Feature File`):

```jsx
//All the required Java packages 

CucumberKW.runFeatureFile('Include/features/operations/Minus.feature')
```
### Test Suite

A Test Suite groups multiple test cases for efficient execution, so that related tests run together and generate consolidated reports for analysis.

Note: Test suites cannot execute feature files directly; you must create linked test cases first.

To view the sample test suite, navigate to **Test Suite > Verify Operations** in the Test Explorer panel.

![A screenshot of the Verify Operations test suite](https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-test-suite.png)

#### Execute selected test cases or test suites
To execute a test case or a test suite in the sample project:

1. Select the test case/test suite you want to execute.

2. Click Run or press `Ctrl + Shift + A` (`macOS: Cmd+Shift+A`). You can choose different browsers to execute your test in the dropdown list next to Run.
<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Execution.png" alt="drawing" width="200"/>

3. View the test result in the **Log Viewer** tab.

![View test result in Log Viewer](https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/BDD-sample-prj/KS-BDD-Log-viewer.png)
## View BDD reports in Katalon Studio

Katalon Studio generates Cucumber Reports after executing a test suite, allowing you to review each test's status—whether they passed, failed, encountered errors, or remain incomplete.
1. To view your reports in different formats (HTML, CSV, XML):
2. In the Test Explorer panel, right-click on your desired report folder.
Select **Open Containing Folder** from the context menu and navigate to the cucumber_report folder for HTML, CSV, or XML reports.
3. An HTML report will look like this: