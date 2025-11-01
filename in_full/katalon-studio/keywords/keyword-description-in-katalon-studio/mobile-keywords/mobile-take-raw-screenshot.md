# [Mobile] Take Raw Screenshot

## Description

An enhanced way to take screenshot faster of the current device screen. This keyword take raw screenshot from a mobile native app.

Keyword name: `Mobile.takeRawScreenshot`

## Parameters

| Parameter     | Parameter Type      | Required     | Description      |
| ------------- | ------------- | ------------- | ------------- |
| fileName | String | Optional      | The absolute path of the saved screenshot image file. If the fileName is not specified, Katalon Studio saves the screenshot with the current timestamp as its name, and under the current report folder location.     |
| flowControl | FailureHandling | Optional      | Specifies the [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop.    |

## Example

You want to verify that the `Mexican` element is correctly displayed, tap on it, and capture raw screenshots before and after the interaction:

```
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile

CustomKeywords.'sample.Common.startApplication'()

Mobile.takeRawScreenshot()

Mobile.verifyElementText(findTestObject('Spy/XCUIElementTypeStaticText - Mexican'), 'Mexican')

Mobile.takeRawScreenshot()

Mobile.tap(findTestObject('XCUIElementTypeStaticText - Mexican'), 0)

Mobile.takeRawScreenshot()

Mobile.closeApplication()
```