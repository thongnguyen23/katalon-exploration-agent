---
title: Configure KRE version for TestCloud execution on TestOps
---

TestCloud uses **Katalon Runtime Engine (KRE)** to execute test scripts created in Katalon Studio. When scheduling a test run on TestOps, you can specify which KRE version to use to ensure compatibility with your scripts and browser requirements.

In the **Schedule Test Run** dialog in TestOps, click **Advanced settings** at the lower left corner to configure the Katalon Runtime Engine (KRE) version. When you set the KRE version to **Latest**, the scheduler will select the most recent KRE version that is compatible with TestCloud to execute.

<img src="https://tw-cdn.katalon.com/katalon-testcloud/tc-advance-settings-kre-versions.png" alt="Select latest KRE version" width="700" />

For TestCloud environments:
- **Latest**: newest version compatible with TestCloud (for example, Katalon Studio v11 or v12 in the future).
- **Latest 9.x**: newest version within the 9.x series (currently 9.7.5).
- **Latest 10.x**: newest version within the 10.x series (e.g., 10.2.3).
- New Default: Latest 10.x is now the default for all new schedules.
- Existing scheduled test runs previously set to the generic `Latest` tag will be automatically migrated to **Latest 9.x** (9.7.5).

Each KRE version supports a different set of browser versions. Use the table below to compare the latest KRE options and see the corresponding supported browsers for each version. 

<table>
<tr>
    <th width="150px">Selected KRE version</th>
    <th width="150px">Compatible KRE version with TestCloud</th>
    <th width="150px">Browser version</th>
</tr>
<tr>
    <td>Latest</td>
    <td>10.3.0</td>
    <td rowspan="13"><code>chrome:>=119; firefox:>=119; chrome_headless:>=119; firefox_headless:>=119; edge_chromium:>=119; safari:>=16</code></td>
</tr>
<tr>
    <td>Latest 10.x</td>
    <td>10.3.0</td>
</tr>
<tr>
    <td>Latest 9.x</td>
    <td>9.7.5</td>
</tr>
<tr>
    <td>10.3.0</td>
    <td>10.3.0</td>
</tr>
<tr>
    <td>10.2.4</td>
    <td>10.2.4</td>
</tr>
<tr>
    <td>10.2.3</td>
    <td>10.2.3</td>
</tr>
<tr>
    <td>10.2.2</td>
    <td>10.2.2</td>
</tr>
<tr>
    <td>10.2.1</td>
    <td>10.2.1</td>
</tr>
<tr>
    <td>10.2.0</td>
    <td>10.2.0</td>
</tr>
<tr>
    <td>10.1.2-rc1</td>
    <td>10.1.2-rc1</td>
</tr>
<tr>
    <td>10.1.1</td>
    <td>10.1.1</td>
</tr>
<tr>
    <td>10.1.0</td>
    <td>10.1.0</td>
</tr>
<tr>
    <td>10.0.1</td>
    <td>10.0.1</td>
</tr>
<tr>
    <td>10.0.0</td>
    <td>10.0.0</td>
</tr>
<tr>
    <td>9.7.5 - 9.0.0</td>
    <td>9.7.5 - 9.0.0</td>
</tr>
<tr>
    <td>8.6.9 - 8.6.8</td>
    <td>8.6.9 - 8.6.8</td>
    <td><code>chrome:88-118; firefox:86-118; chrome_headless:88-118; firefox_headless:86-118; edge_chromium:89-118; Internet Explorer 11; safari:10-15</code></td>
</tr>
</table>


