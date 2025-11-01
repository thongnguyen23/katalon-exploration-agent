---
title: '[WebUI] Set View Port Size'
---

## Description

Set the size of the current window. This will change the outer window dimension and the viewport, synonymous to `window.resizeTo()` in Javascript. The viewport's dimension must be less than the screen's actual dimension.

Keyword name: `setViewPortSize`

:::note
- In Katalon Studio 10.0.0+, `setViewportSize` ensures that the return values of `getViewportWidth` and `getViewportHeight` are consistent with the dimensions set by this keyword.
- However, when using `-window-size` in Desired Capabilities, the returned viewport size may differ, as this capability sets the window size, not the viewport size.
:::

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| width | int | Yes | The target viewport width. |
| height | int | Yes | The target viewport height. |
| flowControl | FailureHandling | Optional | Specify [failure handling](https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

You want to set viewport size (703 x 374) for a web browser:

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
'Open browser and navigate to website katalon.com'
WebUI.openBrowser('https://www.katalon.com/')

'Set viewport size 703x347'
WebUI.setViewPortSize(703, 347)

'Close browser'
WebUI.closeBrowser()
```