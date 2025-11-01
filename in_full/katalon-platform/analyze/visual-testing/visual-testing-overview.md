---
title: Visual Testing overview
---

import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel } from "../../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## What is Visual Testing?
Visual testing is an automated process used to verify the user interface (UI) of web and mobile applications, ensuring that the application appears to end users exactly as intended.

With incorporated artificial intelligence (AI), visual testing also refers to the AI image comparison, in which you could compare the visible output (of your tests) against the baseline image using an AI engine.

Since comparing images manually (using human eyes only) could still result in human errors, visual testing allows automated image comparison using AI-powered functions such as pixel-by-pixel detection, text-change detection, and layout-change detection.

Visual testing helps reduce human errors to a minimum because it captures even minor differences between two images, which human eyes might accidentally miss.
:::info notes
A baseline image is a reference image initially configured to compare with other image output from visual testing.
:::

## Insights
If the software has visual issues, functional testing cannot help since it focuses on the software behaviors only.

For example, automated functional tests cannot detect any change regarding the layout, colors, fonts, or misplacement of elements on a website. In such a case, one would need to check for any visual regressions instead, and the apparent solution is to run visual testing.

Furthermore, there is an increasing demand for opening/using software on different platforms. Considering the combination of different operating systems and browsers when developing a website, it is also wise to be aware that the website might display adequately on one browser but improperly on another browser. Hence, testing a website across various platforms is crucial to check for any visual defects. Manually doing so would cost tremendous time and effort, not to mention that the human eyes might still miss one or two minor visual bugs if checking complex layouts.

Running visual tests spots visual bugs faster and more effectively, and it makes sure those bugs cannot slip into production. Consequently, visual testing helps boost productivity, increase product confidence, and optimize user experiences.

## TestOps Visual Testing
Katalon TestOps offers visual testing with three image comparison methods: pixel-based, layout-based, and content-based comparison. Since AI powers the layout-based and content-based methods, TestOps Visual Testing could become an integral part of your visual testing infrastructure.

### Pixel-based comparison
This method compares the pixel resolution of two images to figure out the pixel-by-pixel differences between them.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} default>

   <img src="https://docs.katalon.com/8e99ca80-22b2-11ed-9930-0242fe3e4a3f/vt-jul2022-pixel-comparison.png" alt="visual-testing-pixel-comparison" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

   <img src="https://tw-cdn.katalon.com/katalon-testops/visual-testing/vt-pixel-based-comparison.png" alt="Pixel-based comparison" width="1080" />
  
  </TabItem>
</Tabs>


The advantage of this method is that it is a popular function and easy to understand and implement. This method identifies pixel differences and picks up minor changes that could be trivial or ignorable to the human eyes.

### Layout-based comparison
This method identifies and maps the similar zones between the baseline and checkpoint images, highlighting the layout differences between the two images.

The AI engine will identify the zones on the images.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} default>

   <img src="https://docs.katalon.com/8e98e020-22b2-11ed-9930-0242fe3e4a3f/vt-jul2022-layout-based-comparison.png" alt="visual-testing-layout-based-comparison" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

   <img src="https://tw-cdn.katalon.com/katalon-testops/visual-testing/vt-layout-based-comparison.png" alt="Layout-based comparison" width="1080" />
  
  </TabItem>
</Tabs>

In Katalon TestOps, the zones are categorized into 3 types:
| Label          | Color        | Description                                                                 |
|----------------|--------------|-----------------------------------------------------------------------------|
| Identical      | Green border | UI zones identically rendered in both images.                              |
| Distinguishable| Red border   | UI zones that look identical for the most parts but have some recognizable distinctions. |
| Missing/New    | Pink border  | UI zones that exist in one image but not in the other. |

This method is helpful to review changes identified by the pixel-based comparison, and it spots the changes in layout, color, font, and element location.

### Content-based comparison
This method identifies the text content differences between two images.

The AI engine will identify the zones on the images.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} default>

   <img src="https://docs.katalon.com/8e9a8dd0-22b2-11ed-9930-0242fe3e4a3f/vt-jul2022-text-content-comparison.png" alt="visual-testing-text-content-comparison" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

   <img src="https://tw-cdn.katalon.com/katalon-testops/visual-testing/vt-text-content-comparison.png" alt="Text content-based comparison" width="1080" />
  
  </TabItem>
</Tabs>

In Katalon TestOps, the zones are categorized into 3 types:

| Label         | Color       | Description                                                     |
| ------------- | ----------- |---------------------------------------------------------------- |
| Identical     | Green border | Shows text-look-like zones identically rendered in both images |
| Shifted | Red border  | Shows text-look-like zones with identical but shifted positions |
| Missing/New   | Pink border | Shows text-look-like zones in one image but not in the other. |

This method is useful when there is a lot of text content on the pages. It helps users review and prioritize which text changes are critical and need immediate attention.

For step-by-step instructions to use visual testing in Katalon TestOps, see [Use TestOps Visual Testing](/katalon-platform/analyze/analytics/visual-testing/set-up-visual-testing).

