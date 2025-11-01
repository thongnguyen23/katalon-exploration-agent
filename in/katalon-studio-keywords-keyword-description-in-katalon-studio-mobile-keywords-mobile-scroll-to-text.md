---
hide_title: true
title: '[Mobile] Scroll To Text'
---

# [Mobile] Scroll To Text


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Scroll to an element which contains the given text.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">Mobile.scrollToText</code></p> 

## Parameters

| Parameters   | Parameter Type   | Required   | Description   |
|------------|------------|------------|------------|
| text | String | Yes | Text of the element to scroll to |
| flowControl | FailureHandling | Optional | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

## Example 

Scroll to the element which the displayed text is `Xfermodes`:

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase{"\n"}import static com.kms.katalon.core.testdata.TestDataFactory.findTestData{"\n"}import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject{"\n"}import internal.GlobalVariable as GlobalVariable{"\n"}import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration{"\n"}import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile{"\n"}import com.kms.katalon.core.util.internal.PathUtil as PathUtil{"\n"}{"\n"}'Start application on current selected android\'s device'{"\n"}Mobile.startApplication(GlobalVariable.G_AndroidApp, false){"\n"}{"\n"}Mobile.tap(findTestObject('Application/android.widget.TextView - Graphics'), GlobalVariable.G_Timeout){"\n"}{"\n"}'Scroll to element which displayed text is Xfermodes'{"\n"}Mobile.scrollToText('Xfermodes'){"\n"}{"\n"}'Get item\'s label'{"\n"}def itemText = Mobile.getText(findTestObject('Application/Graphics/android.widget.TextView - Xfermodes'), GlobalVariable.G_Timeout){"\n"}{"\n"}'Verify if item\'s label is equal to \"Xfermodes\"'{"\n"}Mobile.verifyEqual(itemText, 'Xfermodes'){"\n"}{"\n"}'Close application on current selected android\'s device'{"\n"}Mobile.closeApplication(){"\n"}</code></pre> 
