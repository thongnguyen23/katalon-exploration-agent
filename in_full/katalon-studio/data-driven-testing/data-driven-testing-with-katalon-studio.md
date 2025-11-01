---
hide_title: true
title: Data-driven testing with Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Data-driven testing with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Data-driven testing (DDT) is running  test scripts with various data sets instead of using hard-coded values. <span className="ph">Katalon Studio</span> allows you to perform data-driven testing with internal and external data sources at both test case and test suite levels. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can download the data-driven testing sample project from our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/shopping-cart-tests" target="_blank">Shopping cart sample</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document discusses the DDT components  and the supported data-driven testing methods in <span className="ph">Katalon Studio</span>.</p> 

## <a id="id__section-ddt-variables" class="anchor_top_offset"/>Variables

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> supports three types of variables: Global variables, Test Case variables, and Groovy variables.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Global variables</strong><p className="p">Global variables are variables defined in the execution profile and can be used in a test case, test object, web service object,
    and email configuration within a project. To learn more about global
    variables, see <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Global
      variables</a>.</p></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Test Case variables</strong><p className="p">Test case variables are variables defined in a test case, allowing you to pass dynamic data into a test case. You can create test case variables and call test cases with variables in both manual and script mode.</p><p className="p">To learn more about using test case variables, see <a className="xref" href="/katalon-studio/data-driven-testing/test-case-variables">Test case variables</a>.</p></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Groovy variables</strong><div className="note note note_note"><span className="note__title">Note:</span> 
    <p className="p">Katalon Studio supports Groovy from version 2.4.x onwards.</p>
  </div><div className="p">Groovy variables are the variables defined in  Groovy script. For example:<pre className="pre codeblock"><code>// x is defined as a variable of String type{"\n"}String x = "Hello";{"\n"} {"\n"}// y is defined as a variable of int type{"\n"}int y = 5;{"\n"}{"\n"}// The value of the variables are printed to the console{"\n"}println(x);{"\n"}println(y);{"\n"}</code></pre></div><p className="p">To learn more about Groovy,  refer to this Apache Groovy
    document: <a className="xref j-external-link" href="http://groovy-lang.org/semantics.html" target="_blank">Groovy semantics</a>.</p></div>

## Test data

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test data is the data created for data-driven testing.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can create internal or external data files, then configure data binding to read test data values from these files. To learn more about  test data in <span className="ph">Katalon Studio</span>, see <a className="xref" href="/katalon-studio/data-driven-testing/manage-test-data">Manage test data</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, <span className="ph">Katalon Studio</span> converts variables to strings to   perform data binding. However, you can  disable this function to allow <span className="ph">Katalon Studio</span> to read test data values as their data types. See: <a className="xref" href="#">Enhanced     variable binding</a>.</p> 
        

## Set parameter for your test script

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can pass variables to your test scripts by setting parameters in test cases, test objects, or their properties:</p> 
            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref" href="/katalon-studio/test-objects/web-test-objects/use-variables-in-web-test-objects">Parameterize Web Test Objects</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/mobile-test-objects/parameterize-mobile-test-object-properties-in-katalon-studio">Parameterize Mobile Test Object</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/rest-request/parameterize-a-web-service-object">Parameterize Web Service Object</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/windows-test-objects/windows-test-objects-in-katalon-studio#id_6">Parameterize Windows Test Objects</a></li></ul> 
        

## Data-driven testing methods

            
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> supports the following data-driven testing methods:<ul className="ul"><li className="li"><p className="p"><strong className="ph b">In a test case</strong>: Perform data-driven testing in a test case independently from the test suite. See <a className="xref" href="/katalon-studio/data-driven-testing/data-driven-testing-at-test-case-level">Data-driven testing at the test case level</a>.</p></li><li className="li"><p className="p"><strong className="ph b">In a test suite</strong>: Perform data-driven testing in a test suite. See <a className="xref" href="/katalon-studio/data-driven-testing/data-driven-testing-in-a-test-suite">Data-driven testing in a test suite</a>.</p></li><li className="li"><p className="p"><strong className="ph b">In a dynamic test suite</strong>: Perform data-driven testing in a dynamic test
        suite. See <a className="xref" href="/katalon-studio/data-driven-testing/perform-data-driven-testing-in-a-dynamic-test-suite">Data-driven
          testing in a dynamic test suite</a>.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Alternatively, you can also perform data-driven testing with   Groovy using the <code className="ph codeph">findTestData</code> method. To learn about   this method, you can refer to our API documentation: <a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/testdata/TestData.html" target="_blank">TestData</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   Learn in practice with our free Katalon Academy course:    ​   <a className="xref j-external-link" href="https://academy.katalon.com/courses/data-driven-testing/?utm_source=kat_docs&utm_medium=ddt_ks" target="_blank">Katalon Studio: How to Apply Data-Driven Testing</a>.</p> 
                    
