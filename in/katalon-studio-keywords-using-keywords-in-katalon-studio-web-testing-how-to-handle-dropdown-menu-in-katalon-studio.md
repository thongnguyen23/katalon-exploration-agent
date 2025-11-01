---
hide_title: true
title: How to handle dropdown menu in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_how_handle_drop_down_menu" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to handle dropdown menu in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 


## <a id="id_1" class="anchor_top_offset"/>What is a dropdown?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A dropdown menu (or a dropdown list) is a graphical control element, similar to a list box, that allows users to choose one value from a list. When a dropdown list is inactive, it displays a single value. When activated, it displays a list of values, from which the user may select one. When the user selects a new value, the control reverts to its inactive state, displaying the selected value.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The below image shows the components of a dropdown menu.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <em className="ph i">Index:</em> The index of the option to be selected / deselected.</li><li className="li"> <em className="ph i">Value:</em> The value of the <kbd className="ph userinput">value</kbd> attribute.</li><li className="li"> <em className="ph i">Label:</em> The exactly displayed text of a particular option.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/fb47b770-9ed4-11ed-998d-0242cfbc79b5/Sample_dropdown_html.png")} alt="Sample HTML for dropdown menu" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial shows you how to handle the dropdown menu in common scenarios, using <span className="ph">Katalon Studio</span> built-in keywords.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">For detailed implementation of dropdown handling, you can refer to our sample test project on GitHub: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/katalon-web-automation" target="_blank">katalon-studio-samples/katalon-web-automation</a>.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">The dropdown selection keywords in Katalon Studio are designed to work only with elements using the 'select' tag.</p></li></ul></div></div>

## <a id="id_6" class="anchor_top_offset"/>Select option by index

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">selectOptionByIndex</code> keyword selects the option at the given index. Index always starts from 0. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-select-option-by-index">[WebUI] Select Option By Index</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Example 1</strong>:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we are also verifying that the right option is selected.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Select_by_Index_Example.png")} alt="Sample dropdown with index starting from 0" /><br /><br /></p> 
In Manual View:

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/SelectbyIndex_manual.png" alt="Sample test case with select By Index keyword in Manual view" />

In Script View:
```jsx
'Open browser'
WebUI.openBrowser('file:///C:/Users/User/Desktop/Dropdown.html')
 
'Maximize the Window'
WebUI.maximizeWindow()
 
'Select the dropdown value by Select option by index Method'
WebUI.selectOptionByIndex(findTestObject('dropdown_Month'), 2)
 
'Verifying the Option is Selected by Index option'
WebUI.verifyOptionSelectedByIndex(findTestObject('dropdown_Month'), 2, 60)
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Example 2</strong>:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If we want to select "Feb" to "Apr" from the below combo box, we pass input as value 2-4 and value type as <kbd className="ph userinput">String</kbd>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Select_options_by_passing_Range_value.png")} alt="Sample dropdown menu with multiple options selected" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Input_Dialog_Box.png")} alt="Keyword input &quot;2-4&quot;" /><br /><br /></p> 

## <a id="id_7" class="anchor_top_offset"/>Select option by label

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">selectOptionByLabel</code> keyword selects the option which has the exactly displayed text of a particular option. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-select-option-by-label">[WebUI] Select Option By Label</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Example</strong>: </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If we want to select "Apr" from the dropdown, we pass the exactly visible text from it.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we are also verifying the right option is selected.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/SelectByLabel_Expample.png")} alt="Dropdown option with the label &quot;April&quot; selected" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Select_option_By_label_Manual.png")} alt="Sample test case with keyword &quot;selectOptionByLabel&quot;" /><br /><br /></p> 

In **Script View**:
```jsx
'Open browser'
WebUI.openBrowser('file:///C:/Users/User/Desktop/Dropdown.html')
 
'Maximize the Window'
WebUI.maximizeWindow()
 
'Select the dropdown value by Select option By Label Method'
WebUI.selectOptionByLabel(findTestObject('dropdown_Month'), 'Apr', false)
 
'Verifying the Option is Selected by Label option'
WebUI.verifyOptionSelectedByLabel(findTestObject('dropdown_Month'), 'Apr', false, 60)
 
WebUI.closeBrowser()
```

## <a id="id_8" class="anchor_top_offset"/>Select option by value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">selectOptionByValue</code> keyword selects the option which has value of the <kbd className="ph userinput">value</kbd> attribute. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-select-option-by-value">[WebUI] Select Option By Value</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If we want to select "Mar" from the dropdown, we pass the value as 3 because "Mar" has the value as 3 for <kbd className="ph userinput">Value</kbd> attribute.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we are also verifying that the right option is selected.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/SelectByValue_Exp.png")} alt="Sample dropdown option with the attribute &quot;value=3&quot;" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Select_By_Value_Manual.png")} alt="Sample test case in Manual view with keyword selectOptionByValue" /><br /><br /></p> 

In **Script View**:
```jsx
'Open browser'
WebUI.openBrowser('file:///C:/Users/User/Desktop/Dropdown.html')
 
'Maximize the window'
WebUI.maximizeWindow()
 
'Selecting the month from Select By value method'
WebUI.selectOptionByValue(findTestObject('dropdown_Month'), '3', false)
 
'Verifying the Option is Selected by Value option'
WebUI.verifyOptionSelectedByValue(findTestObject('dropdown_Month'), '3', false, 60) 
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, please refer to <a className="xref" href="/katalon-studio/get-started/sample-projects/webui/webui-create-and-run-web-ui-test-case-using-record-and-playback-in-katalon-studio">Katalon Studio WebUI</a> tutorials.</p> 

## <a id="id_5" class="anchor_top_offset"/>Select all options

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">selectAllOption</code> selects all options from a list. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-select-all-option">[WebUI] Select All Option</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>: <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/SelectAll_Manual.png")} alt="Sample test case with keyword selectAllOption" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Script View</span>:</div>

```jsx
'Launch Browser'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\DropDown\\MultiSelection_dropDown.html')
 
'Maximize the window'
WebUI.maximizeWindow()
 
'Selecting all Options'
WebUI.selectAllOption(findTestObject('comboBox_Role'))
```

## <a id="id_2" class="anchor_top_offset"/>Deselect all options

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">deselectAllOption</code> keyword deselects all the selected items in a combo box. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-deselect-all-option">[WebUI] Deselect All Option</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Multiple_Attribute_Image1.png")} alt="Sample dropdown HTML with multiple=true" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/DeSelectAll_Manual.png")} alt="Sample test case in Manual view with keyword deselectAllOption" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Script View</span>:</div>

```jsx
'Launch Browser'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\DropDown\\MultiSelection_dropDown.html')
 
'Maximize the window'
WebUI.maximizeWindow()
 
'Select all the Options'
WebUI.selectAllOption(findTestObject('comboBox_Role'))
 
'Deselect all the options'
WebUI.deselectAllOption(findTestObject('comboBox_Role'))
 
'Taking the count of number of Selected Options and Storing it in a variable'
NoOfSelectedOptions = WebUI.getNumberOfSelectedOption(findTestObject('comboBox_Role'))
 
'After Deselect verifying the Number of Selected options with Actual result to Expected'
WebUI.verifyEqual(NoOfSelectedOptions, 0)
```

## <a id="id_4" class="anchor_top_offset"/>Get the number of total options

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">getNumberOfTotalOption</code> keyword returns the number of options listed in the combo box. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-get-number-of-total-option">[WebUI] Get Number Of Total Option</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We have a dropdown and want to get the total number of available options in a dropdown then we will use <code className="ph codeph">getNumberOfTotalOption</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Total_Options_Image.png")} alt="Sample dropdown menu with 5 options" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As there are 5 options in the dropdown, the keyword returns the value 5.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Get_Number_of_Total_Options_Manual.png")} alt="Sample test case in Manual view with keyword getNumberOfTotalOption" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Script View</span>:</div>

```jsx
'Launch Browser'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\DropDown\\MultiSelection_dropDown.html')
 
'Maximize the window'
WebUI.maximizeWindow()
 
'Capturing the Number of  Values in the dropdown and storing it in a variable'
TotalOptions = WebUI.getNumberOfTotalOption(findTestObject('comboBox_Role'))
println('No of Roles are :' + TotalOptions)
 
'Verifying the number of Options in the dropdown with Expected result'
WebUI.verifyEqual(TotalOptions, 5)
```

## <a id="id_3" class="anchor_top_offset"/>Get the number of selected options

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">getNumberOfSelectedOption</code> keyword returns the count of options which are being selected in the combo box. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-get-number-of-selected-option">[WebUI] Get Number Of Selected Option</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, in the combo box below the options "Admin" and "HR" are selected. If we want to get the number of selected options, we can use the keyword <code className="ph codeph">getNumberOfTotalOption</code>. In this case, the keyword returns 2.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Get-Number-Of-Selected-Options-Example.png")} alt="Sample dropdown with two options selected" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Manual View</span>:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_handle_drop_down_menu/Get_Number_of_Selected_Option_manual.png")} alt="Sample test case in Manual view with keyword getNumberOfSelectedOption" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Script View</span>:</div>

```jsx
'Launch Browser'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\DropDown\\MultiSelection_dropDown.html')

'Maximize the window'
WebUI.maximizeWindow()

'Select All values available in the dropdown by Select All option'
WebUI.selectAllOption(findTestObject('comboBox_Role'))

'Capturing the Number of selected Values and storing it in a variable'
SelectedItems = WebUI.getNumberOfSelectedOption(findTestObject('comboBox_Role'))
println('No of Selected Roles are ' + SelectedItems)
 
'Verifying the number of Options selected with Expected result'
WebUI.verifyEqual(SelectedItems, 5)
```
