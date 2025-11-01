---
hide_title: true
title: Global variables and Execution profile
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Global variables and Execution profile

Global variables are pre-defined values that are accessible across all test cases, test objects, web service objects, and email configurations in a project. They are used to execute test scripts in multiple and different environments.

For example, in a test case, you can use global variables to input data for keywords in Manual view (see highlighted in blue), or to input parameters when binding data for test execution (see highlighted in red).

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/data-binding-global-varaiable.png")} width={700} alt="Global variables example" />

In Katalon Studio, global variables are defined in execution profiles to configure the testing environment in terms of data and behaviors.

This document shows you how to work with global variables and execution profiles in Katalon Studio.

## Create a profile

The following guide shows you how to create a profile to add global variables.

You can create execution profiles to manage global variables based on specific testing purposes.

1. In the **Tests Explorer** tab, right-click on **Profiles > New > Execution Profile**.

    <img className="image" width={400} src={useBaseUrl("/32400260-7f8f-11ed-998d-0242cfbc79b5/ks-855-exe-profile.png")} />

    Enter a name for the profile in the **New Execution Profile** dialog.

2. You need to define the profile content by adding global variables and values.

    In the profile manual view, click **Add** and double-click on the value fields for **Name**, **Value Type**, **Value**, and **Description** to enter your variables and values.

    ![Add a global variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_Profile_add_variable.png)

    In some fields, you need to click and select the parameter from the dropdown list.

    ![Select variable parameter from dropdown](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Global_variables_select_type_from_dropdown.png)

You have created a new execution profile with your global variables.

## View a profile

Execution profile is provided with **Manual** view and **Script** view.

### Manual view

Here's an example of a profile in **Manual** view:

![Execution profile in Manual view](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Execution_profile_Manual_view.png)

You can sort the variables by variable name (**Name** column) and protected variable (**Protected** column). Click on the header column to activate the sort feature:

![Sort variables by variable name](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Execution_profile_sort_by_Name.png)

![Sort variables by protected variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Execution_profile_sort_by_Protected_variable.png)

### Script view

In **Script** view, an XML editor is available for adding variables via script. To ensure consistency in testing different environments, you can copy and paste the list of global variables from one profile to another.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/profile-script-view.png")} width={500} />

To ensure consistency in testing different environments, you can copy and paste the list of global variables from one profile in Script view to another.

:::tip
An option is right-click on a Profile and select **Copy**, then right-click and select **Paste** to create a duplicate Profile with the copied global variables.

<p><img src="https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_copy_profile_with_global_variables.png" alt="Copy global variables from a Profile" width="600"/></p>

<p>The Tests Explorer menu will display indicators (red dots) about the latest changes made to highlight the issue.</p>

<img src="https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_paste_global_variables_create_new_profile.png" alt="Paste and create a duplicate Profile" width="600"/>
:::

## Enable protected variable option

Starting Katalon Studio 10.2.0 and later, you can now mask the value of a variable by marking it as a protected variable. Here are two key use cases for doing so:

- **Prevent data exposure in shared projects**: Masking ensures that sensitive values—such as credentials or API keys—are not stored in plain text within your project files. This is especially important when collaborating in teams or working with projects stored in version control systems (e.g., GitHub), where unintentional data leaks can occur.
- **Securely share logs and reports**: When a variable is protected, its value is automatically masked in execution logs and test reports (HTML, PDF, CSV). This allows you to share test artifacts with stakeholders or external teams without exposing confidential information.
    
To mask the value of your variable, check the box on the **Protected** field on the far right as shown below.

![Enable Protected variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Global_variables_enable_Protected_value.png)

:::note
When you mark a global variable as protected, its value is securely stored locally on your machine—outside of the project files. This design ensures that sensitive data is not included when the project is shared or uploaded to a remote repository.

However, if you open the project on another machine (e.g., by cloning it from a Git repo or transferring it to a teammate), the values of protected global variables will appear empty. You will need to manually re-enter these values before running your tests.

Failure to do so may cause test executions to fail due to missing variable data.
:::

In Script view, the protected value will look like this:

```
<GlobalVariableEntity>
    <description></description>
    <initValue>''</initValue>
    <name>G_Password</name>
    <protected>true</protected>
    <valueType>STRING</valueType>
</GlobalVariableEntity>
```
Here is an example of an HTML test report with protected value:

![HTML test report with protected variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/KS_masked_variable_HTML_report.png)

You can click the eye icon to toggle reveal mode and view or edit the value of a protected variable.

![Edit value of global variable](https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Global_variables_edit_value.png)

To disable protection and expose the variable's value, uncheck the **Protected** checkbox. A confirmation dialog will appear to ensure you intend to make the value visible.

<img src="https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/Global_variables_disable_Protected_value.png" alt="Uncheck protected variable" width="700"/>

## Use global variables in test execution

By selecting an execution profile, you can define global variables for executing a test case, test suite, and test suite collection in different scenarios. Katalon Studio uses the **default** profile by default as indicated on the main toolbar.

### In test case and test suite

Select your desired profile from the main toolbar. This setting applies to all test cases and test suites within your project.

In a test suite, you can only select one (1) specific profile to apply to all test cases in that test suite. For example, in this test suite, you can execute three (3) test cases using the default profile at a time.

<img xmlns="http://www.w3.org/1999/xhtml" className="image" width={700} src={useBaseUrl("/36670640-9d75-11ee-b8c3-0242c7a41fd4/KS-Test_Suite.png")} alt="global variables in test suite" /> 

### In test suite collection

In a test suite collection, you can assign which profile to apply to each test suite in the **Profile** column.

<img xmlns="http://www.w3.org/1999/xhtml" className="image" width={700} src={useBaseUrl("/367d9b80-9d75-11ee-b8c3-0242c7a41fd4/KS-Test_Suite_Collection.png")} alt="Test suite collection editor" /> 

### Scope of global variables

The scope of Global variables is applied in a test suite collection (TSC).

Katalon Studio defines global variables in an execution profile. In a test suite collection, you can assign different profiles to each test suite. During the runtime, modifying the value of global variables in one test suite will not impact the values of global variables in other test suites within the TSC.

You can find "Test Suites/New Test Suite (1)" is listed twice in the following screenshot. The first one uses "default," and the second one has "stagging". Any changes made in profile "default" will not impact profile "stagging". These two test suites run independently without affecting each other. This association confirms **Global variables and Profile are Test Suite scoped**.

<img src="https://tw-cdn.katalon.com/katalon-studio/data-driven-testing/test-suite-scoped.png" alt="Test Suite Collection scoped" width="600"/>

### For command-line interface (Katalon Runtime Engine)

Select your desired profile in the **Profile** option of Command Builder. You can also manually change the `executionProfile` argument in the generated command.

<img xmlns="http://www.w3.org/1999/xhtml" className="image" width={600} src={useBaseUrl("/3238af60-7f8f-11ed-998d-0242cfbc79b5/ks-855-console-profile.png")} alt="console profile" />

### In test object

To use a global variable in a test object, enter the syntax `${GlobalVariable.name}` in the supported selection methods.

For example:

- In the **HTTP Body** of an API test object:

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/http-body.png")} width={600} />

- In the **Selected Locator** of a WebUI test object:

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/web-ui-test-object.png")} width={600} />

- In a Web service request path:

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/requested-url.png")} width={600} />

### Use escaping and special characters

To use a special character like `$` or `\` as a regular one in any place that calls global variables, prepend it with a backslash: `\` (the so-called escape character).

```
{
   "productName": ${GlobalVariable.productName},
   "unit": "\\bottle\",
   "quantity": 50,
   "discount": ${ if (productName == "wine") { return 30 } else { return 0}}
   "note": "Currency unit of ${GlobalVariable.productName} is \$."

}
```

- Without `\`: `note: Currency unit of ${GlobalVariable.productName} is $.`
- With `\`: `note: Currency unit of wine is $.` 

### Override protected global variable during runtime

Starting Katalon Studio 10.2.0 and later, you can now override protected global variables at runtime using command-line arguments, providing a secure and flexible way to manage sensitive data during test execution. This feature is especially useful for dynamically injecting credentials or environment-specific values without exposing them in logs or reports. By using the appropriate prefix, users can control both visibility and behavior while ensuring compliance with data protection standards.

Refer to the following table for guidance on using override command-line arguments:

| Prefix used | Use Case | Result | Notes |
| ------------ | ------------- | ------------- | ------------- |
| `g_` for unprotected | Override unprotected variable | Variable is overwritten; value will be shown in the log. | Same behavior as in versions 9.7.3 and 10.0.0 |
| `p`_ for protected | Override protected variable | Variable is overwritten; value will not be shown in the log. | Used for secure overrides of protected values. |
| `g_` for protected | Override protected variable using `g_` | Variable is overwritten; value will not be shown, but a warning is logged. | Behaves like `p_`, but logs: `Using g_ for protected variables (array of protected variables), continuing as protected`. |
| `p_` for unprotected | Override unprotected variable using `p_` | Variable is overwritten; value will not be shown, and a warning is logged | Behaves like `p_` for protected variables, with log: `Using p_ for unprotected variables (array of unprotected variables using p), continuing as protected`. |

## Set default profile at project level

:::note
From Katalon Studio v7.4.2, you can set a default profile at the project level.
:::

A default profile is where you store commonly used global variables. Other profiles can either inherit or override the global variables stored in the default one.

You may have multiple profiles for executing your tests, for instance, `staging` and `production` profiles. It would be convenient to set a profile as your default one in every execution of a project.

Right-click on your desired execution profile and select Set as **default Execution Profile**.

<p><img className="image" width={300} src={useBaseUrl("/122c9b30-f552-11ed-878a-0242c7a41fd4/ks-865-set-default-execution-profile.png")} /></p>

The selected profile becomes a default execution profile for test case, test suite, and test suite collection in that project.

<img className="image" width={600} src={useBaseUrl("/11b45df0-f552-11ed-878a-0242c7a41fd4/ks-865-TSC-default-profile.png")} />

The setting is also applied to Command Builder for Katalon Runtime Engine.

<img className="image" width={500} src={useBaseUrl("/02218cf0-f552-11ed-878a-0242c7a41fd4/kre-865-default-profile.png")} />

## Inherit profile

Profile inheritance reduces your effort spent on modification and recreation of the same global variables in derived profiles. Suppose Katalon Studio does not find variables used in the test within the designated profile (any profiles but default). In that case, it will look into the default profile and use its variables to execute the test.

Commonly used global variables should be stored in the **default** profile. The following examples illustrate how the profile inheritance feature works.

- Given the following test case:

    <img className="image" width={600} src={useBaseUrl("/040ae660-f552-11ed-878a-0242c7a41fd4/inherit-sample.png")} />

- Execution default profile in use:

    <img className="image" width={600} src={useBaseUrl("/10fe7b70-f552-11ed-878a-0242c7a41fd4/inherit-default-profile.png")} />

    The result is shown as below:

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/inherit-console-default.png")} width={600} />

- Execute staging and production profile with the given test case:

    When executing the staging and production profiles, the **name**, **serverURL**, and **credential** variables are overridden (highlighted in red), while the **usage** and **reference** variables are inherited (highlighted in blue) from the global variables in the default profile.

    - Staging profile:

        <img className="image" width={600} src={useBaseUrl("/0faddf90-f552-11ed-878a-0242c7a41fd4/inherit-stagging-profile.png")} />

        The result is shown as below:

        <img className="image" width={600} src={useBaseUrl("/0e94f580-f552-11ed-878a-0242c7a41fd4/inherit-console-stagging.png")} />

    - Production profile:

        <img className="image" width={600} src={useBaseUrl("/014bed70-f552-11ed-878a-0242c7a41fd4/inherit-production-profile.png")} />

        The result is shown as below:

        <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-profile-v54/inherit-console-production.png")} width={600} />
