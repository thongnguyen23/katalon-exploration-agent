---
hide_title: true
title: Upgrade or Downgrade WebDrivers in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Upgrade or Downgrade WebDrivers in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To have a better control of the browser versions while testing, Katalon Studio allows you to update or downgrade WebDrivers manually or via Katalon Studio built-in tools. This article will show you how to do so.</p> 

## <a id="id_1" class="anchor_top_offset"/>Update a WebDriver

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can update Chrome, Firefox, Edge Chromium and Internet Explorer WebDrivers directly from Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">From the main toolbar, select <span className="ph uicontrol">Tools</span> &gt; <span className="ph uicontrol">Update WebDrivers</span>. Select a browser in the dropdown list.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={300} src={useBaseUrl("/e60f6e20-2f30-11ed-9930-0242fe3e4a3f/ks-850-update-web-driver.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio can detect and allows you to auto-update a compatible Chrome or Edge Chromium driver version when start using Spy/Recorder Web Utility.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/handle-webdrivers/KS-Auto-update-WebDriver.png")} width={500} alt="update-webdriver-automatically" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For console mode execution, you can use this command argument <code className="ph codeph">--config -webui.autoUpdateDrivers=true</code> to allow automatic WebDriver updates. You can learn more about using the console mode here: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine">Console Mode Execution</a>.</p> 

## <a id="id_2" class="anchor_top_offset"/>Replace a Webdriver

To upgrade or downgrade WebDrivers, you can replace WebDrivers manually. You can choose to do so at the application or project level.

:::info notes
By default, Katalon Studio runs WebDrivers at the application level. Adding a Webdriver at the project level overrides the application level to open your web browsers. 
:::
Do as follows:

1. Find the WebDriver version you want to run your test with. You can find them here:
    - [Chrome Drivers 115 onwards](https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json)
        
      [Chrome Drivers 114 and older](https://chromedriver.chromium.org/downloads)        
    - [Gecko Drivers](https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html)
    - [Internet Explorer](http://selenium-release.storage.googleapis.com/index.html)
    - [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
2. Find the location of the WebDrivers you want to replace.

  - At the application level, WebDriver binaries are stored here:
      
      **Note**: If you have multiple Katalon Studio versions installed on your development machine, make sure to navigate to the correct path of the Katalon Studio version you wish to use.
        
      | *For Window users* |  |
      | --- | --- |
      | **Chrome** <br/> (You can use 32-bit Windows Chromedriver for both 32-bit and 64-bit Windows) | • `<Katalon Studio folder>\configuration\resources\drivers\chromedriver_win32` <br/> <br/> • `<Katalon Studio folder>\configuration\resources\drivers\chromedriver_win64` |
      | **Firefox** | • `<Katalon Studio folder>\configuration\resources\drivers\firefox_win32` <br/> <br/> • `<Katalon Studio folder>\configuration\resources\drivers\firefox_win64` |
      | **Internet Explorer** | • `<Katalon Studio folder>\configuration\resources\drivers\iedriver_win32` <br/> <br/> • `<Katalon Studio folder>\configuration\resources\drivers\iedriver_win64` |
      | **Edge** | • `<Katalon Studio folder>\configuration\resources\drivers\edgedriver` |
      | **Edge (Chromium)** | • `<Katalon Studio folder>\configuration\resources\drivers\edgechromium_win32` <br/> <br/> • `<Katalon Studio folder>\configuration\resources\drivers\edgechromium_win64` |
      ---
      
      | *For macOS users* |  |
      | --- | --- |
      | **Chrome** | •`/Applications/Katalon Studio.app/Contents/Eclipse/configuration/resources/drivers/chromedriver_mac` |
      | **Firefox** | •`/Applications/Katalon Studio.app/Contents/Eclipse/configuration/resources/drivers/firefox_mac` |
      | **Edge (Chromium)** | •`/Applications/Katalon Studio.app/Contents/Eclipse/configuration/resources/drivers/edgechromium_mac` |
    
  - At the project level, go to **\Project Folder\Include (for Windows)** or **/Project Folder/Include (for MacOS/Linux)** on your computer and follow the below paths:

      By default, there is no Webdriver at project level. After replacing WebDrivers at project level, restart Katalon Studio to run new WebDrivers.
    
      | *For Window users* |  |
      | --- | --- |
      | **Chrome** | •`Include\drivers\chromedriver_win32\chromedriver.exe` <br/> <br/> •`Include\drivers\chromedriver_win64\chromedriver.exe` |
      | **Firefox** | •`Include\drivers\geckodriver_win32\geckodriver.exe` <br/> <br/> •`Include\drivers\geckodriver_win64\geckodriver.exe` |
      | **Internet Explorer** | •`Include\drivers\iedriver_win32\IEDriverServer.exe` <br/> <br/> •`Include\drivers\iedriver_win64/IEDriverServer.exe` |
      | **Edge (Chromium)** | •`Include\drivers\edgedriver_win32/MicrosoftWebDriver.exe` <br/> <br/> •`Include\drivers\edgedriver_win64\MicrosoftWebDriver.exe` <br/> <br/> •`Include\drivers\edgechromiumdriver_win64\msedgedriver.exe` <br/> <br/> •`Include\drivers\edgechromiumdriver_win32\msedgedriver.exe` |
      ---

      | *For macOS users* |  |
      | --- | --- |
      | **Chrome** | •`Include/drivers/chromedriver_mac64/chromedriver` |
      | **Firefox** | •`Include/drivers/geckodriver_mac64/geckodriver` |
      | **Edge (Chromium)** | •`Include/drivers/edgechromiumdriver_mac/msedgedriver` |
      
      ---
      | *For Linux users* |  |
      | --- | --- |
      | **Chrome** | •`Include/drivers/chromedriver_linux32/chromedriver` <br/> <br/> •`Include/drivers/chromedriver_linux64/chromedriver` |
      | **Firefox** | •`Include/drivers/geckodriver_linux32/geckodriver` <br/> <br/> •`Include/drivers/geckodriver_linux64/geckodriver` |        

3. After finding the correct location, replace the `driver.exe` file with the one you have downloaded.
    
  **Note**: After updating or downgrading WebDrivers, to make sure the current version of the browser driver is running smoothly, it is advisable to try **re-running the test** to resolve and check any pop-up issues.

## <a id="concept-4485" class="anchor_top_offset"/>Use DriverFactory library

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio also offers DriverFactory library to manipulate WebDriver instances by using Katalon keywords.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Starting from Katalon Studio version 10.0.0, the <code className="ph codeph">DriverFactory</code> class has been refactored. If you are using methods like <code className="ph codeph">getChromeDriverPath()</code>, refer to the migration documentation for details on these changes and how to update your scripts: <a className="xref" href="/katalon-studio/get-started/workspace-settings/migrate-katalon-studio-from-9.x-to-10.0.0#concept-311">Refactoring of DriverFactory</a>.</p></li></ul></div></div>
    

## <a id="id_4" class="anchor_top_offset"/>See also

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/terminate-webdrivers-in-katalon-studio">Terminate       Webdrivers</a>   </li>   <li className="li">     <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/handle-webdrivers-with-eventfiringwebdriver-in-katalon-studio">Handle       WebDrivers with EventFiringWebDrivers</a>   </li> </ul> 
    
  
