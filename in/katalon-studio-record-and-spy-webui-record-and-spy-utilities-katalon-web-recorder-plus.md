---
hide_title: true
title: Katalon Web Recorder Plus
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Katalon Web Recorder Plus

:::note
- You can use Web Recorder Plus with **Web Recorder** and **Object Spy** in Chrome and Edge Chromium. Both **Active Browsers** and **New Browsers** options are supported.
:::

## What is Katalon Web Recorder Plus?

Katalon Web Recorder Plus is an enhancement of Web Recorder that improves test automation capabilities with advanced locators, support for complex web technologies, and a streamlined recording experience.

In this document, you will learn how Web Recorder Plus differs from the standard Web Recorder, along with a tutorial for using it. We also discuss its key changes, behaviors, and current limitations compared to the standard recorder.

## Feature comparison: Web Recorder vs. Web Recorder Plus

The Web Recorder Plus extends the capabilities of the standard recorder by supporting more complex web technologies and offering improved functionality for web test automation. Here's a breakdown of the key differences:

| Feature | Web Recorder | Web Recorder Plus |
| ------------ | ------------- | ------------- |
| Enterprise compatibility | May face challenges with the unpacked extension due to strict security policies. | Provides an official Katalon Studio Recording Engine extension that can be whitelisted and installed, eventually replacing Katalon Compact Utility. |
| Application technologies | General web applications. | Enhanced support for web apps built on advanced web technologies. <ul><li>For web apps like Flutter apps, apps with HTML5 Canvas elements and closed Shadow DOM, see [Enable web smart inspectors](/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio#webui-settings).</li></ul>|
| Locator strategy | Basic XPath and CSS. | Generates unique, stable locators using advanced CSS operators, and excludes text-based locators for improved stability. |
| Text attribute behavior | Uses the element text as a default for test object names. | Adds the` @text` attribute to capture the original element text. Test object names are generated using a new algorithm. |
| Actions supported | Basic interactions. | Auto-detect hover actions, support for mouse down events, and capturing actions like mouse over. |
| Event handling | Limited event hooking. | 	Enhanced event hooking with support for pointer event phases to improve accuracy. |
| User interface enhancements | Default element highlighting. | Updated Katalon green branding for element highlights; optimized UI for shadow DOM and iframe isolation. |
| Performance optimization | Standard performance. | Locator caching for faster interaction and improved stability when interacting with complex elements. |

## Enable Web Recorder Plus in Katalon Studio

1. From the main menu, go to **Katalon Studio > Preferences > Katalon > Beta Features** and check the box for Katalon Web Recorder Plus. 

2. Select the option to launch Katalon Web Recorder Plus in either **New browser** (which is the default option) or **Active browser** mode:

    ![Configure Katalon Web Recorder Plus settings](https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/Configure_Katalon_Web_Recorder_Plus_settings.png)

    - **New browser**: Starts recording in a new browser.
    - **Active browser**: Uses the current browser to start recording.

    If you select the **Active browser** option, install the extension:
    
    - For Chrome: [Install from Chrome Web Store](https://chromewebstore.google.com/detail/katalon-studio-recording/ipkccgcigdgmeofoaocdkabpbckdbdci).
    - For Edge: [Install from Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/katalon-studio-recording-/gjjbphpfndcgghhlfcjnfplblfolcjeb).

    :::note
    After installing the extension for the **Active browser** option, you may need to reload the browser to activate it.
    :::

3. Click **Apply and Close** to save your settings.

4. Once enabled, you can begin recording test cases or capture objects by selecting **Record Web** or **Spy Web** on the main toolbar. For more details on how to record a test case or capture objects, see: [Record a new test](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio) case or [Capture objects](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/spy-web-utility-in-katalon-studio).

Web Recorder Plus is now enabled.

<img width={850} src={useBaseUrl("/d591aa8d-9097-4366-9348-4ab25bf51284/web-recorder-plus-start.jpg")} />

:::tip
- In the recording window, to access the hotkey menu and see the full list of shortcuts:
    - macOS: use `Shift` + `Option` + `
    - Windows: use `Alt` + `
:::
	
### Install the Katalon Studio Recording Engine extension 

This section is specifically for recording with an **Active browser** using **Recorder Plus**. 

When recording with an Active browser, you must install the **Katalon Studio Recording Engine** extension to enable proper recording functionality.

If you select the Active browser option, install the extension: 
- For Chrome: [Install from Chrome Web Store](https://chromewebstore.google.com/detail/katalon-studio-recording/ipkccgcigdgmeofoaocdkabpbckdbdci).

	:::warning Extension compatibility versions
	Since the Chrome Extension Marketplace only provides the latest version, you may encounter unexpected issues if you are not using a compatible version of the extension. In such cases, it is recommended to use New Browser mode for recording instead.
	:::

- For Edge: [Install from Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/katalon-studio-recording-/gjjbphpfndcgghhlfcjnfplblfolcjeb).

Refer to the following table for browser extension version compatibility with Katalon Studio Enterprise (KSE):

| KSE version | Katalon Studio Recording Engine extension version |
|----------|----------|
| Before 10.2.4    | 1.0.8   | 
| 10.3.0 and later    | 1.0.9   | 

Check the version of your Katalon Studio Recording Engine extension. 

- For Chrome: Go to [chrome://extensions/](chrome://extensions/) and use search to find your Katalon Studio Recording Engine extension.
	- You can quickly view the version of your extension on the tile itself.

	<img src= "https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/KSE_view_extension_version_quickview.png" alt="View Katalon Studio Recording Engine extension quick tile" width="400" />

	- Or you can click **Details** and navigate to the **Version** field.

	<img src= "https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/KSE_view_extension_version_details.png" alt="View Katalon Studio Recording Engine extension details" width="600" />
- For Edge: Same as with Chrome, go to the [Extensions page](edge://extensions/) and use search to find your Katalon Studio Recording Engine extension on the list. 
	- You can quickly view the version of your extension on the tile itself, or you can click **Details** and navigate to the **Version** field.

## Recording actions in Web Recorder Plus

With Web Recorder Plus, you can now handle:

- Mouse over events: Allows capturing hover actions on elements.
- Locator value copying:
    - macOS: Use `Option` + `C` (or `Shift` + `Option` + `C`)
    - Windows: Use `Alt` + `C`

    When hovering over an element, this shortcut copies its locator (for example, #btn-make-appointment) to your clipboard, making it easy to reuse in your test scripts.

    <img width={700} src={useBaseUrl("/d0328d88-2214-43ba-adac-4fe1ca22d0be/web-recorder-plus-hotkey.png")} />

:::tip
- In the recording window, to access the hotkey menu and see the full list of shortcuts:
    - macOS: Use `Shift` + `Option` + `
    - Windows: Use `Alt` + `
:::

## Execute test cases recorded using Web Recorder Plus

Test cases recorded using Web Recorder Plus can be executed normally without requiring additional configuration in most scenarios.

However, if your Web Application Under Test (AUT) includes special cases, we recommend enabling Smart Web Inspectors to ensure test stability. You can do this via **Project > Settings > Execution > WebUI > Enable Smart Web Inspectors**, and specify the web AUT: 

![Enable web smart inspectors](https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/KS_Web_Recorder_Plus_enable_web_smart_inspectors.png)

This feature is particularly helpful for the following scenarios:

- **Flutter web app**: Built with the Flutter framework, these apps use unique DOM structures that often require specialized handling.

  :::note
  Only Web Recorder Plus supports recording interactions on Flutter-based web applications. If you're working with such apps, you must use Recorder Plus for reliable element detection and script creation.
  :::

- **Canvas text extraction**: Content rendered inside HTML5 Canvas elements, which traditional locators cannot detect.

- **Closed Shadow DOM**: Components encapsulated in closed Shadow DOM, which limits access to internal elements using standard methods.

- **Obstructed UI elements**: Certain elements—such as calendars, dropdowns, or select boxes—may be partially or fully hidden behind transparent or invisible layers, making them difficult to capture or interact with during recording or execution.

For more information about WebUI execution settings, see [WebUI settings](/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio#webui-settings).

If you are testing a Flutter web app using Katalon Studio version earlier than 10.2.0, use a custom keyword to inject JavaScript that enables element interaction by exposing Flutter semantic nodes.. For implementation guidance, see [Introduction to custom keywords](/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio).

Below is the custom keyword script that enables interaction with Flutter-based web applications:
```jsx
package mypackage

import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

public class FlutterBasedKeywords {

	static String script = """
		(function() {
			"use strict";
			function l(t) {
				new MutationObserver(e => {
					e.some(r => !(r.type !== "childList" || r.addedNodes.length === 0)) && t()
				}).observe(document, { childList: !0, subtree: !0 })
			}
			function s(t = document) {
				if (!t.querySelector("flutter-view")) return;
				t.querySelectorAll("flt-semantics-placeholder").forEach(i => { i.click() });
				const e = t.querySelector("flt-glass-pane");
				if (!e || e.activated) return;
				e.activated = !0;
				const n = document.createElement("style");
				n.innerHTML = \`
					flt-semantics {
						pointer-events: all !important;
					}
					flt-semantics-container {
						left: 0;
						top: 0;
					}
				\`;
				n.id = "flutter-override-styles";
				document.head.appendChild(n);
				const r = e.shadowRoot?.querySelector("flt-semantics-placeholder");
				r && r.click();
			}
			function o() {
				navigator.webdriver && (s(), l(() => { s() }));
			}
			o();
		})();
	""";

	@Keyword
	public static void activateFlutterBasedWebApp() {
		WebUI.executeJavaScript(script, null)
	}
}
```

Here is an example of how to use the custom keyword in your test script:

```jsx
WebUI.openBrowser('https://flutter.github.io/samples/web/material_3_demo/')

CustomKeywords.'mypackage.FlutterBasedKeywords.activateFlutterBasedWebApp'()
//or FlutterBasedKeywords.activateFlutterBasedWebApp()

WebUI.click(findTestObject('Object Repository/Page_Material 3/flt-semantics_Elevated'))
```

:::note
Update the `mypackage` name to match your project structure.
:::

## Configure locator strategy

You can configure how locators are generated for new test objects during recording or spying sessions using Web Recorder Plus.

See the following documentation for more information: [Set the default selection method](/katalon-studio/test-objects/web-test-objects/selection-methods-for-web-objects#set-the-default-selection-method).

<img src= "https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/Selection_method_for_Web_test_objects.png" alt="Selection methods for Web objects" width="600" />

## Configure exclusion patterns from locator generation

To define specific patterns to exclude from locator generation:

1. Go to **Project > Settings > Test Design > WebUI**.

2. Under the **Recorder Plus** section, use the input field to specify patterns (e.g., `pa-*`) for class or attribute names you want Recorder Plus to ignore. This helps prevent unstable or dynamic identifiers (like auto-generated class names) from being used as part of your locators.

	<img src= "https://tw-cdn.katalon.com/katalon-studio/record-and-spy/webui-record-and-spy-utilities/Web_Recorder_Plus_exclude_patterns_locator.png" alt="Configure exclusion patterns from locator generation" width="400" />

	:::note
	This exclusion rule applies only to element class and attribute names.
	:::

3. Click **Apply** or **Apply and close** to save your changes.

## Changes and known limitations in Web Recorder Plus

### Locator changes

- **No text-based locator** - Web Recorder Plus does not use the text content of elements to create locators, as this approach can be unreliable across different versions or content updates.

- **CSS-based strategy** - Locators are generated based on CSS selectors. XPath conversion is available but limited. XPath locators may be less stable than CSS locators, especially for dynamic content. You should set CSS as the default locator strategy to ensure better stability and reliability.

- **Certain locator changes** - You can compare how the locator strategies differ between Web Recorder and Web Recorder Plus in the table below.

The following table shows objects captured by each application on our demo website `https://katalon-demo-cura.herokuapp.com/`.

| First Header | Second Header |
| ------------ | ------------- |
| <ul><li>Object name: `a_Make Appointment`</li><li>XPath: `//a[@id = 'btn-make-appointment']`</li><li>CSS: `#btn-make-appointment`</li></ul> | <ul><li>Object name: `a_btn-make-appointment`</li><li>XPath: `//*[@id = 'btn-make-appointment']`</li><li>CSS: `#btn-make-appointment`</li></ul> |
| <ul><li>Object name: `label_Medicaid`</li><li>XPath: `//section[@id = 'appointment' ]/div/div/form/div[3]/div/label[2]`</li><li>CSS: empty</li></ul> | <ul><li>Object name: `input_programs`</li><li>XPath: `//*[@id = 'radio_program_medicaid']`</li><li>CSS: `#radio_program_medicaid`</li></ul>|
| <ul><li>Object name: `label_Apply for hospital readmission`</li><li>XPath: `//section[@id = 'appointment' ]/div/div/form/div[2]`/div/label</li><li>CSS: `label.checkbox-inline`</li></ul> | <ul><li>Object name: `label_Apply for hospital readmission`</li><li>XPath: `//*[@class and contains(concat(' ', normalize-space(@class), ' '), ' checkbox-inline ')]`</li><li>CSS: `.checkbox-inline`</li></ul> |
| <ul><li>Object name: `input_Visit Date (Required)_visit_date`</li><li>XPath: `//input[@id = 'txt_visit_date']`</li><li>CSS: `#txt_visit_date`</li></ul> | <ul><li>Object name: `input_dd_mm_yyyy`</li><li>XPath: `//*[@id = 'txt_visit_date']`</li><li>CSS: `#txt_visit_date`</li></ul>|
| <ul><li>Object name: `select_Tokyo CURA Healthcare Center _5b4107`</li><li>XPath: `//select[@id = 'combo_facility']`</li><li>CSS: `#combo_facility`</li></ul> | <ul><li>Object name: `select_Facility`</li><li>XPath: `//*[@id = 'combo_facility']`</li><li>CSS: `#combo_facility`</li></ul> |

### Settings in Test Design > WebUI

Katalon Studio offers configuration options for element locators under **Project > Settings > Test Design > WebUI**, including default locator strategies (XPath, CSS, Attributes) and pattern exclusions for element classes or attributes.

However, these settings **may not fully apply** to Web Recorder Plus recordings. While some locator preferences are honored, others—like excluded class patterns—may be bypassed depending on how elements are captured. We recommend reviewing and adjusting generated locators after recording to ensure accuracy and maintainability.

### New tab not supported

Currently, recording interactions across multiple tabs is not supported.

### Performance issues with Smart Locator

On certain websites, using Web Recorder Plus with the Smart Locator feature enabled may cause performance issues. To avoid this, turn off Smart Locator after starting Web Recorder Plus.

Follow these steps to turn off Smart Locator:

1. Locate the **Katalon Studio Recording Engine** extension icon in the browser instance's toolbar.

    <img className="image" width={400} src={useBaseUrl("/7c36566e-efc3-4c80-8bc1-b6d4cd105d19/recorderplus-turn-off-smart-locator-1.png")} />

2. Click the icon, and uncheck the **Enable Smart Locator Capture** option.

    <img className="image" width={400} src={useBaseUrl("/b14a1869-b0d6-40a4-bc6c-76a242bed808/recorderplus-turn-off-smart-locator-2.png")} />

