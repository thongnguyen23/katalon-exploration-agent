# [Mobile] Enhanced Scroll To Text

## Description
Scroll to the given text inside a scrollable container represented by a Test Object.

Keyword name: `Mobile.enhancedScrollToText`

## Parameters

| Parameters   | Parameter Type   | Required   | Description   |
|------------|------------|------------|------------|
| to | TestObject | Yes | The scrollable container in which the text should be found |
| text | String | Yes | Text of the element to scroll to. |
| timeout | Integer | Optional | Maximum time (in seconds) to perform the scroll action before throwing an exception. |
| flowControl | FailureHandling | Optional | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example

Scroll to the element which the displayed text is **Settings**:

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling

// Start the application
Mobile.startApplication('path/to/your/app.apk', false)

// Define the scrollable container (e.g., a list or scroll view)
TestObject scrollableList = findTestObject('Object Repository/Mobile/Scrollable_List')

// Scroll to the target text inside the container
Mobile.enhancedScrollToText(
    scrollableList,          // The scrollable container
    'Settings',              // The text to find and scroll to
    20,                      // Timeout (in seconds)
    FailureHandling.STOP_ON_FAILURE // Failure handling option
)

// (Optional) Tap on the found element after scrolling
Mobile.tap(findTestObject('Object Repository/Mobile/Text_Settings'), 10)

// Close the application
Mobile.closeApplication()

```
