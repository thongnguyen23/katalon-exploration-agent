---
hide_title: true
title: How to implement data-driven testing in a test case with Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to implement data-driven testing in a test case with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

Whenever you want to execute a test case repeatedly with different data, you can implement data-driven testing (DDT). Katalon Recorder facilitates DDT with DDT commands and several data formats. See: [Data-driven testing in Katalon Recorder](/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/data-driven-testing/data-driven-testing-in-katalon-recorder).

This tutorial shows you how to implement DDT in a test case.

Note: To use the sample project of this tutorial, navigate t **Actions > Sample Projects**, then add the **Implement data-driven testing** project.    

## <a id="id_1" class="anchor_top_offset"/>Test case scenario

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In our example, we follow the test case with the scenario "log   in and book a healthcare appointment," which consists of these   steps:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Log in to the application under test (AUT) - Katalon CURA     Healthcare Service:     <code className="ph codeph">https://katalon-demo-cura.herokuapp.com</code>.</li>   <li className="li">Book an appointment by filling in a form with visit date and     comment.</li>   <li className="li">Log out.</li> </ol> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To demonstrate implementing DDT in Katalon Recorder, we create a   test case that uses data from a CSV file to book three   appointments. The process is as follows:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Record the test case: we record the test case to log in and     book an appointment manually.</li>   <li className="li">Implement DDT in the test case: we bind the test case with a     data file and modify it with DDT commands.</li> </ol> 
    
  

## <a id="id_2" class="anchor_top_offset"/>Record the test case

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We record a test case according to the presented scenario.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">In Katalon Recorder, create a new test case, then click on the <strong className="ph b">Record</strong> button to start recording.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-New-test-case.png")} alt="Katalon Recorder new test case" /><br /><br />     </p>   </li><li className="li">     <p className="p">In an active browser tab, navigate to the AUT.</p>     <p className="p">Here the URL for the AUT is <code className="ph codeph">https://katalon-demo-cura.herokuapp.com</code>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/AUT-Homepage.png")} alt="Katalon Recorder AUT overview" /><br /><br />     </p>   </li><li className="li">     <p className="p">Log in to the AUT.</p>     <p className="p">On the top-right corner of the homepage, click on the <em className="ph i">menu</em> button and select <strong className="ph b">Login</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/AUT-Login.png")} alt="Katalon Recorder AUT login button" /><br /><br />     </p>     <p className="p">On the opened Login page, type in the sample username and password, then click <strong className="ph b">Login</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/AUT-Enter-username-password.png")} alt="Katalon Recorder AUT login page" /><br /><br />     </p>   </li><li className="li">     <p className="p">On the <strong className="ph b">Make Appointment</strong> page, input the visit date and comment, then click <strong className="ph b">Book Appointment</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/AUT-Fill-in-form.png")} alt="Katalon Recorder AUT make appointment page" /><br /><br />     </p>   </li><li className="li">     <p className="p">Log out of the AUT. Click on the <em className="ph i">menu</em> button and select <strong className="ph b">Logout</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/AUT-Logout-button.png")} alt="Katalon Recorder AUT logout button" /><br /><br />     </p>   </li><li className="li">     <p className="p">In Katalon Recorder, click on the <strong className="ph b">Stop</strong> button to stop the recording</p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The recorded test case is as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Recorded-test-case.png")} alt="Katalon Recorder recorded test case" /><br /><br /> </p> 
    
## <a id="id_3" class="anchor_top_offset"/>Implement data-driven testing
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon Recorder, there are three steps to implement DDT in a   test case:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Prepare the data file.</li>   <li className="li">Add the data file to your workspace.</li>   <li className="li">Configure data-driven commands and variables in the test case     to use data from the data file.</li> </ol> 

### <a id="id_4" class="anchor_top_offset"/>Prepare the data file

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder supports two data file formats: CSV and JSON. To learn more about the supported formats and their specifications, refer to this document: <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/data-driven-testing/data-driven-testing-in-katalon-recorder#id_5">Data-driven testing in Katalon Recorder</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In our example, we use the following CSV file:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/CSV-file.png")} alt="Katalon Recorder recorded test case" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This CSV data file has a column named "Comment" that contains appointment comments.</p> 

### <a id="id_5" class="anchor_top_offset"/>Add the data file to the workspace

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">In the <strong className="ph b">Workspace</strong> sidebar, click on the <strong className="ph b">Open a Data File</strong> button in the <strong className="ph b">Test Data</strong> section.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Add-test-data-button.png")} alt="Katalon Recorder add test data" /><br /><br />     </p>   </li><li className="li">     <p className="p">In the opened file explorer, select the CSV file.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-File-explorer.png")} alt="Katalon Recorder select the CSV file" /><br /><br />     </p>   </li><li className="li">     <p className="p">Katalon Recorder should display the selected file under the <strong className="ph b">Test Data</strong> section.</p>   </li></ol> 

### <a id="id_6" class="anchor_top_offset"/>Configure data-driven commands and variables in the test case

Katalon Recorder also provides a simple user interface to configure data-driven commands and variables.

Follow these steps:

1. Select the data file. Right-click on the data file and select **Use this in a test case**.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-Use-this-in-a-test-case.png" alt="Katalon Recorder use test data file" /> <br/>

2. Select the test case. In the displayed menu, select the desired test case. Click **Next** to continue.
    Here we select the test case that we previously recorded.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Select-test-case.png" alt="Katalon Recorder select test case" /> <br/>

3. Use the data from the data file. In the displayed test case, select the commands and specify the desired variables. Click Add when done.

    Katalon Recorder specifies a variable using the `${<variable_name>}` syntax as a placeholder in the Value field. When executing the test case, Katalon Recorder expands the variable into its value.

    We want to use the comments from the CSV file, so we replace the current comment text with the Comment variable.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Configure-variable.png" alt="Katalon Recorder configure comment variable" /> <br/>

4. Verify that the values in the test case are replaced with the correct variable.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Test-case-configured-with-variable.png" alt="Katalon Recorder configure comment variable" /> <br/>

5. Play the test case and verify the results in the Log view. The log message should indicate that Katalon Recorder expands the specified variables into test data.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/implement-ddt-in-a-test-case/KR-5.8.0-Test-results.png" alt="Katalon Recorder DDT results" /> <br/>

See also: The Katalon Academy course: [Data-Driven Testing with Katalon Recorder](https://academy.katalon.com/courses/katalon-recorder-data-driven-testing/).