---
hide_title: true
title: Use the Self-Healing function in Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use the Self-Healing function in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">On some websites, automation scripts can fail because the   default locator fails to find an element. In that case,   Self-Healing will automatically try out other locators. If it finds   a valid locator, it will continue the automation script using that   locator and records the broken and valid locators for later   use.</p> 

## <a id="id_1" class="anchor_top_offset"/>Enabling and disabling Self-Healing  
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Self-healing is enabled by default.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can disable it by following these steps:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Go to <strong className="ph b">Settings &gt; Self-Healing</strong>.</p>   </li>   <li className="li">     <p className="p">Uncheck <strong className="ph b">Enable Self-Healing execution</strong>.</p>   </li>   <li className="li">     <p className="p">Save and close.</p>   </li> </ol> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-recorder/docs/jtbd/execute-scenarios/self-healing/kr-self-healing-setting.png")} /><br /><br /> </p> 

## <a id="id_2" class="anchor_top_offset"/>Prioritizing locator methods in Self-Healing
   
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Self-Healing uses 3 locator methods, in this priority order:   <strong className="ph b">id</strong>, <strong className="ph b">css</strong>, <strong className="ph b">xpath</strong>.   However, the best locator methods may vary depending on your   websites under test.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can change the order of locator methods by following these   steps:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Go to <strong className="ph b">Settings &gt; Self-Healing</strong>.</p>   </li>   <li className="li">     <p className="p">Make sure Self-Healing is enabled.</p>   </li>   <li className="li">     <p className="p">Drag and drop the locator methods in the order of your       choosing.</p>   </li>   <li className="li">     <p className="p">Save and close.</p>   </li> </ol> 

## <a id="id_3" class="anchor_top_offset"/>Excluding certain commands from Self-Healing

:::warning caution
Some commands validate that a particular element exists on a certain page. We advise you to not trigger Self-Healing on these commands, as it encurs the risk of validating elements incorrectly.

By default, `verifyElementPresent`,`verifyElementNotPresent`,`assertElementPresent` and `assertElementNotPresent` commands are excluded from Self-Healing.
:::
You can choose to exclude certain commands from Self-Healing by following these steps:

1. Go to **Settings > Self-Healing**.
2. Make sure Self-Healing is enabled.
3. Add the commands you want to exclude to the list.
4. Save and close.

:::info notes
Regex is also supported for excluding commands. For example, you can exclude all command starting with the keywordwaitFor by adding ^waitFor to the list.
:::

## <a id="id_4" class="anchor_top_offset"/>Approving Self-Healing proposals

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When the default locator fails, Self-Healing finds alternative   locators to complete the test execution. After the test execution   is completed, you can choose to replace failing locators by   approving Self-Healing suggestions.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-recorder/docs/jtbd/execute-scenarios/self-healing/kr-self-healing-approval-process.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Self-Healing tab is refreshed on every new execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To approve Self-healing suggestions, follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Go to the Self-Healing tab.</p>   </li><li className="li">     <p className="p">Select the suggested locators using the status filter.</p>   </li><li className="li">     <p className="p">Press <strong className="ph b">Approve</strong>.</p>   </li></ol> 
