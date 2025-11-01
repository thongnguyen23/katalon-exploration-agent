---
hide_title: true
title: Handling Scroll to Element in Mobile Automation in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_scroll_element_mobile_automation" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Scroll to Element in Mobile Automation in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

## <a id="id_1" class="anchor_top_offset"/>Scroll To Text
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial illustrates <strong className="ph b">Scroll to text</strong>   behavior in the mobile app. The demonstration uses API demos, which   you can download from <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation/blob/master/Data%20Files/ApiDemos.apk" target="_blank">here</a>.   The application apk file also comes with the sample project   packaged with your product installation. We will be using Android   O.S for this tutorial, so make sure that your Android device API is   greater than 18.</p> 
  

### <a id="id_2" class="anchor_top_offset"/>Scenario
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The screenshot of the app below has a listview containing 'n'   number of rows. Our goal is to scroll down to the text   '<strong className="ph b">Views</strong>', and to tap on it. When the user taps on   <strong className="ph b">Views,</strong> the app navigates to another screen.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can easily automate this scenario in two ways: manual and   script modes.</p> 

### <a id="id_3" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 1: Click on <strong className="ph b">Add</strong> and select <strong className="ph b">Binary       Statement</strong>.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-1.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 2: Go to <strong className="ph b">Input</strong> field. Select value type     as <strong className="ph b">Variable</strong> in <em className="ph i">Left Expression</em> and name     the variable as '<strong className="ph b">path'</strong>. This name will show up in     Value.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-2.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 3<strong className="ph b">:</strong> Select <strong className="ph b">Value Type</strong> as     <strong className="ph b">Binary</strong> in <em className="ph i">Right Expression</em>. Next, click     on the <strong className="ph b">Value</strong> field. In the new window, enter Left     and Right Expressions.</li>   <li className="li">Step 4<strong className="ph b">:</strong> Select value type as <strong className="ph b">Method       call</strong> in <em className="ph i">Left Expression</em>. Click on the     <strong className="ph b">Input</strong> field, a window will pop up where user can     select an Object Type as <strong className="ph b">Class,</strong> Object as     <strong className="ph b">RunConfiguration,</strong> method as     <strong className="ph b">getProjectDir()</strong> to continue.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-3.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 5: In <em className="ph i">Right Expression</em>, select     <strong className="ph b">String</strong> as <em className="ph i">Value Type</em> and pass the path of     the <strong className="ph b">"/folder name/apk file name with       extension"</strong>.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, if the apk file is stored in Data Filesfolder in   File Explorer, the passed path is "<strong className="ph b">/Data     Files/ApiDemos.apk"</strong> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-5.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 6<strong className="ph b">:</strong> Select <strong className="ph b">Start       Application</strong> from mobile keyword andclick on     <strong className="ph b">Input</strong>. A new window will appear. In     <strong className="ph b">appFile</strong>, select 'Value Type' as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as <strong className="ph b">path</strong>.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-6.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 7: Add <strong className="ph b">Wait For Element Present</strong>     item.</li>   <li className="li">Step 8: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword to pass Input as <strong className="ph b">Views</strong>. <strong className="ph b">Scroll To       Text</strong> accepts String type parameter (Text of the element to     scroll to)</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-8.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 9: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">Views</strong> from Object Repository</li>   <li className="li">Step 10: Select <strong className="ph b">Scroll To Tex</strong>t method and pass     input as '<strong className="ph b">Tabs'</strong>   </li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/scroll_element_mobile_automation/Handling-Scroll-to-Element-in-Mobile-Automation-10.png")} alt="Handling Scroll to Element in Mobile Automation" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The step-by-step guide above can be achieved through   <strong className="ph b">Script mode</strong> (switch to Script Mode by clicking on   Script tab).</p> 

### <a id="id_4" class="anchor_top_offset"/>Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling

'Path of the Apk File Store in path variable'
def path = RunConfiguration.getProjectDir() + '/Data Files/ApiDemos.apk'

'Start the application'
Mobile.startApplication(path, false)

'Wait for element Present of Heading API Demos'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/heading_API_Demos'), 45)

'Scroll to Views text'
Mobile.scrollToText('Views', FailureHandling.STOP_ON_FAILURE)

'Tap on Views'
Mobile.tap(findTestObject('API Demos Objects/text_Views'), 20)

'Scroll to Tabs text'
Mobile.scrollToText('Tabs', FailureHandling.STOP_ON_FAILURE)
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Note:</strong> Steps 1 to 6 in Manual mode can be   optimized by adding a single line in script mode; i.e.,</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>def path = RunConfiguration.getProjectDir() + '/Data Files/ApiDemos.apk'{"\n"}{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">here</a>. For   further instructions and help, please refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-scroll-to-text">Scroll to     Text</a> guideline and join us on <a className="xref j-external-link" href="http://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
