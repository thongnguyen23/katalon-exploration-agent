---
hide_title: true
title: Share test reports via email in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Share test reports via email in Katalon Studio

:::tip requirements
An active Katalon Studio Enterprise license.
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After a test suite or test suite collection execution, you might want to automatically send summary reports to your own email or other stakeholders to notify them about the test result. This document shows you how to set up your mail server and customize email reports to automatically send out a summary report email whenever a test execution finishes.</p> 

## Email settings

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon Studio, go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Email</span> to configure email server settings. You can also customize the email template and choose which types of report files to be sent as attachments, for example, HTML, CSV, PDF, Log, or PNG.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-settings/KS-Project-Settings-Email.png")} alt="Email settings" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, after you successfully set up your mail server, sender, and recipients, Katalon Studio sends all email reports for test suite executions, including test suites inside a test suite collection.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As an exclusive feature for Katalon Studio Enterprise, you have an option to keep your mailbox tidy by only sending email reports for test suite collection executions and skipping all emails for test suites stored inside that test suite collection. This option is useful when executing test suite collections containing many test suites.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/Test%20report/ks-1010-sending-email-report-options.jpg")} width={700} alt="Email settings" /><br /><br /></p> 

## Mail server settings

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph uicontrol">Mail Server Settings</span> define the mail server Katalon Studio uses for sending emails. To set up your mail server, you need to fill in your mail server host, port, credentials, and choose a protocol option.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">Host and Port</span>:</p><ul className="ul"><li className="li"><span className="ph uicontrol">Host</span>: The domain name of the mail server.</li><li className="li"><span className="ph uicontrol">Port</span>: The port to be used for that server.</li></ul><p className="p">Below is a list of some common outgoing mail (SMTP) server configurations:</p></li></ul> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id__568b6df7-d7cd-40c8-99c8-bf812456b32d"><caption /><colgroup><col /><col /><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1">Email sever</th><th className="entry anchor_top_offset" id="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2">Host</th><th className="entry anchor_top_offset" id="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3">Port</th><th className="entry anchor_top_offset" id="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4">Reference</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">Gmail</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><code className="ph codeph">smtp.gmail.com</code></td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">465 or 587</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><a className="xref j-external-link" href="https://support.google.com/mail/answer/7126229" target="_blank">Check Gmail through other email platforms</a></td></tr><tr className><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">Outlook</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><code className="ph codeph">smtp.office365.com</code></td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">587 or 25</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><a className="xref j-external-link" href="https://docs.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365" target="_blank">How to set up a multifunction device or application to send email using Microsoft 365 or Office 365</a></td></tr><tr className><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">Yahoo! Mail</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><code className="ph codeph">smtp.mail.yahoo.com</code></td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 ">465</td><td className="entry" headers="id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__1 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__2 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__3 id__568b6df7-d7cd-40c8-99c8-bf812456b32d__entry__4 "><a className="xref j-external-link" href="https://help.yahoo.com/kb/SLN4724.html" target="_blank">POP access settings and instructions for Yahoo Mail</a></td></tr></tbody></table> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">Username and Password</span>:</p><ul className="ul"><li className="li"><span className="ph uicontrol">Username</span>: Your full email account to authenticate with the server (e.g., yourusername@gmail.com)</li><li className="li"><span className="ph uicontrol">Password</span>: Your email password to authenticate with the server. This could be a password generated from App Passwords.</li></ul><p className="p">For Gmail users:</p><ul className="ul"><li className="li">If your email accounts are using two-step authentication, you can use Google App Passwords to set up a Gmail account in Katalon Studio. An App Password is a 16-digit passcode that gives Katalon Studio permission to access your Google Account. In the <strong className="ph b">Select app</strong> dropdown of App Passwords, select the option <strong className="ph b">Other (Custom name)</strong> to generate an app password for Katalon Studio. Then, use the generated passwords to put in the password section of <strong className="ph b">Mail Server Settings</strong>. For details, see Google Account Help documentation: <a className="xref j-external-link" href="https://support.google.com/accounts/answer/185833" target="_blank">Sign in with App Passwords</a>.</li><li className="li">If you do not use two-step authentication, you can allow less secure apps to access your account. However, to help keep your account secure, starting May 30, 2022, ​​Google will no longer support the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password. For detail, see Google Account Help documentation: <a className="xref j-external-link" href="https://support.google.com/accounts/answer/6010255" target="_blank">Less secure apps &amp; your Google Account</a>.</li></ul><p className="p">For Yahoo! Mail, make sure to allow less secure apps to access your account. Follow this guide: <a className="xref j-external-link" href="https://help.yahoo.com/kb/account/SLN27791.html" target="_blank">Ways to securely access Yahoo Mail</a>.</p><p className="p">As some SMTP servers do not require authentication and username in email address format, Katalon Studio does not validate usernames and passwords.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Protocol</span>: The protocol to communicate with the mail server. There are three options:</p><ul className="ul"><li className="li">None</li><li className="li">SSL (Secure Sockets Layer)</li><li className="li">TLS (Transport Layer Security)</li></ul></li><li className="li"><p className="p"><span className="ph uicontrol">Encrypt authentication data</span>: For sensitive data protection, we recommend enabling <span className="ph uicontrol">Encrypt authentication data</span>.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you fill in your mail server information, you can send a test email to check if the mail server is set up correctly. Input an email in the <span className="ph uicontrol">Recipients</span> field, then click <span className="ph uicontrol">Send Test Email</span>. The <span className="ph uicontrol">Send test email</span> button is only enabled once <span className="ph uicontrol">Mail Server Settings</span> and <span className="ph uicontrol">Recipients</span> are filled correctly.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/emails-settings/send-test-email.png")} alt="send test email" /><br /><br /></p> 

## Email template

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can define the sender, recipients (the list of emails to receive reports), email subject, and body template in this section.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execution-settings/KS-Project-Settings-Email-Template-Report-Format.png")} alt="Email Template and Report format" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports adding Test Suite and Test Suite Collection names in your email subject with the placeholders <code className="ph codeph">${'{'}suiteName{'}'}</code> and <code className="ph codeph">${'{'}suiteCollectionName{'}'}</code>, respectively.</p> 

## Report format

<div xmlns="http://www.w3.org/1999/xhtml" className="p">You can choose whether to include a test execution report as an email attachment. This includes selecting specific log files and configuring the report format (HTML, CSV, or PDF) to be attached.</div>

:::info notes
- Ensure the **Project > Settings > Plugins > Report > PDF** option is explicitly enabled. Without this, a PDF report will not be attached to the email.
- For an HTML report, when you enable the **Attach reference images using linked screenshots (not embedded) to reduce report file size** option in **Project > Settings > Plugins > Report**, only screenshots saved in the `Reports` folder are included in the report. If you want to save screenshots outside the `Reports` folder, do not select this option to avoid missing screenshots in your email report.
:::
## Body template

### Customize email template for test suite

To customize the email body template used for a Test Suite, do one of the following:

- Go to **Project > Settings > Email > Template**, then select **Test Suite** from the dropdown.

  <img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/Edit_test_suite_template_from_Test_suite_settings.png" alt="Customize Test Suite email report from Test Suite settings" width="600" />

- Or click **Edit Template for Test Suite Execution** from the **Email** Settings screen.

  <img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/Edit_test_suite_template_from_Email_settings.png" alt="Customize Test Suite email report from Email settings" width="600" />

The Test Suite email report template is displayed and is editable. Use the main navigation bar above the template, or click within the email body to reveal the quick edit menu.

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/KS_10.3.0_test_suite_report_template_config.png" alt="Edit Test Suite email report using quick menu" width="600" />

Use the following supported variables to customize the content of the Test Suite email template:

| Variable                  | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `${hostName}`             | Name of the host machine where the test was executed.         |
| `${os}`                   | Operating system used during test execution.                  |
| `${browser}`              | Browser name and version used (for Web tests).                |
| `${deviceId}`             | ID of the device used for test execution.                     |
| `${deviceName}`           | Name of the device used for test execution.                   |
| `${suiteName}`            | Name of the test suite executed.                              |
| `${executionProfile}`     | Execution profile used during the test run.                   |
| `${startTime}`            | Timestamp indicating when the test execution started.         |
| `${duration}`             | Total duration of the test execution.                         |
| `${totalPassed}`          | Number of test cases that passed.                             |
| `${totalFailed}`          | Number of test cases that failed.                             |
| `${totalError}`           | Number of test cases that encountered errors.                 |
| `${totalIncomplete}`      | Number of test cases that did not complete.                   |
| `${totalSkipped}`         | Number of test cases that were skipped.                       |
| `${executedBy}`           | Username or identity that initiated the test execution.       |
| `${projectName}`          | Name of the Katalon Studio project.                           |
| `${failedReason}`         | Describes the failure reason if the test suite did not pass.  |
| `${status}`               | Overall status of the test suite (e.g., Passed, Failed).      |
| `${test_suite_result_table}` | A detailed HTML-formatted table of test case results.          |

For projects created in Katalon Studio version 10.1.0 or later, you can include a test case result table in the email body.

To display a test case result table in your email report, manually insert one of the following variables into your Test Suite email template where you want the table to appear: 

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/KS_10.3.0_test_suite_report_template_table.png" alt="Add a test case result table" width="600" />

Refer to the table below to choose the appropriate variable for your reporting needs:

| Variable                         | Description                                                                 | When to Use                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `${test_case_result_table}`      | Displays a **detailed** test case result table, including test case name, status, duration, and error messages (if any). | Use for comprehensive reports intended for debugging, QA reviews, or audit documentation. |
| `${test_case_result_table_minimal}` | Introduced in Katalon Studio 10.3.0, displays a **simplified** result table with only the test case name and execution status. | Use for **lightweight** reports such as CI/CD notifications, stakeholder summaries, or quick overviews. |

:::note
The `${test_case_result_table}` variable is only supported in the Test Suite email template. If used in a Test Suite Collection template, the email will fail to send.
:::

Before saving your changes, click **Preview** to see how the Test Suite Execution report will appear in the email.

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/KS_10.3.0_test_suite_report_template_preview.png" alt="View a preview of the Test Suite Execution email report" width="600" />

Below is a sample report of a successful test suite execution as received via email:

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/Sample_passed_test_suite_execution_email_report.png" alt="Sample Passed Test Suite Execution email report" width="600" />

Below is a sample report of a failed test suite execution as received via email:

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/Sample_failed_test_suite_execution_email_report.png" alt="Sample Failed Test Suite Execution email report" width="600" />

Click **Apply** or **Apply and Close** when you have finished your customization.

### Customize email template for test suite collection

To customize the email body template used for a Test Suite Collection, do one of the following:

- Go to **Project > Settings > Email > Template**, then select **Test Suite Collection** from the dropdown.

  <img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/Edit_test_suite_collection_template_from_Test_suite_collection_settings.png" alt="Customize Test Suite Collection email report from Test Suite settings" width="600" />

- Or click **Edit Template for Test Suite Collection Execution** from the **Email** Settings screen.

  <img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/Edit_test_suite_template_from_Email_settings.png" alt="Customize Test Suite Collection email report from Email settings" width="600" />

Use the following variables to customize the content of the Test Suite Collection email template:

| Variable              | Description                                      |
|-----------------------|--------------------------------------------------|
| `hostName`            | Host's name                                      |
| `os`                  | Operating system                                 |
| `suiteCollectionName` | Name of the Test Suite Collection                |
| `startTime`           | When the Test Suite Collection started running   |
| `duration`            | Duration of the test execution                   |
| `totalPassed`         | Total passed test cases                          |
| `totalFailed`         | Total failed test cases                          |
| `totalError`          | Total error test cases                           |
| `totalIncomplete`     | Total incomplete test cases                      |
| `totalSkipped`        | Total skipped test cases                         |

Before saving your changes, click **Preview** to see how the Test Suite Collection Execution report will appear in the email.

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/KS_10.3.0_test_suite_collection_report_template_preview.png" alt="View a preview of the Test Suite Collection Execution email report" width="600" />

Below is a sample Test Suite Execution report as received via email:

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/generate-test-reports/KS_10.3.0_test_suite_report_collection_template_email_report_sample.png" alt="Sample Test Suite Collection Execution email report" width="600" />

Click **Apply** or **Apply and Close** when you have finished your customization. 

## Use global variables for emails

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">You can customize email settings   with global variables and override their default values via the   command-line.<div className="note note note_note"><span className="note__title">Note:</span> <p className="p"><strong className="ph b">Scope of application</strong>:</p>     <ul className="ul"><li className="li">When sending email reports on a Test Suite, the global         variables in the selected execution profile are applied.</li><li className="li">When sending email reports on a Test Suite Collection:          <ul className="ul"><li className="li">For a Test Suite Collection: only the global variables in the             <em className="ph i">default</em> profile are applied.</li><li className="li">For Test Suites contained in a Test Suite Collection: the             global variables in the selected execution profile of each Test             Suite are applied.</li></ul></li></ul></div><p className="p">The below section guides you on how to do that with a usage     example.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Define a global variable in your execution profile. See <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile#task-466">Create a profile</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Use the syntax <code className="ph codeph">${'{'}GlobalVariable.name{'}'}</code> to call the global variable in supported fields including <span className="ph uicontrol">Sender</span>,       <span className="ph uicontrol">Recipients</span>, <span className="ph uicontrol">Cc</span>, <span className="ph uicontrol">Bcc</span>,  <span className="ph uicontrol">Subject</span> and <span className="ph uicontrol">Body Template</span>.</span><p className="p">Note that global variables in emails only work when they are defined in the project profile. 
      If a global variable is updated at runtime (for example, in a Listener class), the updated value will not be applied to the email body.
    </p></li><li className="li step stepexpand"><span className="ph cmd">Send a test email so you can see the effect.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/3e9d1df0-7485-11ed-a602-0242cfbc79b5/ks-email.png")} /><p className="p">When running your Test Suite/Test Suite Collection in console         mode, you can also pass another value to override the default value         of that global variable with the         <code className="ph codeph">-g_&lt;variableName&gt;=&lt;variableValue&gt;</code> syntax.         For instance, <code className="ph codeph">-g_&lt;subject&gt;=&lt;Release 7.7&gt;</code>.</p></div></li></ol> 
