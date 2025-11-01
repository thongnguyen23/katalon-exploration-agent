---
hide_title: true
title: Import and export keywords in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Import and export keywords in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph">Katalon Studio</span>, you can import and export custom keywords across projects for quicker and easier management. This feature minimizes the risk of moving test artifacts across different test projects.</p> 

## <a id="id_1" class="anchor_top_offset"/>Import keywords

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Currently, <span className="ph">Katalon Studio</span> provides two options to import keywords: from a local folder or from a Git repository.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To import new keywords, navigate to <span className="ph uicontrol">Menu</span> &gt; <span className="ph uicontrol">File</span> &gt; <span className="ph uicontrol">Import Keywords</span> and choose your preferred option. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/4c4aef10-340a-11ed-9930-0242fe3e4a3f/ks-se-import-keyword-in-file.png")} alt="Import keywords into Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Additionally, you can import keywords from the <strong className="ph b">Tests Explorer</strong> by right-clicking on the <strong className="ph b">Keywords</strong> folder and choose <span className="ph uicontrol">Import</span> &gt; <span className="ph uicontrol">Folder</span> or <span className="ph uicontrol">Git</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={400} src={useBaseUrl("/02c585d0-340a-11ed-9930-0242fe3e4a3f/ks-se-850-import-keyword.png")} alt="Import keywords from Test Explorer in Katalon Studio." /></p> 

### <a id="id_2" class="anchor_top_offset"/>Import from a local folder

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/d5c63f10-340a-11ed-9930-0242fe3e4a3f/ks-850-se-folder.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After the <span className="ph uicontrol">Browse For Folder</span> panel appears, choose your desired folder to import the keywords to <span className="ph">Katalon Studio</span>. If the keywords imported don't belong to any package, <span className="ph">Katalon Studio</span> puts them into a default package.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/97c8b070-340b-11ed-9930-0242fe3e4a3f/ks-se-850-keywords-folder.png")} alt="Default package of keywords in Katalon Studio." /></p> 

### <a id="id_3" class="anchor_top_offset"/>Import from Git 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If the user is importing the keywords from a public repository,   <strong className="ph b">NO</strong> authentication is <strong className="ph b">required</strong>.   However, if the repository is private, please provide your Git   authentication. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" width={600} src={useBaseUrl("/76a3c690-340c-11ed-9930-0242fe3e4a3f/ks-850-se-clone-git-repository.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When Katalon Studio successfully discovers the desired   repository, it will ask the user to choose a branch to check out.   Please select the branch that contains the keywords you want to   import. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" width={600} src={useBaseUrl("/068ddba0-340e-11ed-9930-0242fe3e4a3f/ks-850-clone-git-repository.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio will clone the Git repository to a default   location in your project folder. Choose your initial   branch and click <strong className="ph b">Finish.</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" width={600} src={useBaseUrl("/5f536200-340e-11ed-9930-0242fe3e4a3f/ks-850-local-destination.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio will notify you whether the keywords are imported   successfully. If the keywords imported don't belong to any package,   Katalon Studio will put them into a <strong className="ph b">default</strong>   package.</p> 

### <a id="id_4" class="anchor_top_offset"/>Duplicate keywords

<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are instances of similar keywords exist in the project. Katalon Studio will automatically detect and alert users for taking actions. There are 3 options to choose as shown below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/importexport-keywords/image2018-6-21-113A463A12.png")} /><br /><br /></p> 

## <a id="id_5" class="anchor_top_offset"/>Export keywords

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To increase code usability, Katalon Studio also let you export keyword for sharing across team members. Simply right-click on Keywords in the Tests Explorer, select Export from the context-menu. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={400} src={useBaseUrl("/8e297250-3412-11ed-9930-0242fe3e4a3f/ks-850-se-export.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Browse For Folder</strong> panel displays, choose your desired folder to export the keywords to the local storage.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/e04023c0-3419-11ed-9930-0242fe3e4a3f/ks-se-850-export-file.png")} /></p> 
