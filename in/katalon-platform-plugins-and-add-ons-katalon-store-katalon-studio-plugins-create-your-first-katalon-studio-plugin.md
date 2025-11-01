---
hide_title: true
title: Create your first Katalon Studio plugin
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create your first <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  plugin

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial will walk you through creating your first <span className="ph">Katalon Studio</span> plugin. The plugin in this tutorial does two things:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Listens to the <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-platform/blob/master/com.katalon.platform/src/main/java/com/katalon/platform/api/extension/PluginActivationListener.java" target="_blank">plugin       activation event</a> then prints a hello message after the plugin     was installed successfully in <span className="ph">Katalon Studio</span>.</li><li className="li">Listens to the <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-platform/blob/master/com.katalon.platform/src/main/java/com/katalon/platform/api/extension/EventListenerInitializer.java" target="_blank">test       execution event</a> then prints a report message in Console.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find the source code of this tutorial <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-sample-plugin" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A <span className="ph">Katalon Studio</span> plugin is a Maven-based Java project, and also   an <a className="xref j-external-link" href="http://spring.io/blog/2008/02/18/creating-osgi-bundles/" target="_blank">OSGI     bundle 1</a> project. A plugin contains these components:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">The <code className="ph codeph">pom.xml</code> to describe your plugin, what it is     (name, version, vendor,etc).</li><li className="li">The <code className="ph codeph">plugin.xml</code> to let Katalon Studio know about     all the extensions of your plugin.</li><li className="li">All packaged codes of your plugin.</li></ul> 

## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ol className="ol"><li className="li">Java SDK 1.8</li><li className="li">Maven 3.3+</li><li className="li">Download <span className="ph">Katalon Studio</span> version 6.0.3 (beta): <a className="xref j-external-link" href="https://s3.amazonaws.com/katalon/release-beta/6.0.3/Katalon_Studio_Windows_32.zip" target="_blank">win32</a>,
      <a className="xref j-external-link" href="https://s3.amazonaws.com/katalon/release-beta/6.0.3/Katalon_Studio_Windows_64.zip" target="_blank">win64</a>,
      <a className="xref j-external-link" href="https://s3.amazonaws.com/katalon/release-beta/6.0.3/Katalon+Studio.dmg" target="_blank">macOS</a>,
      and <a className="xref j-external-link" href="https://s3.amazonaws.com/katalon/release-beta/6.0.3/Katalon_Studio_Linux_64.tar.gz" target="_blank">linux64</a>.</li></ol></div>

## <a id="id_2" class="anchor_top_offset"/>      Step 1: Create a Maven-based Java project    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Let's create your Java Maven-based project with project   structure looks like this:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>├─── src/{"\n"}│{"   "}└─── main/{"\n"}│{"       "}├─── java/{"\n"}│{"       "}└─── resources/{"\n"}│{"           "}└─── plugin.xml{"\n"}└─── pom.xml{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">During this tutorial, we are using the example declarations   below. These declarations can be changed depend on your specific   needs:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <strong className="ph b">com.mycompany.plugin</strong> is groupId.</li><li className="li">     <strong className="ph b">my-first-katalon-plugin</strong> is artifactId.</li><li className="li">     <strong className="ph b">com.mycompany.plugin</strong> is the default     package.</li></ul> 

## <a id="id_3" class="anchor_top_offset"/>      Step 2: Update <code xmlns="http://www.w3.org/1999/xhtml" className="ph codeph">pom.xml</code>           

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Update your <code className="ph codeph">pom.xml</code> file with the template   below:</p> 

```html
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.katalon</groupId>
        <artifactId>com.katalon.platform.parent</artifactId>
        <version>1.0.17</version>
    </parent>

    <!-- REPLACE ME: Your plugin description here -->
    <groupId>com.mycompany.plugin</groupId>
    <artifactId>my-first-katalon-plugin</artifactId>
    <version>1.0.0</version>

    <packaging>bundle</packaging>

    <dependencies>
        <!-- Katalon Platform dependencies-->
        <dependency>
            <groupId>com.katalon</groupId>
            <artifactId>com.katalon.platform</artifactId>
            <version>1.0.17</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-dependency-plugin</artifactId>
                <version>2.4</version>
                <executions>
                    <execution>
                        <id>unpack-dependencies</id>
                        <phase>prepare-package</phase>
                        <goals>
                            <goal>unpack-dependencies</goal>
                        </goals>
                        <configuration>
                            <excludes>com/katalon/platform/,org/eclipse/,org/osgi/</excludes>
                            <includes>/.class</includes>
                            <outputDirectory>${project.build.outputDirectory}</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.felix</groupId>
                <artifactId>maven-bundle-plugin</artifactId>
                <extensions>true</extensions>
                <configuration>
                    <instructions>
                        <Bundle-SymbolicName>${project.groupId}.${project.artifactId};singleton:=true</Bundle-SymbolicName>
                        <Bundle-Version>${project.version}</Bundle-Version>
                        <Import-Package></Import-Package>
                        <DynamicImport-Package></DynamicImport-Package>
                        <_noee>true</_noee>
                        <_nouse>true</_nouse>

                        <!-- REPLACE ME: Change your public export package here -->
                        <Export-Package>com.mycompany.plugin*</Export-Package>
                    </instructions>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The tags can be changed under <strong className="ph b">REPLACE ME</strong> if   needed.</p> 

## <a id="id_4" class="anchor_top_offset"/>      Step 3:    

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> allows client plugins to contribute to   <span className="ph">Katalon Studio</span> core features. All of the features are described at   <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-platform/blob/master/com.katalon.platform/plugin.xml" target="_blank">this     link</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are many <code className="ph codeph">extension</code> tags here. Each of these   tags is a <code className="ph codeph">Extension Point</code> describing specifications to   allow client plugins hook into Katalon Studio platform. A plugin   can contribute to many extension points by declaring it in   <code className="ph codeph">plugin.xml</code> file.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, we want to <code className="ph codeph">Subscribe plugin installation     event</code>:</p> 

```html
<extension 
      point="com.katalon.platform.extensions_point">
      <point
            id="com.katalon.platform.api.extension.pluginActivationListener"
            interfaceClass="com.katalon.platform.api.extension.PluginActivationListener"
            serviceClass="com.katalon.platform.internal.lifecycle.PluginActivationListenerService">
      </point>  
</extension>
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Above declarations mean:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">id: the id of the extension point.</li><li className="li">interfaceClass: the required interface class that client     plugins should provide the implementation to extend this     feature.</li><li className="li">serviceClass: an internal service class.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To extend this extension point, we need to declare in   <code className="ph codeph">plugin.xml</code> as shown below:</p> 

```html
<plugin>
      <extension
            point="com.katalon.platform.extensions">
      <point
            id="com.mycompany.plugin.myFirstExtensionId"
            extensionPointId="com.katalon.platform.api.extension.pluginActivationListener"
            implementationClass="com.mycompany.plugin.MyPluginActivationListener">
      </point>
      </extension>
</plugin>
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Above declarations mean:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">id: the unique id of the your extension. You can replace by any     name but it must be unique.</li><li className="li">extensionPointId: the id of the extension point. Simply change     the id if you want to extend other extension points.</li><li className="li">implementationClass: the class that implements the     <code className="ph codeph">interfaceClass</code> mentioned at Step 3. Next, we create     it.</li></ul> 

## <a id="id_5" class="anchor_top_offset"/>      Step 4: Create your            <code xmlns="http://www.w3.org/1999/xhtml" className="ph codeph">implementationClass</code>           

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Create a class file <code className="ph codeph">MyPluginActivationListener</code>   under <code className="ph codeph">src/java/main</code> folder:</p> 

```jsx
package com.mycompany.plugin;

import com.katalon.platform.api.Plugin;
import com.katalon.platform.api.extension.PluginActivationListener;

public class MyPluginActivationListener implements PluginActivationListener {
    // After this plugin is activated, we will print a hello message to console.
    @Override
    public void afterActivation(Plugin plugin) {
        System.out.println("Hello, my plugin is: " + plugin.getPluginId());
    }
}
```

## <a id="id_6" class="anchor_top_offset"/>      Step 5: Build your plugin    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Type <code className="ph codeph">mvn clean package</code> and wait until the   <strong className="ph b">BUILD SUCCESS</strong> message is displayed from the   command line window.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/build-plugin.png")} width={500} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After the build completed, there is a   <code className="ph codeph">my-first-katalon-plugin.jar</code> under the   <code className="ph codeph">target</code> folder, we will need this to launch your plugin   in the next step.</p> 

## <a id="id_7" class="anchor_top_offset"/>      Step 6: Test your plugin    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open Katalon Studio (since 6.0.4) and activate <strong className="ph b">Event     Log</strong> tab that's nearby <code className="ph codeph">Console Log</code> tab. All   your plugin's message will be displayed here.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Launch your plugin by clicking on <strong className="ph b">Plugin/Install     Plugin</strong> menu and choose the jar was mentioned above.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should be able to see the notification message <code className="ph codeph">Plugin     installed successfully</code> from Katalon Studio and the message   <code className="ph codeph">Hello, my plugin is:     com.mycomany.my-first-katalon-plugin</code> is displayed in   <code className="ph codeph">Event Log</code> tab. Success!</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/test-plugin.png")} width={500} /><br /><br /> </p> 

## <a id="id_8" class="anchor_top_offset"/>      Step 7: Create an execution               event extension    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To create an <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-platform/blob/master/com.katalon.platform/src/main/java/com/katalon/platform/api/extension/EventListenerInitializer.java" target="_blank">execution event extension</a>, we go back to <code className="ph codeph">     <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-platform/blob/master/com.katalon.platform/plugin.xml" target="_blank">plugin.xml</a>   </code>   file of Katalon Studio Platform, and find the declaration of   <code className="ph codeph">Subscribe KS execution event</code>:</p> 

```html
<extension
      point="com.katalon.platform.extensions_point">
      <point
            id="com.katalon.platform.api.extension.eventListener"
            interfaceClass="com.katalon.platform.api.event.EventListenerInitializer"
            serviceClass="com.katalon.platform.internal.event.EventListenerService">
      </point>
</extension>
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Now, we need to declare our extension in   <code className="ph codeph">plugin.xml</code> </p> 

```html
<extension
      point="com.katalon.platform.extensions">
      <point
            id="com.mycompany.plugin.myAnotherExtensionId"
            extensionPointId="com.katalon.platform.api.extension.eventListener"
            implementationClass="com.mycompany.plugin.MyExecutionEventListener">
      </point>
</extension>
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">and create <code className="ph codeph">implementationClass</code>:</p> 

```jsx
package com.mycompany.plugin;

import org.osgi.service.event.Event;

import com.katalon.platform.api.event.EventListener;
import com.katalon.platform.api.event.ExecutionEvent;
import com.katalon.platform.api.execution.TestSuiteExecutionContext;
import com.katalon.platform.api.extension.EventListenerInitializer;
public class MyExecutionEventListener implements EventListenerInitializer {

    @Override
    public void registerListener(EventListener listener) {
        listener.on(Event.class, event -> {
            if (ExecutionEvent.TEST_SUITE_FINISHED_EVENT.equals(event.getTopic())) {
                ExecutionEvent eventObject = (ExecutionEvent) event.getProperty("org.eclipse.e4.data");

                TestSuiteExecutionContext testSuiteContext = (TestSuiteExecutionContext) eventObject
                        .getExecutionContext();

                System.out.println("Test execution completed: " + testSuiteContext.getReportId());
            }
        });
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This <code className="ph codeph">implementationClass</code> just prints an execution   completed message to console but you can extend this class to do   more business logics. A good example for this is <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-slack-plugin" target="_blank">Slack     Integration Plugin</a>. You can see how it integrates with Slack   application.</p> 

## <a id="id_9" class="anchor_top_offset"/>      Step 8: Reload your plugin    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Type <code className="ph codeph">mvn clean package</code> and wait until the   <strong className="ph b">BUILD SUCCESS</strong> message is displayed in the command   line window.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on <code className="ph codeph">Plugin/Uninstall Plugin</code> to uninstall your   first loaded plugin.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on <code className="ph codeph">Plugin/Install Plugin</code> and choose the jar   file again.</p> 

## <a id="id_10" class="anchor_top_offset"/>      Step 9: Test execution event    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Run the test suite and wait until the execution finished.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Look at the <code className="ph codeph">Event Log</code> and the message should be   displayed as shown below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/test-execution-event.png")} width={500} /><br /><br /> </p> 
