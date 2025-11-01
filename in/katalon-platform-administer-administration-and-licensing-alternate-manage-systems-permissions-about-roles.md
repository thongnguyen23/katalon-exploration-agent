---
hide_title: true
title: About Roles
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-3410" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>About Roles

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">All roles are predefined by Katalon and are not editable nor removable. </p></li></ul></div></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Role is a named template that is comprised of a combination of <a className="xref" href="/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles">permissions</a>. It determines what specific actions a User can perform within <span className="ph">Katalon TestOps</span>. A User can hold multiple roles. </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">They come in two types. In hierarchical order, they are:<ul className="ul"><li className="li"><p className="p">Account Level Roles</p></li><li className="li"><p className="p">Project Level Roles</p></li></ul> </div>

## About Account Level Roles 

<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__About-Account-Level-Roles">Account Level Roles are for operational administrators who need access to settings that encompass the entirety of the Account, such as those found within the Account, Organization, and System sections of <span className="ph">Katalon TestOps</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" width={500} src={useBaseUrl("/9cf28297-5293-4d75-af7d-c1b014bd2daf/TO3B2_Account_Level_Roles.png")} alt="Account Level Roles cover the Account, Organization, and System sections within TestOps Gen 3." /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv">There are three types of Account Level Roles:</div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-account-admins">1. <strong className="ph b">Account Admins</strong> <u className="ph u">hold the highest level of permissions for all features</u>. Their main responsibilities include managing the <span className="ph uicontrol">Account</span> and <span className="ph uicontrol">Organization</span> sections, granting them authority over the following functions: </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">In the Account section:</p><ul className="ul"><li className="li"><p className="p">General account information and settings</p></li><li className="li"><p className="p">License management</p></li><li className="li"><p className="p">License utilization</p></li></ul></li></ul><ul className="ul"><li className="li"><p className="p">In the Organization section: </p><ul className="ul"><li className="li"><p className="p">Organization management</p></li><li className="li"><p className="p">Portfolio management</p></li><li className="li"><p className="p">User management</p></li></ul></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-system-admins">2. <strong className="ph b">System Admins</strong> are afforded the highest level of permissions with regards to settings concerning the <span className="ph uicontrol">System</span> section. They can affect:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">General system settings</p></li><li className="li"><p className="p">User role and permission management</p></li><li className="li"><p className="p">System configurations</p></li><li className="li"><p className="p">System integrations</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-users">3. <strong className="ph b">Users</strong> are not afforded any permissions and is the default role everyone is assigned to when first joining an Account. Each user is exclusively affiliated with a single Organization (unless removed), and can be added to any Project across Organizations. </p> 

## About Project Level Roles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Project Level Roles are for Project admins and users who need access to settings or features that directly interact with the testing cycle or its elements. They are limited to affecting settings within the <span className="ph uicontrol">Project</span> section, and can manage multiple Projects. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/715f6b04-0343-4f45-9a04-5ef61c2f38bc/TO3B2_Project_Level_Roles.png")} alt="Project Level Roles cover the Project section within Katalon TestOps Gen 3." /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv">There are four types of Project Level Roles:</div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-project-admins">1. <strong className="ph b">Project Admins</strong> possess the highest level of permissions within this role type. They preside over the <span className="ph uicontrol">Project</span> section, which allow them to manage the following settings: </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">General project settings</li><li className="li"><p className="p">Script repository configuration</p></li><li className="li"><p className="p">Project configurations</p></li><li className="li"><p className="p">Project integrations</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-test-leads">2. <strong className="ph b">Test Leads </strong>are fully authorized to manage all relevant features related to the elements within a Project, such as test management, releases, or reports and analytics.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-testers">3. <strong className="ph b">Testers </strong>are partially authorized to manage all relevant features related to the elements within a Project, similar to those with the Test Lead role. The difference is they only have read-only access for certain features. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p anchor_top_offset" id="concept-3410__about-members">4.<strong className="ph b"> Members </strong>are limited to read-access level permissions for all features. </p> 
