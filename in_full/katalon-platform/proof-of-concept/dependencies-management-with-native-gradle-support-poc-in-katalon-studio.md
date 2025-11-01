---
hide_title: true
title: Dependencies Management with Native Gradle Support in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Dependencies Management with Native Gradle Support in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

:::tip requirements
This Proof of Concept (PoC) is not ready for production use. We recommend using this PoC for evaluation purposes only.
:::

Previously, Katalon Studio provides a [Gradle Plugin](https://plugins.gradle.org/plugin/com.katalon.gradle-plugin) to simplify and automate some tasks in Katalon Studio. However, some users find it cumbersome, and dependencies management is pretty bare-bones.

Empowered by [Buildship](https://www.eclipse.org/community/eclipse_newsletter/2018/february/buildship.php), an Eclipse plugin, the Gradle wrapper and native Gradle integration in Katalon Studio makes dependencies management with Maven or Gradle more streamlined and robust. You are no longer required to use any Command-line or third-party tools and free to decide which Gradle version to use in your test project instead of being limited to use only the fixed version that you have installed on your local machine earlier.

This feature is particularly beneficial to Katalon users who use external libraries in multiple test projects and prefer to use Gradle for managing their build process. You can now run Gradle tasks in a better editor without installing Gradle in Katalon Studio or using an external terminal/command prompt. It substantially reduces your manual effort when you can manage and download external libraries in fewer steps than before.

This manual introduces what built-in Gradle support looks like and how to use it in Katalon Studio.

**Note**: Download Katalon Studio v8.0.0.rc from our GitHub repository: [Katalon Studio v8.0.0.rc](https://github.com/katalon-studio/katalon-studio/releases/tag/v8.0.0.rc).

## <a id="id_1" class="anchor_top_offset"/>Gradle Settings in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

Katalon Studio turns on the built-in Gradle integration by default for all projects.

:::info notes
When you create/open a project for the first time, it takes 2 to 5 minutes to download Gradle.
:::
You can access Gradle settings by going to **Katalon Studio > Preferences > Gradle**.
<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/gradle-preferences.png" alt="Graddle Preferences" /> <br/>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To change the Gradle settings of an opening project, go to <strong className="ph b">Project</strong> &gt; <strong className="ph b">Properties</strong> &gt; <strong className="ph b">Gradle</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/project-menu.png")} width={250} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/project.png")} /><br /><br /> </p> 

## <a id="id_2" class="anchor_top_offset"/>Gradle Tasks in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To use Gradle tasks in <span className="ph">Katalon Studio</span>, open the <strong className="ph b">Gradle Tasks</strong> tab at the bottom dock:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/gradle-tasks.png")} width={600} /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">To sync Gradle tasks when you change the <code className="ph codeph">build.gradle</code> file, on the top right corner, click the <strong className="ph b">Refresh Tasks for All Projects</strong> button.</p>   </li><li className="li">     <p className="p">To view and use Katalon Gradle tasks, on the top right corner, click on the three-dot button and select <strong className="ph b">Show All Tasks</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/context-menu.png")} width={500} /><br /><br />     </p>     <p className="p">All Katalon Tasks are available under the <strong className="ph b">other</strong> category of the Gradle task tree:</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/gradle/other-gradle.png")} /><br /><br />     </p>   </li><li className="li">     <p className="p">Click on any item on the Gradle task tree to run the dedicated Gradle tasks. For the <strong className="ph b">katalonCopyDependencies</strong> task, you need to select <strong className="ph b">Project</strong> &gt; <strong className="ph b">Refresh</strong> to refresh the project classpath after successfully running the task.</p>   </li></ul> 

## <a id="id_3" class="anchor_top_offset"/>Usage Examples of katalonCopyDependencies task in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">On Tests Explorer, open the <code className="ph codeph">build.gradle</code> file, in   its editor:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">You can use <code className="ph codeph">compile</code> to add dependencies to a     project:<pre className="pre codeblock"><code>compile 'io.rest-assured:json-schema-validator:3.2.0'{"\n"}</code></pre></li><li className="li">Use the following command to exclude dependencies:<pre className="pre codeblock"><code>compile ('io.rest-assured:json-schema-validator:3.2.0') {"{"}{"\n"}{"    "}exclude group: 'org.hamcrest', module: 'hamcrest-core' {"\n"}{"}"}{"\n"}</code></pre></li></ol> 
