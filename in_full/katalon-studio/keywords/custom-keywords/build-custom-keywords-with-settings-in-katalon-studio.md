---
hide_title: true
title: Build custom keywords with Settings in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Build custom keywords with Settings in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can create a <strong className="ph b">Settings</strong> page under <strong className="ph b">Project Settings/Plugins</strong> for a custom-keyword plugin. This can be utilized to store project-scoped variables for users to customize.</p> 

## <a id="id_1" class="anchor_top_offset"/>Add settings page

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Custom Keyword Plugin declares the setting page UI in   <strong className="ph b">katalon-plugin.json</strong> with this sample:</p> 

```jsx
{
    "keywords": [],
    "configuration": {
        "settingId": "some id",
        "settingPage": {
            "name": "name",
            "components": [
                {
                    "key": "key1",
                    "type": "text",
                    "label": "My Label 1",
                    "defaultValue":"My default value 1"
                },
                {
                    "key": "key2",
                    "type": "secret",
                    "label": "My Label 2"
                }, ...
            ]
        }
    }
}
```

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <strong className="ph b">settingId</strong>: id the setting file that stores     user setting properties in the setting page. There is a file will     generated to store user settings at location:<pre className="pre codeblock"><code>&lt;Project dir&gt;/settings/external/&lt;settingId&gt;.properties</code></pre></li><li className="li">     <strong className="ph b">settingPage</strong> : contains the following     sub-properties      <ul className="ul"><li className="li">         <strong className="ph b">name</strong>: Name of the setting page</li><li className="li">         <strong className="ph b">components</strong>: list of UI components          <ul className="ul"><li className="li">             <strong className="ph b">key</strong>: key of the component</li><li className="li">             <strong className="ph b">label</strong>: label of the component</li><li className="li">             <strong className="ph b">type</strong>: type of the component             (‘text’ or ‘secret’)</li><li className="li">             <strong className="ph b">defaultValue</strong>: default value of the             component</li></ul>       </li></ul>   </li></ul> 

## <a id="id_2" class="anchor_top_offset"/>Prepare to test

1. Clone this project from our GitHub repository: `https://github.com/katalon-studio/katalon-studio-excel-custom-keywords-plugin`
2. Open the project in Katalon Studio at least once.
3. Modify katalon-plugin.json with this template:

```jsx
{
    "keywords": ["com.katalon.plugin.keyword.excel.ExcelReadKeywords", "com.katalon.plugin.keyword.excel.ExcelWriteKeywords"],
    "configuration": {
        "settingId": "com.katalon.plugin.keyword.excel-keywords",
        "settingPage": {
            "name": "Excel Keywords",
            "components": [
                {
                    "key": "username",
                    "type": "text",
                    "label": "Username"
                },
                {
                    "key": "password",
                    "type": "secret",
                    "label": "Password"
                }
            ]
        }
    }
}
```

4. Build excel keyword project:

`gradle katalonPluginPackage`
A jar file will be generated in **/build/libs** folder.

5. Copy and paste the generated jar file to **Plugins** folder of a Katalon Studio project (Project A).
6. Open **Project A** and navigate to **Project Settings/Plugins/Excel Keywords**.
7. Customize the settings as wish.

## <a id="id_3" class="anchor_top_offset"/>Retrieve the setting values

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The values can be retrieved in keyword script as the following   sample:</p> 

```jsx
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.setting.BundleSettingStore as BundleSettingStore

BundleSettingStore bundleSetting = new BundleSettingStore(RunConfiguration.getProjectDir(), '<setting_id>', true)
println(bundleSetting.getString('username', ''))
println(bundleSetting.getString('password', ''))
```