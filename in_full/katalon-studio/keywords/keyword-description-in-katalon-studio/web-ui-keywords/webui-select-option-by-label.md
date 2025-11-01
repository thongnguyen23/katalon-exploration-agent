---
title: '[WebUI] Select Option By Label'
---

## Description

Select the options with the given label (displayed text).

Keyword text: `selectOptionByLabel`

![Select by label example](https://docs.katalon.com/1641f630-803f-11ed-998d-0242cfbc79b5/ks-select-by-label.png)

:::note
- The `selectOptionByLabel` keyword only works with elements using the 'select' tag.
:::

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| to | TestObject | Yes | Represents a web element. |
| labelText | String | Yes | Displayed text of the options to be selected. |
| isRegex | Boolean | Yes | true if the label is a regular expression, otherwise false. |
| flowControl | FailureHandling | Optional | Specify [failure handling](https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

Enter the following script when you want to select the **Hongkong CURA Healthcare Center** option in the **Facility** drop-down list:

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

'Open browser and navigate to demo AUT site'
WebUI.openBrowser('http://demoaut.katalon.com/')

'Click on \'Make Appointment\' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Fill in login information'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), 'John Doe')

WebUI.setText(findTestObject('Page_Login/txt_Password'), 'ThisIsNotAPassword')

'Click on \'Login\' button'
WebUI.click(findTestObject('Page_Login/btn_Login'))

'Select \"Hongkong CURA Healthcare Center\" option'
WebUI.selectOptionByLabel(findTestObject('Page_CuraAppointment/lst_Facility'), 'Hongkong CURA Healthcare Center', false)

'Close Browser'
WebUI.closeBrowser()
```

You may also select the option that contains `Hongkong` with a regular expression. Make the following changes:

```jsx
'Select the option that contains \"Hongkong"\'
WebUI.selectOptionByLabel(findTestObject('Page_CuraAppointment/lst_Facility'), 'Hongkong.*', true)
```

`Hongkong.*` is the sample regular expression. This matches all the strings that contain `Hongkong` , and is followed by zero or more of any character.