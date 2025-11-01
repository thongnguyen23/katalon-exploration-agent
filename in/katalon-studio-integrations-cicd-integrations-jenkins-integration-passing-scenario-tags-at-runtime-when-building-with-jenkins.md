---
hide_title: true
title: Passing scenario tags at runtime when building with Jenkins
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Passing scenario tags at runtime when building with Jenkins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When running automated tests, you might want to classify   different features and scenarios into different tags for better   management.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial  guides you through how to set your scenario   tags to be executed at runtime when Jenkins Build triggers your   tests.</p> 

## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Jenkins is already installed. See Jenkins documentation on <a className="xref j-external-link" href="https://www.jenkins.io/doc/book/installing/" target="_blank">Installing
        Jenkins</a>.</li><li className="li">Katalon plugin is already installed on Jenkins. See <a className="xref" href="/katalon-platform/integrations/cicd-integrations/jenkins-integration/use-katalon-plugins-for-jenkins-integration/use-katalon-plugins-for-jenkins-integration-on-windowsmacos#id_2">How
        to use Katalon plugin for Jenkins on Windows</a>.</li><li className="li">An active Katalon Runtime Engine license.</li></ul></div>

## <a id="task-8549" class="anchor_top_offset"/>Create Global Variables

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">You can change global variable values in a test suite during     runtime without affecting other test suites. Therefore, using a     global variable as a parameter in the keyword     <code className="ph codeph">runFeatureFolderWithTags</code> can save you time when you     have many tags to manage.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Tests Explorer</span> &gt;       <span className="ph uicontrol">Profiles</span> to open your desired profiles. Click       <span className="ph uicontrol">Add</span> to create a global variable whose values are       tags. See <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Global         Variables</a>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-tag-runtime/globalvariable-tags.png")} width={600} alt="add global variable" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">Write a test case with the following keyword:</span><div className="itemgroup info"><pre className="pre codeblock"><code>runFeatureFolderWithTags(folderRelativePath, tags)</code></pre><ul className="ul"><li className="li">folderRelativePath: the folder relative path that starts from           the current project location.</li><li className="li">tags: the global variable defined in step 1.</li></ul><strong className="ph b">Example</strong>:<pre className="pre codeblock"><code>CucumberKW.runFeatureFolderWithTags('Include/features/BDD Cucumber Tests', GlobalVariable.username){"\n"}</code></pre><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">To learn more about this keyword, see <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/cucumber-keywords/cucumber-run-feature-folder-with-tags">[Cucumber]                 Run Feature Folder with Tags</a>.</p></li></ul></div></div></li><li className="li step stepexpand"><span className="ph cmd">Add this test case to a test suite and execute it from Jenkins.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">With the global variable created, you can choose which feature   files folder to run with your desired tags values.</section> 
    

## <a id="id_2" class="anchor_top_offset"/>Update Global Variables during runtime

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To change the global variable by your desired scenario tags   during runtime, use the following command syntax   <code className="ph codeph">-g_XXX</code>, for example,   <code className="ph codeph">-g_userName="admin"</code>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Read more about running Cucumber feature files at <a className="xref" href="/katalon-platform/integrations/integrations-in-katalon-platform#id_cucumber-features-file">BDD     Testing Framework (Cucumber integration)</a>.</p> 
    
  
