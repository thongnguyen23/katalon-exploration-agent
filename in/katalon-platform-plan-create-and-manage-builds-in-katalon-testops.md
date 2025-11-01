---
title: Create and manage builds in Katalon TestOps (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />
<p xmlns="http://www.w3.org/1999/xhtml" className="p">During the release cycle, you commonly need to test different   builds to easily track production issues. In TestOps, the Build   function allows you to associate and orchestrate the test runs   relevant to each build.</p> 

## <a id="id_1" class="anchor_top_offset"/>Create a build  
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Sign in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon         TestOps</a> and go to your Project.</p>   </li>   <li className="li">     <p className="p">Go to <strong className="ph b">Planning</strong> &gt;       <strong className="ph b">Releases</strong>.</p>   </li>   <li className="li">     <p className="p">Select a Release (e.g., <strong className="ph b">7.3.7</strong>).</p>     <p className="p">The <strong className="ph b">Test Cases</strong> page of the       <strong className="ph b">7.3.7</strong> Release appears as below.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/builds/create-build-2.png")} alt="create build button" /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Click on the <strong className="ph b">Create Build</strong> button at the top       right corner.</p>     <p className="p">The <strong className="ph b">Create Build</strong> page appears.</p>   </li>   <li className="li">     <p className="p">Fill in the required information.</p>     <ul className="ul">       <li className="li">         <strong className="ph b">Name</strong>: enter the Build's name.</li>       <li className="li">         <strong className="ph b">Description</strong>: add a note about your Build.</li>       <li className="li">         <strong className="ph b">Date</strong>: enter the creation date for this         Build.</li>     </ul>   </li>   <li className="li">     <p className="p">Click <strong className="ph b">Create</strong>.</p>   </li> </ol> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You have created a new Build. This Build now appears in the   <strong className="ph b">Builds</strong> section of the <strong className="ph b">7.3.7</strong>   Release.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/builds/build-list-2.png")} alt="builds section" /><br /><br /> </p> 
    
      

### <a id="id_2" class="anchor_top_offset"/>Link Test Runs to a build

You can link a Test Run to a Build (or a Release). See: [Link Test Runs to a Release](/katalon-platform/plan/link-test-runs-to-a-release-in-testops).

:::tip tips
You can link multiple Test Runs to a Build.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After linking, you can view the linked Test Runs on the Build page.</p> 

## <a id="id_3" class="anchor_top_offset"/>Manage a build
### <a id="id_4" class="anchor_top_offset"/>View a build   
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Go to <strong className="ph b">Planning</strong> &gt;       <strong className="ph b">Releases</strong>.</p>   </li>   <li className="li">     <p className="p">Select a Release.</p>   </li>   <li className="li">     <p className="p">Scroll down to view a list of Builds in the       <strong className="ph b">Builds</strong> section.</p>   </li>   <li className="li">     <p className="p">Select a Build.</p>     <p className="p">The Build page appears.</p>     <p className="p">You can view a list of Test Runs you have linked to this       Build.</p>     <p className="p">You can also see all Test Cases associated with this Build.</p>   </li> </ol> 

### <a id="id_5" class="anchor_top_offset"/>Update a build       
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Go to <strong className="ph b">Planning</strong> &gt;       <strong className="ph b">Releases</strong>.</p>   </li>   <li className="li">     <p className="p">Select a Release.</p>   </li>   <li className="li">     <p className="p">Scroll down to view a list of Builds in the       <strong className="ph b">Builds</strong> section.</p>   </li>   <li className="li">     <p className="p">Click on the <em className="ph i">Extension</em> icon of the Build you want to       update.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/testops-new/katalon-analytics/docs/build/build-edit-delete.png")} alt="edit build" /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Click <strong className="ph b">Edit</strong>.</p>   </li>   <li className="li">     <p className="p">Update the Build's information.</p>   </li>   <li className="li">     <p className="p">Click <strong className="ph b">Save</strong>.</p>   </li> </ol> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You have updated a Build.</p> 

### <a id="id_6" class="anchor_top_offset"/>Delete a build

1. Go to **Planning > Releases**.
2. Select a Release.
3. Scroll down to view a list of Builds in the **Builds** section.
4. Click on the Extension icon of the Build you want to delete.
5. Click **Delete**.
  The **Delete Build** box pops up as below.

  <img src="https://raw.githubusercontent.com/katalon-studio/docs-images/testops-new/katalon-analytics/docs/build/build-delete.png" alt="edit build" /> <br/>

6. Click **Delete** to confirm your action.

:::warning notice
You cannot undo this action.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See also: <a className="xref" href="/katalon-platform/plan/create-and-edit-releases-in-testops">Manage Test Runs by Release</a>.</p> 
