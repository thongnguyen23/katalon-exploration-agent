---
hide_title: true
title: Using List to Store the Mobile Elements to Validate Data in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_store_mobile_elements_to_validate_data" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Using List to Store the Mobile Elements to Validate Data in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

    

## <a id="id_1" class="anchor_top_offset"/>Scenario

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We want to select a Radio button from a List. In order to do so,   we need to capture all the button elements in a collection and pick   the desired Radio button.</p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from Mobile keyword and click on     <strong className="ph b">Input</strong> it will open a window. In     <strong className="ph b">appFile</strong>, select <strong className="ph b">Value Type</strong> as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as <strong className="ph b">path</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/store_mobile_elements_to_validate_data/Using-List-to-Store-the-Mobile-Elements-to-Validate-Data-1.png")} alt="Select an element from a list in mobile automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: Add <strong className="ph b">Wait For Element Present</strong>     item.</li><li className="li">Step 3: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">Views</strong>. <strong className="ph b">Scroll       To Text</strong> accepts String type parameter (Text of the element     to scroll to).</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/store_mobile_elements_to_validate_data/Using-List-to-Store-the-Mobile-Elements-to-Validate-Data-9.png")} alt="Select an element from a list in mobile automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 4: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">Views.</strong>   </li><li className="li">Step 5: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">Radio Group.</strong>   </li><li className="li">Step 6: Tap on <strong className="ph b">Radio Group.</strong>   </li><li className="li">Step 7: After tapping on 'Radio Group', we want to     <strong className="ph b">wait</strong> for heading '<strong className="ph b">Views/Radio       Group</strong>' to be <strong className="ph b">visible</strong> on the screen.</li><li className="li">Step 8: Add a <strong className="ph b">binary statement</strong> to initialize     <strong className="ph b">Appium Driver</strong> with Katalon <strong className="ph b">Mobile       Driver</strong>.</li><li className="li">Step 9: Add another <strong className="ph b">binary statement</strong> to get     all radio elements and store in a List. In <strong className="ph b">Left       Expression</strong>, select '<strong className="ph b">Variable</strong>' as     <strong className="ph b">Value Type</strong> and pass '<strong className="ph b">elements</strong>' in     <strong className="ph b">Value</strong>. In <strong className="ph b">Right expression</strong>,     select '<strong className="ph b">Method Call</strong>' as <strong className="ph b">Value       Type</strong> and pass the list of radio buttons object     information.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/store_mobile_elements_to_validate_data/Using-List-to-Store-the-Mobile-Elements-to-Validate-Data-92.png")} alt="Select an element from a list in mobile automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 10: Add a <strong className="ph b">for-each loop</strong> statement.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/store_mobile_elements_to_validate_data/Using-List-to-Store-the-Mobile-Elements-to-Validate-Data-10.png")} alt="Select an element from a list in mobile automation" /><br /><br /> </p> 

<ul> <li> Step 10.1: Add a binary statement to capture the text of each element in the list and store it in the "actual_Text" variable. </li> </ul>

<ul><li> Step 10.2: Add 'if' statement and verify whether the actual text matches the expected text. When the actual text matches the expected text, perform click action on Radio button. </li> </ul>

<ul> <li> Step 10.3: After performing click event, we need to terminate for each loop. Add a method call statement 'break' to achieve this. </li> </ul>

## <a id="id_3" class="anchor_top_offset"/>Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import org.openqa.selenium.WebElement as WebElement
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory as MobileDriverFactory
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import io.appium.java_client.AppiumDriver as AppiumDriver

'Path of the Apk File Store in path variable' 
def path = RunConfiguration.getProjectDir() + '/Data Files/ApiDemos.apk'

'Start the application' 
Mobile.startApplication(path, false)

'Wait for element Present of Heading API Demos' 
Mobile.waitForElementPresent(findTestObject('API Demos Objects/List_Example/heading_API_Demos'), 45)

'Scroll to Views text' 
Mobile.scrollToText('Views', FailureHandling.STOP_ON_FAILURE)

'Tap on Views' 
Mobile.tap(findTestObject('API Demos Objects/List_Example/text_Views'), 20)

'Scroll to Radio Group text' 
Mobile.scrollToText('Radio Group', FailureHandling.STOP_ON_FAILURE)

'Tap on Radio Group' 
Mobile.tap(findTestObject('API Demos Objects/List_Example/text_Radio Group'), 30)
 
'Wait for Element Present of Header Radio Group'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/List_Example/text_Header Radio Group'), 30)

'Initializing Appium Driver by Katalon Mobile Driver' 
AppiumDriver<?> driver = MobileDriverFactory.getDriver()

'Getting all similar elements and storing in to List' 
List<WebElement> elements = driver.findElementsByClassName('android.widget.RadioButton')

'Printing the Size of list elements' 
println('The size of elements is ::' + elements.size())
 
'Here Using For each loop for iterations' 
for (WebElement radio : elements) {
    'Get the text of each element in the list and store in to the "actual_Text" variable.'
    String actual_Text = radio.getText()
    
    'Here verifying the actual text with expected text of "Dinner" on every iteration' 
     if(actual_Text.equals("Dinner")){
        'Click on expected Element "Dinner" '
        radio.click();

        'Break the loop'
        break;
     }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available at <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">katalon-studio/katalon-mobile-automation</a>.</p> 
