---
hide_title: true
title: '[Mobile] Take Element Screenshot'
---

# [Mobile] Take Element Screenshot


## Description

Take a screenshot of a UI element to send to TestOps Vision. The test engine will scroll to this element first then taking a screenshot.

Keyword name: `Mobile.takeElementScrenshot` 

## Parameters

| Parameter      | Parameter Type      | Required      | Description      |
| ------------- | ------------- | ------------- | ------------- |
| fileName | String | Optional      | Absolute path to the stored image file. `fileName` should contain `.png` as images are stored to the `.png` format. If the file name is not defined, the test engine will generate a random file name.      |
| rect | Rectangle | Yes      | A rectangle defining the position and size of the area to be captured.      |
| ignoredElements | List | Optional      | List of the ignored elements. These elements will be hidden by drawing an overlap color layer. If the test engine failed to hide the element by any problems, this keyword would continue without impacting the result.      |
| hidingColor | Color | Optional      | The color used to draw the overlap layer. If not defined, `Color.GRAY` is used.      |
| flowControl | FailureHandling | Optional      | Specifies the [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop.      |

## Returns

A String representing the path to the captured image. Throw: StepFailedException if the UI element cannot be found or Katalon Studio cannot store the image in the disk.

## Example

You want to capture a screenshot of a specific mobile UI element, highlight it in green, and hide unwanted elements from view:

```
// add import libs first
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
// take element screenshot and store to report folder
Mobile.takeElementScreenshot(RunConfiguration.getReportFolder() + '/element_screenshot.png', findTestObject('App/screenshot_element'), [findTestObject('hide_element_1'), findTestObject('hide_element_2')], Color.GREEN)
```
