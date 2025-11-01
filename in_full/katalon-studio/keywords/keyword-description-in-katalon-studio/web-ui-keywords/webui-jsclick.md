# [WebUI] JavaScript Click

## Description

Performs a click action on a web element using JavaScript. This method is useful in cases where `WebUI.click()` fails to trigger the expected behavior, typically in mobile web environments or when the element is overlapped, hidden, or not fully interactable through standard WebDriver click actions.

Keyword name: `WebUI.jsClick()`

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Required** |
|--------------|--------------|--------------|--------------|
| to | TestObject | Yes | Represents a web element. |
| flowControl | FailureHandling | Optional | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

In this example, we want to click on the **Make Appointment** button. However, if the button is covered by a loading overlay or another element, we use `WebUI.jsClick()` so it directly triggers the element’s click event via JavaScript, bypassing overlays or UI constraints.

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('https://katalon-demo-cura.herokuapp.com/')

WebUI.click(findTestObject('Object Repository/Page_CURA Healthcare Service/a_We Care About Your Health_btn-make-appointment'))

WebUI.jsClick(findTestObject('Page_CURA Healthcare Service/button_Comment_btn-book-appointment'))

WebUI.setText(findTestObject('Object Repository/Page_CURA Healthcare Service/input_Username_txt-username'), 'John Doe')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_CURA Healthcare Service/input_Password_txt-password'), 'g3/DOGG74jC3Flrr3yH+3D/yKbOqqUNM')

WebUI.click(findTestObject('Object Repository/Page_CURA Healthcare Service/button_Password_btn-login'))

WebUI.click(findTestObject('Object Repository/Page_CURA Healthcare Service/span_Visit Date (Required)_glyphicon glyphi_cada34'))

WebUI.click(findTestObject('Object Repository/Page_CURA Healthcare Service/td_Sa_old day'))

WebUI.click(findTestObject('Object Repository/Page_CURA Healthcare Service/button_Comment_btn-book-appointment'))

WebUI.closeBrowser()
```