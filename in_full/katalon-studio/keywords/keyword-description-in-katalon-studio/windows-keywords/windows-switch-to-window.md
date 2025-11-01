---
title: "[Windows] Switch To Window"
---

## Description

Find and attach the opening application window that describes by the given windows object to the working WindowsDriver session on the current desktop.

This keyword should be used when the main application window has been closed and replaced by another window, the application has multiple working windows (We can switch among these windows), or we already have an opened application and need to switch to without reopening.

Keyword name: `switchToWindow`

## Parameters

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `windowsObject` | `WindowsTestObject` | Yes | An object that describes locator and locator strategy to find the opening application. |
| `flowControl` | `FailureHandling` | Optional | Specify [failure handling](https://docs.katalon.com/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Returns

| **Parameter Type** | **Description** |
| --- | --- |
| WindowsDriver | The WindowsDriver after Katalon Studio switches successfully. |
| `StepFailedException` | Throws an error if Katalon Studio could not find any window that matches with the given windows object. |

# Example
```jsx
Windows.switchToWindow(findWindowsObject('Object Repository/Window'))
```