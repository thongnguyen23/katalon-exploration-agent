---
title: Manage Katalon Licenses (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After purchasing <span className="ph">Katalon Studio Enterprise (KSE)</span> and/or <span className="ph">Katalon Runtime Engine (KRE)</span> licenses, you can attribute, transfer, and remove granted licenses from <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon TestOps</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">You must be the Owner or Admin of your Organization to access the <strong className="ph b">License Management</strong> page. For further details on roles and user management, see: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-users">User Management</a>.</li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="note warning note_warning"><span className="note__title">Warning:</span> <ul className="ul"><li className="li"><p className="p">The Owner or Admin of an Organization needs to assign a paid license to all of their users to avoid mixed <span className="ph">Katalon Studio</span> and <span className="ph">Katalon Studio Enterprise</span> licenses within an organization. For further information, refer to the <strong className="ph b">Free Offerings</strong> term in <a className="xref j-external-link" href="https://katalon.com/terms#customer-terms-of-use" target="_blank">Terms of Use</a>.</p></li></ul></div>

## <a id="id_1" class="anchor_top_offset"/>View license information

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">You must be the Owner or Admin of your Organization to access the <strong className="ph b">License Management</strong> page. If you do not have it, you can ask your account owner for this permission. See: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-users#change-user-role">Change user role</a>.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can verify the subscription information and view all license information by following these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">Sign in to <a className="xref j-external-link" href="https://my.katalon.com/" target="_blank">TestOps Admin</a> and select your Account.</p></li><li className="li"><p className="p">On the Account admin page, select your Organization.</p></li><li className="li"><p className="p">Select <span className="ph uicontrol">License</span> to open the <span className="ph uicontrol">License Management</span> page.</p></li><li className="li"><p className="p">Select a Katalon product. For example, <span className="ph uicontrol">Katalon Studio Enterprise (per-User)</span>. The page displays as below.</p><p className="p"><img className="image" src={useBaseUrl("/10825190-bf7c-11ee-ac6d-0242c7a41fd4/KT-_License_Management_page.png")} /></p><ul className="ul"><li className="li"><p className="p">In the <strong className="ph b">Subscription Details</strong> section, you can see the following information:</p><ul className="ul"><li className="li"> <strong className="ph b">Subscribed Licenses</strong>: the total number of licenses you have purchased, also known as your license quota.</li><li className="li"><p className="p"> <strong className="ph b">Available Licenses</strong>: the remaining licenses you can use.</p><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Licenses attributed online, as well as offline licenses you have generated, are subtracted from your license quota.</li></ul></div></li><li className="li"><strong className="ph b">Machine Quota</strong>: the maximum number of machines that can be registered with your licenses. </li><li className="li"><strong className="ph b">Expiry Date</strong>: the date when your licenses expire. </li></ul></li><li className="li"><p className="p">In the <strong className="ph b">Licensed Users</strong> section, you can add users for license usage. You can also view a list of users you have added for license usage.</p></li><li className="li"><p className="p">In the <strong className="ph b">Online Licenses</strong> section, you can see a list of active machine IDs (users who are currently using the licenses online).</p></li><li className="li"><p className="p">In the <strong className="ph b">Offline Licenses</strong> section, you can see a list of machine IDs bound to offline licenses.</p></li><li className="li"><p className="p">In the <strong className="ph b">Registered Machines</strong> section, you can see a list of all machine IDs that are using either types of licenses.</p></li></ul></li></ol> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Contact us at license@katalon.com if you need further help with your licenses.</li></ul></div>

## <a id="id_2" class="anchor_top_offset"/>Grant a license to users

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can assign licenses to users. See <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/grant-a-katalon-license#task-1443">Grant a License to users</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Once you have assigned a license successfully, users can follow this activation guide: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate Katalon License</a>.</p> 

## <a id="id_3" class="anchor_top_offset"/>Remove a license

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can remove a Licensed User, a machine ID, or a license from a machine ID. See <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/remove-a-license#task-5047">Remove the KSE license from assigned user</a>.</p> 

## <a id="task-2705" class="anchor_top_offset"/>Transfer a license between users

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Transferring licenses ensures an organization's users can pass licenses between each other as needed. Users without a license attributed to them can still have the privileges of a free plan.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">To transfer a KRE license, simply terminate the session currently using it. It will then be available for use again.</p></li></ul></div>Licenses can be transferred between users as long as the organization does not exceed its license quota. To do so, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">Removing a license from the user associated with it. For a more detailed explanation, see: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/remove-a-license#task-5047">Remove the KRE license from assigned users</a>. </span></li><li className="li step"><span className="ph cmd">Reassign the license by granting it again from the <span className="ph uicontrol">License Management</span> page. For more details, see: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/grant-a-katalon-license#task-1443">Grant an online license to users</a>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have transferred your license between users. <div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">To remove a KRE license, simply terminate the session currently using it. It will then be available for use again.</p></li></ul></div> <div className="note trouble note_trouble"><span className="note__title">Trouble:</span> <ul className="ul"><li className="li"><p className="p">If you are encountering errors regarding your license usage, see this troubleshooting document: <a className="xref" href="/katalon-platform/troubleshooting/troubleshooting-common-administrative-issues/the-number-of-the-licenses-cannot-exceed-the-license-quota">The number of the licenses cannot exceed the license quota</a>.</p></li></ul></div></section> 
      

### <a id="id_5" class="anchor_top_offset"/>Transfer the KRE license to another machine

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All licensed Users in an Organization can use available KRE   licenses by default once the Organization has purchased the KRE   licenses.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Licensed Users activate a KRE license by running KSE with KRE.   After activation, their machine ID is then added to the   <strong className="ph b">Online Licenses</strong> section. This license is then   reserved for their use.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Therefore, to make a KRE license available when all licenses are   reserved, a machine ID has to be deactivated.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To deactivate a machine ID, see: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/remove-a-license#id_3">Remove     a registered machine ID</a>.</p> 
      
    
