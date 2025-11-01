---
hide_title: true
title: Katalon Studio GitHub Action
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalon Studio GitHub Action

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Use Actions on GitHub to automate your development   workflow. The <span className="ph">Katalon Studio</span> GitHub Action  available on   the          GitHub marketplace allows you to automate your <span className="ph">Katalon Studio</span> project   execution. Access <span className="ph">Katalon Studio</span> GitHub Action  from GitHub marketplace: <a className="xref j-external-link" href="https://github.com/marketplace/actions/katalon-studio" target="_blank">Katalon Studio GitHub Action</a>.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">You need an active <span className="ph">Katalon Runtime Engine (KRE)</span> license.</li><li className="li"><p className="p">You have already set up your Katalon API key using a  GitHub encrypted secret named <code className="ph codeph">API_KEY</code>. To learn how to use Katalon API keys, see <a className="xref" href="/katalon-platform/administer/settings/katalon-api-key-in-katalon-testops">Katalon         API Keys</a>. To learn more about GitHub encrypted secrets, see GitHub document <a className="xref j-external-link" href="https://docs.github.com/en/actions/security-guides/encrypted-secrets" target="_blank">Encrypted secrets</a>.</p></li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Variables

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To run the <span className="ph">Katalon Studio</span> GitHub Action,  define the variables in the action metadata file.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Below is an example of how the action metadata file looks like. You do not need to create  action metadata files when using <span className="ph">Katalon Studio</span> GitHub Action:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>name: 'Katalon-Studio'{"\n"}description: 'Execute Katalon Studio projects'{"\n"}inputs:{"\n"}{"      "}version:{"\n"}{"            "}description: 'Which version of Katalon Studio to run'{"\n"}{"            "}required: true{"\n"}{"            "}default: ''{"\n"}{"\n"}{"      "}projectPath:{"\n"}{"            "}description: 'Where the Katalon Studio project is checked out'{"\n"}{"            "}required: true{"\n"}{"            "}default: ''{"\n"}{"\n"}{"      "}args:{"\n"}{"            "}description: 'What arguments to run Katalon Studio project'{"\n"}{"            "}required: true{"\n"}{"            "}default: ''{"\n"}{"\n"}runs:{"\n"}{"      "}using: 'node16'{"\n"}{"      "}main: 'index.js'{"\n"}</code></pre> 

## <a id="id_2" class="anchor_top_offset"/>Usage Example

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>name: CI{"\n"}on:{"\n"}{"  "}push:{"\n"}{"    "}branches: [ master ]{"\n"}{"  "}pull_request:{"\n"}{"    "}branches: [ master ]{"\n"}{"\n"}jobs:{"\n"}{"  "}build:{"\n"}{"    "}runs-on: windows-latest{"\n"}{"    "}steps:{"\n"}{"    "}- name: Checkout{"\n"}{"      "}uses: actions/checkout@v2.1{"\n"}{"    "}- name: Katalon Studio Github Action{"\n"}{"      "}uses: katalon-studio/katalon-studio-github-action@v2{"\n"}{"      "}with:{"\n"}{"          "}version: '7.5.5'{"\n"}{"          "}projectPath: '${"{"}{"{"} github.workspace {"}"}{"}"}'{"\n"}{"          "}args: '-noSplash -retry=0 -testSuiteCollectionPath="Test Suites/Simple Test Suite Collection" -apiKey= ${"{"}{"{"} secrets.API_KEY {"}"}{"}"} --config -webui.autoUpdateDrivers=true'{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find the CI samples for macOS and Windows on our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/ci-samples/tree/master/.github/workflows" target="_blank">ci-samples/.github/workflows/</a>.</p> 
