---
hide_title: true
title: Import Selenium IDE version 3 projects to Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Import Selenium IDE version 3 projects to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In addition to importing Selenium/TestNG/JUnit projects into Katalon Studio, you can also import a Selenium IDE project for execution with <span className="ph">Katalon Studio</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Selenium IDE is an integrated development environment for Selenium tests. It is implemented as a Chrome add-on and Firefox extension, which allows users to record, edit, and debug tests. Katalon Studio supports Selenium IDE project version 3.x onwards.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial shows you how to import a Selenium IDE project to a project in <span className="ph">Katalon Studio</span> and how <span className="ph">Katalon Studio</span> maps the imported test artifacts.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can download our GitHub sample project for importing a Selenium IDE project to <span className="ph">Katalon Studio</span>: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/import-selenium-ide-sample" target="_blank">Import Selenium IDE sample</a>.</p> 

## <a id="concept-6087" class="anchor_top_offset"/>Import a Selenium IDE project to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph">Katalon Studio</span>:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Open a project.</li><li className="li">     <p className="p">From the menu bar, select <strong className="ph b">File &gt; Import Selenium IDE Project</strong> and browse your Selenium IDE file (a single file with a <code className="ph codeph">.side</code> extension) to open.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-selenium-ide/selenium-ide.png")} width={763} alt="Import Selenium IDE" /><br /><br />     </p>   </li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Map Selenium IDE with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  test artifacts

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Selenium IDE project contains Tests, Suites, and Executing.   Katalon Studio only imports Tests and Suites.</p> 

### <a id="id_3" class="anchor_top_offset"/>Selenium IDE Suites - <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  Test Suites

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Under the <strong className="ph b">Test Suites</strong> folder in <strong className="ph b">Tests Explorer</strong>, Katalon Studio creates an <strong className="ph b">Imported from Selenium IDE Scripts</strong> folder to store the imported suites. Once the import process is done, Katalon Studio open the test suites automatically.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-selenium-ide/test-suites.png")} /><br /><br /> </p> 

:::info notes
- If your Katalon project already has an **Imported from Selenium IDE Scripts** folder under the **Test Suites** folder, the new folder should be **Imported from Selenium IDE Scripts (1)**.
- If there is no suite in the imported Selenium IDE project, Katalon Studio does not create an **Imported from Selenium IDE Scripts** folder under the **Test Suites** folder.
:::

### <a id="id_4" class="anchor_top_offset"/>Selenium IDE Tests - <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  Test Cases

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Under the <strong className="ph b">Test Cases</strong> folder in <strong className="ph b">Tests Explorer</strong>, Katalon Studio creates an <strong className="ph b">Imported from Selenium IDE Scripts/&lt;suite name&gt;</strong> folder to store the imported tests.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-selenium-ide/test-cases.png")} width={750} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">An imported test case contains a set of Selenium commands recorded by Selenium IDE.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-selenium-ide/test.png")} width={800} /><br /><br /> </p> 

:::info notes
- Supported element locators include `identifier`, `id`, `name`, `dom`, `xpath`, `link`, `css`, and `ui`. To learn more about Selenium locators, you can refer to the Selenium Java document here: [Selenium Java document](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/locators/package-summary.html).
:::

## <a id="id_5" class="anchor_top_offset"/>See also

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref" href="/katalon-studio/get-started/migrate-from-other-tools/seleniumtestngjunit-migration-to-katalon-studio">Selenium/TestNG/JUnit       Migration to Katalon Studio</a>   </li><li className="li">Learn more with our Katalon Academy course: <a className="xref j-external-link" href="https://academy.katalon.com/courses/selenium-migrate/?utm_source=kat_docs&utm_medium=import_selenium_ide" target="_blank">Migrate       from Selenium to Katalon Studio – Everything You Should       Know</a>   </li></ul> 
