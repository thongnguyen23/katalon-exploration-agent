---
title: '[WebUI] Scroll From Viewport Offset'
---

:::caution Prerequisites
This keyword is available from Katalon Studio version **10.0.0+**.
:::

## Description

Scroll from a position within the current viewport with a given offset(x, y), deltaX, and deltaY.

If the offset from the upper left corner of the viewport falls outside of the screen, it will result in an exception.

Keyword name: `scrollFromViewportOffset`

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| viewportOffsetX | int | Yes | Specify the x offset value of the current viewport to start scrolling from. Negative values represent left. |
| viewportOffsetY | int | Yes | Specify the y offset value of the current viewport to start scrolling from. Negative values represent up. |
| deltaX | int | Yes | Specify the delta x value for how much to scroll in the right direction. Negative values represent left. |
| deltaY | int | Yes | Specify the delta y value for how much to scroll in the down direction. Negative values represent up. |
| flowControl | FailureHandling | Optional | Specify [failure handling](https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

You want to scroll from an offset of (50, 60) and scroll by (100, 150):

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

'Scroll from the offset (50, 60) by (100, 150)'
WebUI.scrollFromViewportOffset(50, 60, 100, 150)

'Close browser'
WebUI.closeBrowser()
```