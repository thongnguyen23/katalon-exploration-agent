---
hide_title: true
title: Generate groovy doc for a plugin on Katalon Store
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Generate groovy doc for a plugin on <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Beside publishing your plugin to <span className="ph">Katalon Store</span>, you can generate   your documentation into groovydoc and add to store.</p> 

## <a id="id_1" class="anchor_top_offset"/>Add documentation title to <code xmlns="http://www.w3.org/1999/xhtml" className="ph codeph">build.gradle</code>     
     
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In your project, open build.gradle file and update   <code className="ph codeph">docTitle</code>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Let’s refer to the following example:</p> 
              
```jsx
groovydoc {
    source = pluginSources
    docTitle = 'WaitForAngularLoad Custom Keywords'
}
```

## <a id="id_2" class="anchor_top_offset"/>Add dependencies to <code xmlns="http://www.w3.org/1999/xhtml" className="ph codeph">build.gradle</code>     

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add dependencies to <code className="ph codeph">build.gradle</code>   (optional). Let’s refer to the following example to add   dependencies:</p> 

```jsx
dependencies {
    compile('com.paulhammant:ngwebdriver:1.1.4') {
        exclude group: 'org.seleniumhq.selenium'
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you don't have the dependencies, delete the command lines.</p> 

## <a id="concept-1739" class="anchor_top_offset"/>How to build

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Run the following command at the root folder:<pre className="pre codeblock"><code>gradle groovydoc -x compileGroovy</code></pre></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After successfully running the command, there will be the "build" folder displayed in your plugin package.</p> 

## <a id="id_3" class="anchor_top_offset"/>Add the project to katalon-plugin-docs repository

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Go to     <code className="ph codeph">katalon-plugin-docs/katalon-plugin-docs.github.io/</code>   </li><li className="li">Upload your file to “docs” folder</li><li className="li">Create a pull request and wait for approval</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example of the AngularJS Dropdown Keywords successfully added to   Git: <a className="xref j-external-link" href="https://github.com/katalon-plugin-docs/katalon-plugin-docs.github.io/tree/master/docs/angularjs-dropdown-custom-keywords" target="_blank">AngularJS Dropdown custom keyword</a>.</p> 
