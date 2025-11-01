---
hide_title: true
title: Use variables in Web test objects
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_parameterize-web-objects" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use variables in Web test objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can update test object locators dynamically by using either local or global variables. This feature comes in handy in these use cases:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">You want to perform a bulk action on a group of similar elements without defining multiple test objects, such as checking on multiple checkboxes;</li><li className="li">You can only identify an object's locator during runtime because there's a group of similar objects and the chosen one cannot be specified beforehand in test scripts.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports using variables in properties of test objects to handle dynamic objects. Dynamic objects are those that have some particular changes in their properties based on specific business rules. The example below describes how to apply this feature.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add variable to an object locator by replacing the value with the syntax ${'{'}&lt;variable name&gt;{'}'}. The workflow is as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Select the object whose properties you want to add variables.</li><li className="li">Capture its locator and create a variable with<code className="ph codeph">${'{'}&lt;variable name&gt;{'}'}</code> as a placeholder for its dynamic property. For example, we create the <code className="ph codeph">${'{'}id{'}'}</code> variable for the <code className="ph codeph">id</code> property's value. You can use variables in different selection methods.<ul className="ul"><li className="li"><p className="p">Attributes <img className="image" width={600} src={useBaseUrl("/56268ac0-d5fe-11ee-9719-0242c7a41fd4/KS_object_view_added_variable_to_attributes.png")} /></p></li><li className="li"><p className="p">XPath <img className="image" width={600} src={useBaseUrl("/563cd1e0-d5fe-11ee-9719-0242c7a41fd4/KS_object_view_added_variable_to_xpath.png")} /></p></li></ul></li><li className="li"><p className="p">Using the test objects.</p><p className="p">In <span className="ph uicontrol">Manual</span> view of the test case. Click on the  object with variable.<img className="image" width={600} src={useBaseUrl("/561acaf0-d5fe-11ee-9719-0242c7a41fd4/KS_test_case_click_object.png")} alt="Test Case - Click on Object" /></p><p className="p">In the <span className="ph uicontrol">Test Object Input</span>, declare the variable. <img className="image" width={500} src={useBaseUrl("/56318740-d5fe-11ee-9719-0242c7a41fd4/KS_test_object_input.png")} /></p><div className="p">The equivalent result in <span className="ph uicontrol">Script</span> view:<pre className="pre codeblock"><code>WebUI.setText(findTestObject('Page_CURA Healthcare Service/input_Username_username', [('id') : 'txt-username']), Username){"\n"}</code></pre></div></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> There are some cases in which you can identify an object's locator only when it's runtime. In other words, the exact locator of the intended object cannot be specified beforehand in test scripts. In the<a className="xref j-external-link" href="https://katalon-demo-cura.herokuapp.com/profile.php#login" target="_blank"> Cura Healthcare Center appointment web     page</a>, for instance, there are three options of the healthcare program, and the selected one is only known with passing data during execution. </p> 
<img xmlns="http://www.w3.org/1999/xhtml" className="image" width={670} src={useBaseUrl("/562419c0-d5fe-11ee-9719-0242c7a41fd4/KS_AUT_healthcare_medicare_selected.png")} /> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Depending on your preferred selection method, including XPath, Attributes or CSS, the captured object has a corresponding selected locator. </p> 

Below steps are how to add variable to test objects in this case:

- **Medicare**: `//*[@id=\"appointment\"]/div/div/form/div[3]/div/label[1]`
- **Medicaid**: `//*[@id=\"appointment\"]/div/div/form/div[3]/div/label[2]`
- **None**: `//*[@id=\"appointment\"]/div/div/form/div[3]/div/label[3]`

In the captured XPath locators of those 3 options, they share this same pattern `//*[@id=\"appointment\"]/div/div/form/div[3]/div/label`. In this case, the property variation is the label index. We can dynamically determine which option to select by modifying the label index with variable.

For example: `//*[@id=\"appointment\"]/div/div/form/div[3]/div/label[${index}]`.