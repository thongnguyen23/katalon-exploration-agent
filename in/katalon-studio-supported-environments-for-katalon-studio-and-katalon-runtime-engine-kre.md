---
title: Supported environments for Katalon Studio and Katalon Runtime Engine (KRE)
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::info
We recommend using the latest version of Katalon Studio. Download the latest version from the Katalon website: [Katalon products.](https://www.katalon.com/download/)
:::

Katalon Studio (KS) provides free, basic tools suitable for the testing needs of individuals. For an advanced business solution, you can purchase Katalon Studio Enterprise (KSE) licenses. To compare features between Katalon Studio and KSE, you can refer to this document: <a href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-studio-vs-katalon-studio-enterprise-features">Katalon Studio vs Katalon Studio Enterprise Features</a>.

Katalon Runtime Engine (KRE) is the test execution add-on of Katalon Studio. KRE allows you to execute tests in a command-line interface (CLI).

## System requirements

  <Tabs>
  <TabItem value="ks-supported-env" label="Katalon Studio" default>
<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Platform</th>
      <th colspan="2">Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3"><b>Operating System</b></td>
      <td>Windows</td>
      <td colspan="2">Windows 7, 8, 10, 11, Server 2016, 2019, 2022</td>
    </tr>
    <tr>
      <td>macOS</td>
      <td colspan="2">OS X El Capitan 10.11 through macOS Ventura 13.2</td>
    </tr>
    <tr>
      <td>Linux</td>
      <td colspan="2">
        <ul>
          <li>OpenJDK 8 or 17. See <a href="/katalon-studio/get-started/install-katalon-studio#task-2817">Install Katalon Studio for Linux</a>.</li>
          <li>Latest Linux distros supporting Gnome, KDE, or Unity DE.</li>
          <li>Tested on Ubuntu 20.04, 22.04, 24.04 LTS.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2"><b>GUI Components</b></td>
      <td colspan="2">Required for all operating systems.</td>
    </tr>
    <tr>
      <td colspan="2"><b>CPU</b></td>
      <td colspan="2">Minimum: 2 GHz or faster 64-bit (x64) processor</td>
    </tr>
    <tr>
      <td colspan="2"><b>Memory</b></td>
      <td colspan="2">
        <ul>
          <li>Minimum: 4 GB available RAM (64-bit)</li>
          <li>
            Recommended: 8 GB available RAM (64-bit)
            <div>
              <b>Note:</b> Available RAM refers to unused memory not shared with other apps. See <a href="/katalon-platform/troubleshooting/troubleshooting-common-execution-issues/how-to-free-up-more-available-ram-for-katalon-studio">How to free up more available RAM for Katalon Studio</a>.
            </div>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2"><b>Hard Drive</b></td>
      <td colspan="2">At least 1 GB free. More may be required for projects and reports.</td>
    </tr>
  </tbody>
</table>
  </TabItem>

<TabItem value="kre-supported-env" label="Katalon Runtime Engine" default>
  <table>
    <thead>
      <tr>
        <th>Category</th>
        <th>Platform</th>
        <th colspan="2">Details</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><b>Operating System</b></td>
        <td>Windows</td>
        <td colspan="2">Windows 7, 8, 10, 11, Server 2016, 2019, 2022</td>
      </tr>
      <tr>
        <td>macOS</td>
        <td colspan="2">OS X El Capitan 10.11 through macOS Ventura 13.2</td>
      </tr>
      <tr>
        <td>Linux</td>
        <td colspan="2">
          <ul>
            <li>OpenJDK 8 or 17. See <a href="/katalon-studio/get-started/install-katalon-studio#task-2817">Install Katalon Runtime Engine for Linux</a>.</li>
            <li>Debian, Ubuntu, RHEL, Fedora, and CentOS-based distributions.</li>
            <li>Tested on Ubuntu 20.04, 22.04, 24.04 LTS.</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td colspan="2"><b>GUI Components</b></td>
        <td colspan="2">Katalon Runtime Engine (KRE) does not include GUI components. See <a href="/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10">Execution on KRE</a>.</td>
      </tr>
      <tr>
        <td colspan="2"><b>CPU</b></td>
        <td colspan="2">Minimum: 2 GHz or faster 64-bit (x64) processor</td>
      </tr>
      <tr>
        <td colspan="2"><b>Memory</b></td>
        <td colspan="2">
          <ul>
            <li>Minimum: 4 GB available RAM (64-bit)</li>
            <li>Concurrent executions (incl. Docker): sessions × 2GB (e.g., 3 sessions = 6GB)</li>
            <li>Recommended for AWS EC2: minimum 8 GB available RAM</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td colspan="2"><b>Hard Drive</b></td>
        <td colspan="2">At least 1 GB free. More may be needed for large projects and reports.</td>
      </tr>
    </tbody>
  </table>

  </TabItem>

</Tabs>



## Supported browsers

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe"><caption /><colgroup><col /><col /><col /><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1">Desktop Browsers</th><th className="entry anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2">Version on Windows</th><th className="entry anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3">Version on macOS</th><th className="entry anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4">Version on Linux</th><th className="entry anchor_top_offset" id="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5">Note</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Internet Explorer (IE)</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">9, 10, 11</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Required IE configurations: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/internet-explorer-configurations-for-katalon-studio">Internet Explorer Configurations</a>.</td></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Microsoft Edge</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">18</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 " /></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Microsoft Edge (Chromium)</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">80+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">80+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 " /></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Firefox</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">56+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">56+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">56+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 " /></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Google Chrome</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">58+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">58+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">58+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 " /></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Opera</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 " /></tr><tr className><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Safari</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">12+</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">N/A</td><td className="entry" headers="id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__1 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__2 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__3 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__4 id_2__8b94727e-5b26-4220-b73c-f08ddd1246fe__entry__5 ">Make sure <span className="ph uicontrol">Allow Remote Automation</span> is enabled in Safari browser: <a className="xref j-external-link" href="https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari#2957277" target="_blank">Enable Webdriver Support</a>.</td></tr></tbody></table> 

## Supported mobile operating systems (OS)

| Installation | Version on Windows | Version on macOS | Appium | Native App Support | [Hybrid App Support](https://appium.github.io/appium.io/docs/en/writing-running-appium/web/hybrid/)** | Mobile Browser Support | Xcode |
| ------------ | -------------  | ------------ | -------------  | ------------ | ------------- | ------------  | ------------ 
| Android | 6.x - 15.x | 6.x - 15.x | 1.12.1+, 2.11.1* | Yes | No | No | N/A |
| iOS | Content Cell | 9-15, 16, 17, 18* | 1.12.1+, 2.11.1* | Yes | No | No | v9.4.1-15* |

- (*) Requires Katalon Studio version 10.0.0 or later.
- (**) Refer to the following workarounds for hybrid apps:
  - [Capture elements in hybrid Android apps](/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/hybrid-mobile-apps-testing/native-render-only-webview-render-capture-elements-in-hybrid-android-apps-in-katalon-studio)
  - [Flutter-based application testing with custom SetText keyword](/katalon-studio/keywords/custom-keywords/flutter-based-application-testing-with-custom-settext-keyword-in-katalon-studio)

### Supported Appium drivers

The following are related to Appium mobile operating system (OS) only:

| Driver | Version |
| ------------ | ------------- |
| [Appium Flutter](/katalon-studio/keywords/custom-keywords/flutter-based-application-testing-with-custom-settext-keyword-in-katalon-studio#set-up-appium-flutter-driver) | 2.8.0 |
| [Appium XCUITest Driver for iOS](/katalon-studio/manage-projects/set-up-projects/mobile-testing/execute-mobile-tests-with-appium-2.x#install-appium-2x-and-execute-mobile-tests) | 7.21.1 |
| [Appium UiAutomator2 Driver for Android](/katalon-studio/manage-projects/set-up-projects/mobile-testing/execute-mobile-tests-with-appium-2.x#install-appium-2x-and-execute-mobile-tests) | 3.7.0 - 4.0.0* |

*For information on the differences when using Appium UIAutomator2 version 4 with Katalon Studio, see: [v4.0.0 release notes](https://github.com/appium/appium-uiautomator2-driver/releases/tag/v4.0.0). 

## Supported Windows platforms

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> fully supports automation testing for desktop   apps written in the following platforms:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Universal Windows Platform (UWP)</li><li className="li">Windows Forms (WinForms)</li><li className="li">Windows Presentation Foundation (WPF)</li><li className="li">Classic Windows (Win32)</li></ul> 
