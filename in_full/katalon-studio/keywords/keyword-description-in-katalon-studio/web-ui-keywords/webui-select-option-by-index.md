---
title: '[WebUI] Select Option By Index'
---

## Description

Select the option by the given index. Index starts from `0`.

Keyword name: `selectOptionByIndex` 

- The `selectOptionByIndex` keyword only works with elements using the `select` tag.

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `to` | `TestObject` | Yes | Represents a web element. |
| `range` | `Object` | Yes | Index range of the options to be selected.<br/><ul><li>0 - index 0</li><li>"1,2" - index 1 and 2</li><li>"0-2" - index 0 to 2 (1,2,3)</li></ul> |
| `flowControl` | `FailureHandling` | Optional | Specify <a href="https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop. |


## Example

1. Enter the following script when you want to select the first option on the **Facility** drop-down list:

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
WebUI.openBrowser('[http://demoaut.katalon.com/](http:http://demoaut.katalon.com/)')

'Click on 'Make Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Fill in login information'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), 'John Doe')

WebUI.setText(findTestObject('Page_Login/txt_Password'), 'ThisIsNotAPassword')

'Click on 'Login' button'
WebUI.click(findTestObject('Page_Login/btn_Login'))

'Select the first option on 'Facility' list'
WebUI.selectOptionByIndex(findTestObject('Page_CuraAppointment/lst_Facility'), '0')

'Close Browser'
WebUI.closeBrowser()
```

2. Enter the following script when you want to select the second and third options on the **Facility** drop-down list:

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
WebUI.openBrowser('[http://demoaut.katalon.com/](http://demoaut.katalon.com/)')

'Click on 'Make Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Fill in login information'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), 'John Doe')

WebUI.setText(findTestObject('Page_Login/txt_Password'), 'ThisIsNotAPassword')

'Click on 'Login' button'
WebUI.click(findTestObject('Page_Login/btn_Login'))

'Select the second and third options on 'Facility' list'
WebUI.selectOptionByIndex(findTestObject('Page_CuraAppointment/lst_Facility'), '1,2')

'Close Browser'
WebUI.closeBrowser()
```

3. Enter the following script when you want to select options 1 to 3 on the **Facility** drop-down list:

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
WebUI.openBrowser('[http://demoaut.katalon.com/](http://demoaut.katalon.com/)')

'Click on 'Make Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Fill in login information'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), 'John Doe')

WebUI.setText(findTestObject('Page_Login/txt_Password'), 'ThisIsNotAPassword')

'Click on 'Login' button'
WebUI.click(findTestObject('Page_Login/btn_Login'))

'Select option 1, 2, 3 on 'Facility' list'
WebUI.selectOptionByIndex(findTestObject('Page_CuraAppointment/lst_Facility'), '0-2')

'Close Browser'
WebUI.closeBrowser()
```