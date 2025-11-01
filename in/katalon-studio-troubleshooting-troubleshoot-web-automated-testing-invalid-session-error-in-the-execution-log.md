---
hide_title: true
title: Invalid Session error in the execution log
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-8887" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Invalid Session error in the execution log

When executing tests with Chrome browser, there is `Invalid Session` error message in the execution log.

1. From your opened project in Katalon Studio, navigate to **Projects > Settings > Desired Capabilities > WebUIChrome**.
    <img className="image" src={useBaseUrl("/1687e7c0-a556-11ee-b8c3-0242c7a41fd4/KS-_Project_Settings_-_Desired_Cap_for_Chromes.png")} alt="Chrome desired capabilities" />

2. Select **Add** from the command toolbar, then input the following values:

    <div style={{ width: '90%' }}>
    <table style={{ width: '100%', tableLayout: 'fixed' }}>
    <thead>
    <tr>
    <th style={{ width: '20%' }}><strong>Table 1</strong></th>
    <th></th>
    <th></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><code>args</code></td>
    <td><code>List</code></td>
    <td>
    Click <strong>More [...]</strong>. In the pop-up <strong>List Property Builder</strong> dialog, click <strong>Add</strong>, then input values from Table 2 below.
    </td>
    </tr>
    </tbody>
    </table>
    </div>

    | **Table 2** |  |
    | --- | --- |
    | Type | Value |
    | `String` | `--no-sandbox` |
    | `String` | `--disable-dev-shm-usage` | 
    | `String` | `--disable-gpu` | 

    <img className="image" src={useBaseUrl("/13e30680-a556-11ee-b8c3-0242c7a41fd4/KS_-_desired_capabilities_to_avoid_Invalid_Sessions.png")} alt="desired capabilities to avoid Invalid Sessions" />