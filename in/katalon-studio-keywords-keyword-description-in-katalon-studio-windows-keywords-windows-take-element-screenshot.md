---
title: "[Windows] Take Element Screenshot"
---

## Description
Captures a screenshot of a specific UI element in the currently active Windows application.

Keyword name: `Windows.takeElementScreenshot`

## Parameters

| Parameter       | Parameter Type | Mandatory     | Description |
|------------|-----|----------------| ----------------|
| fileName   | String  | Optional | Represents a path to save the image file. It can be either an absolute or a relative path. |
| to  | TestObject  | Yes           | Represents the Windows UI element to capture. |
| flowControl | FailureHandling  | Optional   | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

You want to take a screenshot of a specific UI element (`Edit_PasswordBox`)) in a Windows desktop application:

```jsx
Windows.takeElementScreenshot("C:\temp\element_screenshot_02.png", findWindowsObject("Object Repository/WpfApplication/Simple_Controls/Edit_PasswordBox"), STOP_ON_FAILURE)
```