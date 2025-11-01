---
title: "[Windows] Take Screenshot"
---

## Description
Captures a screenshot of the currently focused Windows application screen.

Keyword name: `Windows.takeScreenshot`

## Parameters

| Parameter       | Parameter Type | Mandatory     | Description |
|------------|-----|----------------| ----------------|
| fileName   | String  | Optional | Represents a path to the saved image. The path can be absolute path or relative path. |
| flowControl | FailureHandling  | Optional   | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |
| screenshotOptions  | Map  | Optional           | Represents the information to be printed on the captured screenshot. |

The `screenshotOptions` parameter has the following properties:

| Parameter       | Parameter Type | Mandatory     | Description |
|------------|-----|----------------| ----------------|
| Text   | String  | Yes | Determines the information to be printed on the captured screenshot. This string should be limited to 100 characters and must not be null or empty. |
| x | Integer  | Optional   | Number of pixels from the left side of the image. The default is `0`. |
| y  | Integer  | Optional           | Number of pixels from the top of the image. The default is `0`. |
| font   | String  | Optional | Font name. The default is `Arial`. |
| fontSize | Integer  | Optional   | Size of font. The default is `12`, maximum is `50`. |
| fontColor  | String  | Optional           | Hex string of color. Default is "#000000" (black). |
| fontStyle  | FontStyle  | Optional           | Can be `Plain`, `Italic` or `Bold`. Default is `Plain`. |

## Example

You want to take a screenshot of a Windows application in a device:

```jsx
"Start the note pad application"
Windows.startApplication('C:\\Windows\\System32\\notepad.exe')

'Take screenshot of current device screen'
Windows.takeScreenshot("D:\screenshot.png")

"Close note pad application"
Windows.closeApplication()
```