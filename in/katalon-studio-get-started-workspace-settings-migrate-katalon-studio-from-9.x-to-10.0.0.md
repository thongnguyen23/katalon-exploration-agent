---
hide_title: true
title: Migrate Katalon Studio from 9.x to 10.0.0
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Migrate Katalon Studio from 9.x to 10.0.0

In version 10.0.0, Katalon Studio adopts Selenium 4 and the W3C WebDriver standard. This upgrade introduces significant changes in how browsers are configured and interacted with in test scripts, particularly the shift from using `DesiredCapabilities` to `Options`.

## Katalon Studio 9.x vs. 10.x general comparison

| First Header | 9.x | 10.x |
| ------------ | ------------- | ------------- |
| Selenium | 3.141.59 | 4.22 |
| Appium | 2.2.0 | 2.11.1 |
| Smart Locator | Requires extension | Natively supported without execution extension. |
| Smart Wait | Requires extension | Natively supported without execution extension. |
| BiDi (bidirectional communication) | Not supported | <ul><li>Default support for execution using Smart Locator and Smart Wait.</li><li>Disable BiDi by setting `"webSocketUrl": false` in the desired capabilities.</li></ul> |

:::note
Katalon Studio's BiDi support is currently limited to Smart Locator and Smart Wait.
:::

### Smart Locator and Smart Wait enhancement with BiDi

In Katalon Studio 10.x, Smart Locator and Smart Wait are now natively supported without requiring an extension, but these features are available only when using browsers that support BiDi.

Supported browsers when BiDi is enabled:
- Chrome
- Edge
- Firefox
- Headless browsers

:::note Known limitation
Katalon Studio 10.x does not support BiDi on remote web driver, TestCloud (desktop and mobile), and Safari.
:::

## Upgrade with actions required

When upgrading from 9.x to 10.x, you need to perform some additional steps to successfully migrate your existing test cases and configurations.

### Transition from `DesiredCapabilities` to `Options` 

In Selenium 4, DesiredCapabilities is deprecated in favor of Options classes for configuring browsers. This change aligns with the W3C WebDriver protocol that Selenium 4 adheres to.

**Action required**:

- Replace all uses of `DesiredCapabilities` with the corresponding `Options` classes (for example, `ChromeOptions`, `FirefoxOptions`). 

    - For example:

    Before (Katalon Studio 9.x):

    ```jsx
    DesiredCapabilities caps = DesiredCapabilities.firefox();
    caps.setCapability("platform", "Windows 10");
    caps.setCapability("version", "92");
    caps.setCapability("build", myTestBuild);
    caps.setCapability("name", myTestName);
    WebDriver driver = new RemoteWebDriver(new URL(cloudUrl), caps);
    ```

    After (Katalon Studio 10.x):

    ```jsx
    FirefoxOptions browserOptions = new FirefoxOptions();
    browserOptions.setPlatformName("Windows 10");
    browserOptions.setBrowserVersion("92");
    Map<String, Object> cloudOptions = new HashMap<>();
    cloudOptions.put("build",myTestBuild);
    cloudOptions.put("name", myTestName);
    browserOptions.setCapability("cloud:options", cloudOptions);
    WebDriver driver = new RemoteWebDriver(new URL(cloudUrl), browserOptions);
    ```

    - To easily update your test scripts, use the Advanced Search feature to find and replace `DesiredCapabilities`. You can access it via **Action > Advanced Search > File Search**, and use the **Replace…** option. See [Advanced Search](/katalon-studio/manage-test-artifacts/search-test-cases-in-katalon-studio#task-741).

Also update the desired capabilities in **Project > Settings > Desired Capabilities**:

<img src= "https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-studio/docs/project-settings-new-ui/KS-DC-FIREFOX-mozilla-options.png" alt="Update desired capabilities" width="600" />

### W3C standard capability validation and backward compatibility

With the adoption of Selenium 4, Katalon Studio follows the W3C WebDriver standard, which is now the default protocol for configuring browser capabilities. If your project includes capabilities that do not comply with this standard, the session may fail to start.

Here is the list of W3C WebDriver standard capabilities:
- `browserName`
- `browserVersion` (replaces `version`)
- `platformName` (replaces `platform`)
- `acceptInsecureCerts`
- `pageLoadStrategy`
- `proxy`
- `timeouts`
- `unhandledPromptBehavior`

For an up-to-date list of standard capabilities, you can refer to the WebDriver documentation: [Capabilities](https://www.w3.org/TR/webdriver1/#capabilities).

**Action required**:
Any capabilities not listed above must include a vendor prefix (for example, appium: or cloud:). For mobile testing with Appium, Katalon Studio automatically adds the appium: prefix to the required capabilities at runtime. However, Katalon Studio does not modify user-configured capabilities in project settings.

- For example: 

    - User-configured capabilities:

    ```jsx
    {
        "app": "c0425be7-5f0e-426b-8ffe-c0bc9f21c89f",
        "deviceName": "Google Pixel 7 Pro",
        "vendor:option": {
            "deviceVersion": "15",
            "deviceId": "google_pixel_7_pro",
            "usingTunnel": false
        },
        "platformName": "ANDROID",
        "platformVersion": "android-15",
        "isRealMobile": true
    }
    ```
    - Formatted user-configured capabilities following W3C:
    ```jsx
    {
        "appium:app": "c0425be7-5f0e-426b-8ffe-c0bc9f21c89f",
        "appium:deviceName": "Google Pixel 7 Pro",
        "vendor:option": {
            "deviceVersion": "15",
            "deviceId": "google_pixel_7_pro",
            "usingTunnel": false
        },
        "platformName": "ANDROID",
        "appium:platformVersion": "android-15",
        "appium:isRealMobile": true
    }
   ``` 

- For non-mobile (Selenium) tests, if any user-configured capabilities do not follow W3C standards, the test will fail, and Katalon Studio will display an error message.

 ### Removal of `SmartWaitWebDriver`

In Katalon Studio 10.x, the `SmartWaitWebDriver` class has been removed. This class was used to automatically manage waiting for elements before interacting with them. However, with Selenium 4, these capabilities are now handled natively through WebDriver decorators.

**Action required**:

- Remove any references to `SmartWaitWebDriver` from your test scripts.
- Use standard WebDriver methods, which now include enhanced waiting functions.

For example:

- Before (Katalon Studio 9.x):

    ```jsx
    import com.kms.katalon.core.webui.driver.DriverFactory
    import com.kms.katalon.core.webui.driver.SmartWaitWebDriver
    import org.openqa.selenium.WebDriver

    // Step 1: Initialize the WebDriver using DriverFactory
    WebDriver driver = DriverFactory.getWebDriver()

    // Step 2: Wrap the WebDriver with SmartWaitWebDriver to enable Smart Wait
    SmartWaitWebDriver smartWaitDriver = new SmartWaitWebDriver(driver)

    // Step 3: Navigate to a web page
    smartWaitDriver.get("https://example.com")

    // Step 4: Perform interactions (SmartWait ensures elements are ready before interacting)
    smartWaitDriver.findElementById("someElementId").click()

    // Step 5: Close the browser after the test
    DriverFactory.closeWebDriver()
    ```
- After (Katalon Studio 10.x):

    ```jsx
    import com.kms.katalon.core.webui.driver.DriverFactory
    import org.openqa.selenium.WebDriver

    // Step 1: Initialize the WebDriver using DriverFactory
    WebDriver driver = DriverFactory.getWebDriver()

    // Step 2: Navigate to a web page
    driver.get("https://example.com")

    // Step 3: Perform interactions
    driver.findElementById("someElementId").click()

    // Step 4: Close the browser after the test
    DriverFactory.closeWebDriver()
    ```

### Removal of `AbstractEventListener`, `EventFiringWebDriver`, and `WebDriverEventListener` 

The `AbstractEventListener`, `EventFiringWebDriver`, and `WebDriverEventListener` classes will no longer function in Selenium 4. If you are using these classes, update your test cases to remove or replace them with the new Selenium 4 features, which include improved support for event handling via decorators.

To migrate test scripts that use these classes, refer to Selenium documentation: [Removal of AbstractEventListener + EventFiringWebDriver + WebDriverEventListener](https://www.selenium.dev/blog/2023/java-removal-of-deprecated-events-classes/).

### Refactoring of `DriverFactory` 

If you're using Katalon Studio version 10.0.0 and previously relied on the method DriverFactory.getChromeDriverPath(), you might encounter the following error:

```
groovy.lang.MissingMethodException: No signature of method: static com.kms.katalon.core.webui.driver.DriverFactory.getChromeDriverPath() is applicable for argument types: () values: []{"\n"}
```
This issue occurs because, starting from version 10.0.0, the DriverFactory class has been refactored. The getChromeDriverPath() method has been moved to the ChromeDriverUtil class.

**Action required**:
1. Replace the previous import:

    ```jsx
    import com.kms.katalon.core.webui.driver.DriverFactory
    ```
2. Use the following import and updated method:
    ```jsx
    import com.kms.katalon.core.webui.driver.chrome
    String chromeDriverPath = ChromeDriverUtil.getChromeDriverPath()
    ```

### Remote browser testing support

Selenium 4 is fully supported on popular cloud-based remote testing services. If you're using a remote testing service such as LambdaTest, Sauce Labs, or BrowserStack, ensure your capabilities comply with the W3C WebDriver standard.

**Action required**:
- For cloud services that only support Selenium 4, convert your existing `DesiredCapabilities` to the new W3C-compliant format.
- Follow the specific instructions provided by your cloud service to ensure compatibility.

This table outlines the required configurations and compatibility for each remote testing service when using Selenium 4:

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="concept-1476__53136d01-4538-4ca4-ad87-3dee80496a47"><caption /><colgroup><col style={{width: '15.384615384615385%'}} /><col style={{width: '28.205128205128204%'}} /><col style={{width: '28.205128205128204%'}} /><col style={{width: '28.205128205128204%'}} /></colgroup><tbody className="tbody"><tr className><td className="entry"><strong className="ph b">Integration</strong></td><td className="entry"><strong className="ph b">Web</strong></td><td className="entry"><strong className="ph b">Mobile</strong></td><td className="entry"><strong className="ph b">Plugin</strong></td></tr><tr className><td className="entry">LambdaTest</td><td className="entry">No specific settings required.</td><td className="entry"><ul className="ul"><li className="li"><p className="p">Include user name and access key in the remote URL or in desired capabilities.</p></li><li className="li"><p className="p">Place <code className="ph codeph">lt:options</code> for other capabilities.</p></li><li className="li"><p className="p">Use <code className="ph codeph">lt:options</code> for device in mobile native app</p></li></ul><p className="p">Note that you can use older desired capabilities.</p></td><td className="entry">N/A</td></tr><tr className><td className="entry">Sauce Labs</td><td className="entry">No specific settings required.</td><td className="entry"><ul className="ul"><li className="li"><p className="p">Put all desired capabilities in <code className="ph codeph">sauce:options</code>.</p></li></ul></td><td className="entry">N/A</td></tr><tr className><td className="entry">BrowserStack</td><td className="entry"><ul className="ul"><li className="li"><p className="p">Place <code className="ph codeph">browserName</code> in desired capabilities.</p></li><li className="li"><p className="p">Place remaining desired capabilities in <code className="ph codeph">bstack:options</code>.</p></li></ul></td><td className="entry"><ul className="ul"><li className="li"><p className="p">Place <code className="ph codeph">platformName</code> in desired capabilities.</p></li><li className="li"><p className="p">Place remaining desired capabilities in <code className="ph codeph">bstack:options</code>.</p></li></ul></td><td className="entry"><ul className="ul"><li className="li"><p className="p">Not supported</p></li></ul></td></tr></tbody></table></div>

:::note Troubleshooting
If you encounter issues with element detection when migrating to BrowserStack for mobile testing, see this troubleshooting document: [Unable to detect all elements during mobile testing on BrowserStack](/katalon-studio/troubleshooting/troubleshoot-mobile-automated-testing/unable-to-detect-all-elements-during-mobile-testing-on-browserstack).
:::

### Transition to W3C standard for mobile testing

With the adoption of Selenium 4 and Appium Java Client 9.2.3, Katalon Studio 10.x introduces significant improvements in mobile testing capabilities, aligning fully with the W3C WebDriver standard. While these enhancements increase compatibility and precision in mobile automation, existing scripts will require updates to remain functional.

#### Prerequisites for mobile testing

Ensure the following mobile drivers are installed to support mobile testing and resolve swipe action issues in Katalon Studio 10.0.0:

- **Android**: Appium UiAutomator2 Driver (version 3.7.0 or higher).
- **iOS**: Appium XCUITest Driver (version 7.21.1 or higher).

#### Changes Due to Java Client Version 9 Refactoring
Appium Java Client 9.2.3 removes support for the legacy JSON Wire Protocol (JWP). Therefore, you must replace all JWP implementations with the corresponding W3C WebDriver protocol standards.

**Action required**: 
- Replace all uses of JSON Wire Protocol with the corresponding W3C Protocol.
    - **Method 1: AppiumDriver and AndroidDriver**

    Replace generic driver declarations:

        - Before (Katalon Studio 9.x):

        ```
        // AppiumDriver
        import io.appium.java_client.AppiumDriver;
        AppiumDriver<?> driver = MobileDriverFactory.getDriver();

        // AndroidDriver
        import io.appium.java_client.android.AndroidDriver;
        AndroidDriver<?> driver = MobileDriverFactory.getDriver();
        ```
        - After (Katalon Studio 10.x):

        ```
        import io.appium.java_client.AppiumDriver;
        AppiumDriver driver = MobileDriverFactory.getDriver();
        ```
    - **Method 2: Replace MobileElement with WebElement**

    Use Selenium's standard WebElement approach.

        - Before (Katalon Studio 9.x):

        ```jsx
        import io.appium.java_client.MobileElement;
        MobileElement startElement = driver.findElementByXPath("xxx");
        ```
        - After (Katalon Studio 10.x):

        ```jsx
        import org.openqa.selenium.WebElement;
        import org.openqa.selenium.By;
        WebElement startElement = driver.findElement(By.xpath("xxx"));
        ```

    - **Method 3: Replace TouchAction with PointerInput for touch interactions**

    The `TouchAction` class has been deprecated in favor of Selenium’s PointerInput, which offers enhanced control for simulating precise touch gestures such as swiping, tapping, and dragging.

        - Before (Katalon Studio 9.x):

            ```jsx
            import io.appium.java_client.TouchAction;
            import io.appium.java_client.touch.WaitOptions;
            import io.appium.java_client.touch.offset.PointOption;

            TouchAction action = new TouchAction(driver)
                .press(PointOption.point(100, 500))
                .waitAction(WaitOptions.waitOptions(Duration.ofMillis(500)))
                .moveTo(PointOption.point(100, 100))
                .release()
                .perform();
            ```

        - After (Katalon Studio 10.x):

        ```jsx
        import org.openqa.selenium.interactions.PointerInput;
        import org.openqa.selenium.interactions.Sequence;
        import java.time.Duration;
        import java.util.Collections;

        PointerInput finger = new PointerInput(PointerInput.Kind.TOUCH, "finger");
        Sequence sequence = new Sequence(finger, 2);

        sequence.addAction(finger.createPointerMove(Duration.ZERO, PointerInput.Origin.viewport(), 100, 500));
        sequence.addAction(finger.createPointerDown(PointerInput.MouseButton.LEFT.asArg()));
        sequence.addAction(finger.createPointerMove(Duration.ofMillis(500), PointerInput.Origin.viewport(), 100, 100));
        sequence.addAction(finger.createPointerUp(PointerInput.MouseButton.LEFT.asArg()));

        driver.perform(Collections.singletonList(sequence));
        ```

    - **Method 4: Using activateApp and terminateApp with InteractsWithApps**

    In Katalon Studio 10.x, handling methods like `activateApp(appId)` and `terminateApp(appId)` require casting the driver to the InteractsWithApps interface.

        - Before (Katalon Studio 9.x):

        ```jsx
        AppiumDriver<?> driver = MobileDriverFactory.getDriver();
        driver.activateApp(appId);
        driver.terminateApp(appId);
        ```

        - After (Katalon Studio 10.x):

        ```jsx
        import io.appium.java_client.AppiumDriver;
        import io.appium.java_client.InteractsWithApps;

        AppiumDriver driver = MobileDriverFactory.getDriver();

        ((InteractsWithApps) driver).activateApp(appId);
        ((InteractsWithApps) driver).terminateApp(appId);
        ```

Implementing these adjustments ensures your mobile automation scripts leverage the full capabilities of the W3C WebDriver standard in Katalon Studio 10.x.      

## Known limitations and issues

### Windows Desktop app testing unavailable in Katalon Studio 10.0.0

Windows Desktop app testing has been temporarily removed due to compatibility issues between Selenium 4 and WinAppDriver.

We are working on an alternative implementation for Desktop app testing in future releases that will be compatible with Selenium 4 and Katalon Studio.

:::warning Warning
If your projects rely on Windows Desktop app testing, we recommend staying on Katalon Studio version 9.x. For more details, see [Customer Support FAQs](/katalon-platform/customer-support-faqs).
:::

### `Browserstack.getCurrentRemoteBrowser()` not supported

For remote testing on BrowserStack, the `Browserstack.getCurrentRemoteBrowser()` function is currently outdated and does not operate with the setup specified for Selenium 4.

### Katalon Compact Utility (KCU) not supported with BiDi

You can record with KCU when BiDi is not enabled during the recording session. However, the test will fail during execution unless you add the desired capability: webSocketUrl=false. This turns off BiDi to ensure successful execution.

Refer to the image below for the desired capability setup details: 
<img className="image" width={700} src={useBaseUrl("/6fd6d09e-367b-416d-9c82-ed6f422904e5/Set_webSocketUrl__false.png")} /> 

### BiDi not working with Incognito mode in Chrome/Edge Chromium

Incognito mode works normally with BiDi in Firefox, allowing tests to execute as expected. However, the browser session fails to start in Chrome, Edge Chromium, and Chrome headless.

For a workaround, set `webSocketUrl = false` in desired capabilities to disable BiDi if Incognito mode is required.

### BiDi not working with custom Chrome/Edge Chromium profiles

When setting the project configuration (capabilities) to open a custom Chrome or Edge Chromium profile with BiDi enabled, the browser session closes immediately after opening.

This behavior is caused by an issue with BiDi Mapper initialization, where the browser encounters a TrustedHTML assignment problem.

You may see the following error: 
```jsx
org.openqa.selenium.SessionNotCreatedException: Could not start a new session. Response code 500. Message: unknown error: Failed to initialize BiDi Mapper: TypeError: Failed to set the 'innerHTML' property on 'Element': This document requires 'TrustedHTML' assignment.
```

### Simple dialogs (alert/prompt) handler behavior

The `unhandledPromptBehavior` capability, which defaults to "dismiss and notify" per W3C standards, dismisses simple dialogs automatically. 

For a workaround, set `unhandledPromptBehavior` to ignore so that you can handle simple dialogs manually.

To learn more about simple dialogs, you can refer to HTML Standard documentation: [Simple dialogs](https://html.spec.whatwg.org/#simple-dialogs).