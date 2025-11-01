---
hide_title: true
title: Data-driven testing in Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Data-driven testing in Katalon Recorder

Data-driven testing (DDT) allows you to execute test cases using data from external data files in table or spreadsheet format. Katalon Recorder facilitates DDT by providing DDT commands and enabling you to bind test cases with data files.

:::tip requirements
Katalon Recorder version 5.6.0 onwards.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article introduces you to the DDT commands and data file   formats supported by Katalon Recorder.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Data-driven commands 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder provides two commands for DDT:   <code className="ph codeph">loadVars</code> and <code className="ph codeph">endLoadVars</code>.</p> 

### <a id="id_2" class="anchor_top_offset"/>loadVars
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">loadVars</code> command starts a loop to repeatedly   load the values from the data file specified in the   <strong className="ph b">Target</strong> field.</p> 

### <a id="id_3" class="anchor_top_offset"/>endLoadVars      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">endLoadVars</code> command terminates the data-driven   block. You need to add it to your test; otherwise, you will get an   error message.</p> 

### <a id="id_4" class="anchor_top_offset"/>Data-driven testing process

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you execute a test containing <code className="ph codeph">loadVars</code> and   <code className="ph codeph">endLoadVars</code> commands, the following process will take   place, with <em className="ph i">i</em> starting with 1 and ending with the number   of rows in the data file:</p> 
        
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">The <em className="ph i">ith</em> row of the data file will be fetched.</li>   <li className="li">The values of the row will be mapped to the variables used in     the test case.</li>   <li className="li">The steps between <code className="ph codeph">loadVars</code> and     <code className="ph codeph">endLoadVars</code> will be executed using these mapped     values.</li> </ol> 

## <a id="id_5" class="anchor_top_offset"/>Data file formats      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder supports two data file formats: CSV and   JSON.</p> 

### <a id="id_6" class="anchor_top_offset"/>Data files in CSV format

<p xmlns="http://www.w3.org/1999/xhtml" className="p">While performing DDT with a CSV data file, Katalon Recorder navigates the file using the column names, and extracts data from the file, row by row. Therefore, you need to create a CSV file with specific column names.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder also treats CSV column names as case-sensitive.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, a data-driven test that fills in a form with dates and comments might have a CSV data file as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/ddt-guide/KR-Sample-CSV-file.png")} alt="Sample CSV file for Katalon Recorder" /><br /><br /> </p> 

### <a id="id_7" class="anchor_top_offset"/>Data files in JSON format

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder uses JSON data files with specific syntax. Test data in a JSON file must be organized in an array. Each element (data row) in the array is represented as an object with <em className="ph i">name/value</em> pairs; the name specifies the column name, and the value specifies the value in the respective row.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/ddt-guide/KR-DDT-Sample-JSON-syntax.png")} alt="Sample JSON syntax" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, a JSON data file with two columns, dates and comments, might be written as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/ddt-guide/KR-Sample-JSON-file.png")} alt="Sample JSON file for Katalon Recorder" /><br /><br /> </p> 

## <a id="id_8" class="anchor_top_offset"/>Sample projects

Katalon Recorder comes with a set of built-in sample projects to get you started with DDT.

Follow these steps to add a sample project:
1. In the Actions sidebar, select Sample Projects.

  <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/ddt-guide/KR-Action-sidebar-Sample-Projects.png" alt="Action sidebar" /> <br/>

2. In the displayed dialog, select the Fill a form with data from CSV file with Sample Test Data sample project. Click Add to add the project.

  <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/ddt-guide/KR-Sample-Project-dialog.png" alt="Sample project dialog" /> <br/>

See also: The Katalon Academy course: [Data-Driven Testing with Katalon Recorder](https://academy.katalon.com/courses/katalon-recorder-data-driven-testing/).

