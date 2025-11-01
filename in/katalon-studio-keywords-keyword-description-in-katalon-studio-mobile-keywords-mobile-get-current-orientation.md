---
hide_title: true
title: '[Mobile] Get Current Orientation'
---

# [Mobile] Get Current Orientation


## Description

Get the current screen orientation of the device.

Keyword name: `Mobile.getCurrentOrientation` 

## Parameters

| Parameter      | Parameter Type     | Required      | Description    |
| ------------- | ------------- | ------------- | ------------- |
| flowControl | FailureHandling | Optional      | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop.      |

## Returns

| Parameter Type     | Description      |
| ------------- | ------------- |
| String | Current screen orientation (portrait, landscape). |

## Example 

You want to get the current orientation of the device, then store it into "orientation" variable:

```
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

'Start application on current selected android device'
Mobile.startApplication(GlobalVariable.G_AndroidApp, false)

'Get current orientation of selected android device'
orientation = Mobile.getCurrentOrientation()

'Close application on current selected android device'
Mobile.closeApplication()


```