---
title: "Customize TestCloud environment using Regular Expression"
---

:::info Notes
This feature is applicable for mobile browser and mobile app testing.
:::

In TestOps, you can run mobile tests in TestCloud environment within a desired range of OS versions and devices. This allows for more flexible and targeted test execution. TestCloud supports regular expressions (RegEx) for custom device and OS version ranges. To ensure accuracy for the RegEx syntax, you can refer to [RegExr](https://regexr.com/).

Follow these steps:

## Set custom OS version

1. Go to **Test Execution** > **Schedule Test Run**.

    The **Schedule Test Run** dialog pops up.
2. In the **Environment** section, click the drop-down menu and select **More options**.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/TC_environment_select_more_options_button.png" alt="Select more options" width="500"/>

3. In **Mobile Browsers** or **Mobile Native App** configuration tab, scroll to the bottom of OS version column and select **Custom**.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-regex-for-mobile/testcloud-custom-os-version-settings.png" alt="Select custom settings" width="500"/>
4. Refer to the tables below to set the Regex value for your OS version and device name.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-regex-for-mobile/testcloud-set-custom-os-version-dialog.png" alt="Custom version dialog" width="400"/>

    #### Regex characters for OS versions

    :::note
    For Samsung, Google, and Xiaomi devices, you need to remove the device family prefix and replace “Plus” with “+”. Examples: 
    - Samsung Galaxy A8 Plus → Galaxy A8+ 
    - Google Pixel 3a XL → Pixel 3a XL
    - Xiaomi Redmi Note 8 Pro → Redmi Note 8 Pro
    :::

    | Regex characters | Description | Example |
    | ---------------- | ----------- | ------- |
    | `.*`| Match any version that starts with the given string.<br/> **In the given example**, your device will be allocated any version that starts with 13. | `(13.*)` |
    | `,` | Include more combinations of different versions.<br/> **In the given example**, the regex characters `.*` and `,` are combined to match any OS version containing 13, 14, or 15.| `(13.*), (14.*), (15.*)` |
    | `[]`| Include a range of versions in the combination mentioned using a single character only.<br/> **In the given example**, TestCloud will fetch any OS version available from 12, 13, 15. | `1[235]` |
    | `^` | Is used to negate a character from the search.<br/> **In the given example**, this matches OS versions that begin with 1 and do not have 5 as the next character. | `1[^5].*` |
    | <code>&#124;</code> | Match any of the specified versions in the list.<br/> **In the given example**, <code>&#124;</code> and `.*` are used together to fetch any available OS version containing 13 or 14. | <code>(1(3&#124;4).*)</code> | 

    #### Regex characters for Device name

    | Regex characters | Description | Example |
    | ---------------- | ----------- | ------- |
    | `.*`|  Include all the devices that match the string passed.<br/> **In the given example**, you'll be allocated any device from the Inventory that's an iPhone or a Pixel device respectively. | `(iPhone.*)` |
    | `,` | Include more combinations of different devices in a single expression.<br/> **In the given example**, the regex characters `.*` and `,` are combined to match any device name containing Pixel or Samsung. | `(Pixel.*), (Samsung.*)` |
    | `[]`| Match special/reserved characters such as `+`, `.`, `(`, `)` etc. in the device name search. Not using the `[]` may treat these characters as regex characters.<br/> **In the given example**, you'll be allocated any iPad Pro 12.9 (2022). | `iPad Pro 12[.]9 [(]2022[)].*` |
    | `[]` | Include a range of devices in the combination mentioned using a single character only.<br/> **In the given example**, it'll fetch any device available from Pixel 3, Pixel 3a, Pixel 4, Pixel 5, Pixel 6, Pixel 6 Pro, etc.| `(Pixel [3456].*)` |
    | `$` | The `$` character indicates the end of a string.<br/> **In the given example**, only Pixel 6 devices are allocated & will neglect the Pixel 6 Pro devices. | `(Pixel 6$)` |
    | `^` | The `^` character has multiple purposes. Inside square brackets (e.g., `[^8]`), it negates the character set, matching anything except 8. At the start of a pattern, it asserts that the match must occur at the beginning of a line. When used with a negative lookahead (?!), it helps exclude specific patterns from matching.<br/> **In the given example**, `.*` matches OnePlus devices except those with "8" in the name. | `(OnePlus [^8].*)` |
    | <code>&#124;</code> | Match any of the specified devices in the list.<br/> **In the given example**, you will be allocated any iPad Pro 12.9 (2020), iPad Pro 12.9 (2021), or iPad Pro 12.9 (2022). | <code>iPad Pro 12.9 (202(0&#124;1&#124;2))</code> |


5. Click **Save**. TestCloud will display the Regex value accordingly.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-regex-for-mobile/testcloud-regex-os-version-displayed.png" alt="Regex OS version displayed" width="500"/>

#### Result

You can schedule and run tests with the custom OS version and device.
