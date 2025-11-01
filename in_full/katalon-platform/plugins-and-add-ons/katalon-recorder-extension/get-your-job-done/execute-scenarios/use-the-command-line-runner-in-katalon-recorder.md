---
hide_title: true
title: Use the Command-Line Runner in Katalon Recorder
---

# <a id="id_Use-the-Command-Line-Runner" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use the Command-Line Runner in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 


## <a id="id" class="anchor_top_offset"/>Use the Command-Line Runner

You can now execute tests in Katalon Recorder directly from the command line using the [Command-Line runner](https://www.npmjs.com/package/katalon-recorder-cli) (KR CLI)

:::tip requirements
- node version 8 or 10.
- npm.
- kr-cli.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are using Homebrew to manage dependencies, run the   following script:</p> 
        
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>brew install node</code></pre></div>
        
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>npm i -g katalon-recorder-cli</code></pre></div>
      
## <a id="id_1" class="anchor_top_offset"/>Using KR CLI as a tester

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are a tester, you can integrate KR tests into the CI/CD   pipeline to execute them at specific time intervals, or by defining   custom triggers.</p> 

### <a id="id_2" class="anchor_top_offset"/>Executing a test suite

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Copy the following command:     <div className="p">       <pre className="pre codeblock"><code>kr-cli run &lt;browser&gt; &lt;pathToHtmlFile&gt; --report=&lt;pathToReportFolder&gt;</code></pre>     </div>   </li><li className="li">Replace:<ul className="ul"><li className="li">         <p className="p">           <code className="ph codeph">pathToHtmlFile</code> with the absolute path to your KR           test suite.</p>       </li><li className="li">         <p className="p">           <code className="ph codeph">browser</code> with either chrome or firefox.</p>       </li><li className="li">         <p className="p">           <code className="ph codeph">pathToReportFolder</code> with the absolute path to an           existing folder</p>       </li></ul></li><li className="li">Execute the command.</li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After executing the command, a report file with a .csv extension   and a log file with a .log extension will be generated at the   specified report folder.</p> 

### <a id="id_3" class="anchor_top_offset"/>Executing a test suite with data files

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Copy the following command:<div className="p">       <pre className="pre codeblock"><code>kr-cli run &lt;browser&gt; &lt;pathToHtmlFile&gt; --report=&lt;pathToReportFolder&gt; --data=&lt;pathToData1&gt;</code></pre>     </div></li><li className="li">Replace:<ul className="ul"><li className="li">         <p className="p">           <code className="ph codeph">pathToHtmlFile</code> with the absolute path to your KR           test suite.</p>       </li><li className="li">         <p className="p">           <code className="ph codeph">browser</code> with either chrome or firefox.</p>       </li><li className="li">         <p className="p">           <code className="ph codeph">pathToReportFolder</code> with the aboluste path to an           existing folder.</p>       </li><li className="li">         <p className="p">           <code className="ph codeph">pathToData1</code> with the absolute path to your data           file.</p>       </li></ul></li><li className="li">Execute the command.</li></ol> 
                  
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If your test suite uses multiple data files, separate the paths   with a comma.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A report file with a .csv extension and a log file with a .log   extension will be generated at the specified report folder.</p> 
    

## <a id="id_4" class="anchor_top_offset"/>Using KR CLI as a developer

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are a developer, you can integrate KR tests into your   development process to ensure that your code doesn't break   important user experiences.</p> 
    
### <a id="id_5" class="anchor_top_offset"/>Executing all test suites in a project

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Place all KR test suites under folder /tests/kr-test in your       NodeJS project.</p>   </li><li className="li">     <p className="p">Copy the following command:</p><p className="p">       <code className="ph codeph">kr-cli dev &lt;browser&gt; --lg</code>     </p>   </li><li className="li">     <p className="p">Replace browser with chrome or firefox.</p>   </li><li className="li">     <p className="p">Execute the command.</p>   </li></ol> 

:::info notes
- By default, no report or log files are generated when running commands in development mode. Instead, An overview of test execution will be printed directly to your command line tool.

- Specify --lg to print the logs to your command line tool during test execution.
:::
