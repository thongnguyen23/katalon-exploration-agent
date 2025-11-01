---
title: '[WebUI] Set Encrypted Text'
---

## Description

Set encrypted text into an input field. It also clears the previous value of the input field. To encrypt raw text, follow the instructions below:

- In Manual mode **-** The pop up dialog has been shown when calling keyword `Set Encrypted Text`. Input raw text and select insert.
- In Script mode - Go to **Help** > **Encrypt Text**, input raw text to encrypt. Next, copy and paste encrypted text into the test scripts.

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| to | TestObject | Yes | Represents a web element. |
| text | String | Yes | The encrypted text. |
| flowControl | FailureHandling | Optional | Specify [failure handling](https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

Set the encrypted text to `txt_Password` of a login form:

```jsx
'Open browser and navigate to AUT'
WebUI.openBrowser('http://demoaut.katalon.com/profile.php#login')

'Input username'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), 'John Doe')

'Input password'
WebUI.setEncryptedText(findTestObject('Page_Login/txt_Password'), 'g3/DOGG74jC3Flrr3yH+3D/yKbOqqUNM')

'Click on "Login" button'
WebUI.click(findTestObject('Page_Login/btn_Login'))

'Close browser'
WebUI.closeBrowser()
```