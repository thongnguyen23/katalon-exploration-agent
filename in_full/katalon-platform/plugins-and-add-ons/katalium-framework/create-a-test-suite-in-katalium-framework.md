---
hide_title: true
title: Create a Test Suite in Katalium Framework
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create a Test Suite in Katalium Framework

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test suites and their parameters are defined using TestNG   syntax.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is a simple example (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/resources/testng.xml" target="_blank">source     code</a>):</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;?xml version = "1.0" encoding = "UTF-8"?&gt;{"\n"}&lt;!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" &gt;{"\n"}{"\n"}&lt;suite name="Suite1" verbose="1"&gt;{"\n"}{"    "}&lt;test name="simple" &gt;{"\n"}{"        "}&lt;parameter name="kataDisableScreenshot" value="false" /&gt;{"\n"}{"        "}&lt;classes&gt;{"\n"}{"            "}&lt;class name="com.katalon.kata.sample.testcase.simple.MakeAppointmentTest" /&gt;{"\n"}{"        "}&lt;/classes&gt;{"\n"}{"    "}&lt;/test&gt;{"\n"}{"\n"}{"    "}&lt;test name="parameterize" &gt;{"\n"}{"        "}&lt;parameter name="kataDisableScreenshot" value="true" /&gt;{"\n"}{"        "}&lt;parameter name="facility" value="Hongkong CURA Healthcare Center" /&gt;{"\n"}{"        "}&lt;parameter name="visitDate" value="27/12/2016" /&gt;{"\n"}{"        "}&lt;parameter name="comment" value="Please make appointment as soon as possible." /&gt;{"\n"}{"        "}&lt;classes&gt;{"\n"}{"            "}&lt;class name="com.katalon.kata.sample.testcase.parameterize.ParameterizedMakeAppointmentTest" /&gt;{"\n"}{"        "}&lt;/classes&gt;{"\n"}{"    "}&lt;/test&gt;{"\n"}&lt;/suite&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test suites can be specified in command line, e.g. <code className="ph codeph">mvn     clean test     -Dsurefire.suiteXmlFiles=src/test/resources/testng-parallel.xml</code>.</p> 
