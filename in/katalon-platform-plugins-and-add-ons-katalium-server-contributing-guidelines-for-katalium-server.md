---
hide_title: true
title: Contributing Guidelines for Katalium Server
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Contributing Guidelines for Katalium Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Server is open-sourced at   <code className="ph codeph">https://github.com/katalon-studio/katalium-server</code>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Frontend

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The GUI of Katalium Server is built with ReactJS and <a className="xref j-external-link" href="https://github.com/facebook/create-react-app" target="_blank">Create React     App (CRA)</a>. This GUI is only enabled in Grid mode.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The recommended NodeJS version is <code className="ph codeph">10.16.0</code> or   newer.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Executing the following commands to start:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>cd web{"\n"}npm install{"\n"}npm run start{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">CRA scripts will start a server at <code className="ph codeph">http://localhost:3000</code> with   API requests forwarded to Selenium Grid at   <code className="ph codeph">http://localhost:4444</code>.</p> 

## <a id="id_2" class="anchor_top_offset"/>Backend

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Importing as Maven project into <code className="ph codeph">IntelliJ IDEA</code>,   <code className="ph codeph">Visual Studio Code</code> or <code className="ph codeph">Eclipse</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To start the server in standalone mode, use entry class   <code className="ph codeph">com.katalon.kata.server.KatalonServer</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To start the server as a hub, use entry class   <code className="ph codeph">com.katalon.kata.server.KatalonServer</code> with arguments   <code className="ph codeph">-role hub -servlets     com.katalon.kata.servlet.ListSessionsServlet,com.katalon.kata.servlet.KatalonConsole,com.katalon.kata.servlet.ScreenShotsServlet,com.katalon.kata.servlet.ConfigSessionsServlet,com.katalon.kata.servlet.SessionServlet</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To start the server as a node, use entry class   <code className="ph codeph">com.katalon.kata.server.KatalonServer</code> with arguments   <code className="ph codeph">-role node -hub http://localhost:4444/grid/register -proxy     com.katalon.kata.proxy.KatalonProxy</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-server/docs/katalium-contributing/1-katalium.png")} /><br /><br /> </p> 
    

## <a id="id_3" class="anchor_top_offset"/>Package

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For more detailed infomation please refer to   <code className="ph codeph">Jenkinsfile</code>.</p> 
    
  

## <a id="id_4" class="anchor_top_offset"/>References

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Selenium Grid   <code className="ph codeph">https://www.seleniumhq.org/docs/07_selenium_grid.jsp</code>.</p> 
