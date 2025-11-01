---
hide_title: true
title: Error exporting test artifacts in Katalon Studio
---

# <a id="troubleshooting-yyf1tpo8" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Error exporting test artifacts in Katalon Studio

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When exporting test artifacts in Katalon Studio, the following error can occur:</p><div className="p"><pre className="pre codeblock"><code>Error exporting test artifacts{"\n"}Cannot invoke "java.io.File.getAbsolutePath()" because the return value of "com.katalon.platform.api.model.TestCaseEntity.getScriptFile()" is null{"\n"}</code></pre></div></section> 

#### Cause
Each test case in Katalon Studio should consist of:

- A metadata file (`.tc`, in XML format)
- A script file (`.groovy`)

The error arises when one or more test cases are missing the script file (`*.groovy`). This can happen due to merge conflicts, unexpected errors, or other issues that caused the file to be lost or corrupted.
#### Remedy
1. Identify the broken test case(s).The error occurs because Katalon Studio is trying to export a test case, but the script file (`*.groovy`) is missing. To identify the problematic test case(s), apply the binary search technique:

    a. Export half of the test case folders. 

    b. If the error occurs, narrow down the problem by exporting half of the previously selected folders.
    
    c. If no error occurs, export the second half of the folders.
    
    d. Repeat this process until you identify the folder containing the broken test case(s).

2. Once the broken test case(s) are identified, there are two ways to resolve the issue:
    - Remove the test case
    
    Completely delete both the metadata file (`*.tc`) and the script file (`*.groovy`) for the broken test case.
    
    - Recreate the test case
    
    Delete both the `*.tc` and `*.groovy` files, and then recreate the test case using Katalon Studio