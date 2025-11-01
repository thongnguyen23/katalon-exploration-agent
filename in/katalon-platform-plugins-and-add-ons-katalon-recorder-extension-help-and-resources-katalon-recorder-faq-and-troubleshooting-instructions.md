---
hide_title: true
title: Katalon Recorder FAQ and Troubleshooting Instructions
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-7243" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/><span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span>  FAQ and Troubleshooting Instructions

## <a id="id_1" class="anchor_top_offset"/>Why should I sign up for a free account?

<div xmlns="http://www.w3.org/1999/xhtml" className="p">When you sign up for a free account, you will get access to the following capabilities in Katalon Recorder:<ul className="ul"><li className="li"><p className="p">Create <strong className="ph b">unlimited automation scripts</strong> to automate unlimited scenarios.</p></li><li className="li"><p className="p"><strong className="ph b"><a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/execution-report/view-execution-reports-in-testops">Automatically back up your data to TestOps</a></strong> to avoid data loss.</p></li><li className="li"><p className="p"><strong className="ph b"><a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/execution-report/view-execution-reports-in-testops">Store execution results to TestOps</a></strong> to review trends and history.</p></li><li className="li"><p className="p"><strong className="ph b">Receive updates</strong> on Katalon, new features and bug fixes regularly to maximize the value of the product.</p></li></ul> </div>

## <a id="id_2" class="anchor_top_offset"/>Common failures and resolutions  
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Try the following suggestions when your automation scripts fail.   If they don't work either, open a thread on <a className="xref j-external-link" href="https://forum.katalon.com/c/katalon-recorder/17" target="_blank">our     forum</a> to ask experts for help.</p> 

### <a id="id_3" class="anchor_top_offset"/>Your automation script passes but the actual action was not         performed

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Add the following step:<ul className="ul"><li className="li"><p className="p">Command: waitForElementPresent.</p></li><li className="li"><p className="p">Target: Same target as the failing step.</p></li><li className="li"><p className="p">Value: none.</p></li></ul> </div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">before the failing step.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">If that doesn't work, then add the following step: <ul className="ul"><li className="li"><p className="p">Command:
        pause.</p></li><li className="li"><p className="p">Target: none.</p></li><li className="li"><p className="p">Value: 10000 (miliseconds).</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">before the failing step.</p> 
      

### <a id="id_4" class="anchor_top_offset"/>Your automation script fails because of element not found

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Locators are methods that KR use to find elements on websites.   If your automation script fails because of an element not found,   click on the target dropdown of the failed step and choose another   locator.</p> 
      
## <a id="id_5" class="anchor_top_offset"/>FAQ

### <a id="id_6" class="anchor_top_offset"/>Upload files

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Currently, only the Chrome version of Katalon Recorder supports   file uploading.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Right click on the extension icon on the top right toolbar,   select <strong className="ph b">Manage extensions</strong>. In the <strong className="ph b">Manage     extensions</strong> page, enable "Allow access to file URLs".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-recorder/docs/katalon-recorder-allow-access-to-file-urls.png")} /><br /><br /> </p> 
The action was completed using "type" command. Example:

```jsx
type | id=file-upload | C:\file.txt (or /home/me/file.txt for Linux)
```
:::info notes
Do not `click` on the input element.
:::
We are still actively looking for a solution for Firefox. If you have any question or suggestion, please join the discussion here.
      
### <a id="id_7" class="anchor_top_offset"/>Drag and drop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If the drag-and-drop feature on your website was built with   HTML5, please use the command "dragAndDropToObject". If it was   built with jQuery UI, please use the command   "dragAndDropToObjectByJqueryUI".</p> 
      
### <a id="id_8" class="anchor_top_offset"/>Set text values for text-based input elements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Due to the differences between web pages, there are three   commands you can use to set text values for text-based input   elements (e.g. type="text" or "number"). If you encounter troubles   setting text values, please try those commands in this order:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">type</li><li className="li">sendKeys</li><li className="li">setText</li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   For input elements with type="number",   you have to use "setText" to set negative values. </p> 

### <a id="id_9" class="anchor_top_offset"/>Content Security Policy errors

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We are looking for a solution right now. Technically, it's   possible to overwrite CSP rules with add-ons, but it would be   insecure to do that on every web page.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For now, to work around the issue on Chrome, users can use a   third-party add-on (e.g.<a className="xref j-external-link" href="https://chrome.google.com/webstore/detail/disable-content-security/ieelmcmcagommplceebfedjlakkhpden?hl=en" target="_blank">Disable Content-Security-Policy</a>)   to disable CSP rules, then execute the test in KR as usual.   <strong className="ph b">Don't forget to disable that add-on when     unused.</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">On Firefox, please disable the "security.csp.enable" option in   "about:config" to achieve the same effect. <strong className="ph b">Don't     forget to enable it when unused.</strong> </p> 
