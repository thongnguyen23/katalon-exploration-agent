---
title: Supported Jira field types (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">When creating a new Jira issue using Report Defect, it may fail if it contains unsupported field-types that are required fields.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/3f164d80-77bb-11ee-8403-0242c7a41fd4/Unsupported_Jira_Field_Types_Error.png")} alt="Report Defect can't create the issue type in TestOps." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> supports the following:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Single type:</p><ul className="ul"><li className="li"> string</li><li className="li"> number</li><li className="li">date</li><li className="li">datetime</li><li className="li">user</li><li className="li">option</li><li className="li">issuetype</li><li className="li">project</li><li className="li">priority</li></ul></li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Multiple type:</p><ul className="ul"><li className="li">array (string)</li><li className="li">array (option)</li></ul></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To resolve this, you can go to Jira and create your ticket there. Then, go back to TestOps to link that issue to the test result. </p> 
