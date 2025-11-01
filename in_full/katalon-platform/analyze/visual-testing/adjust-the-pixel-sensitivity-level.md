---
title: Adjust the pixel sensitivity level
---
import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel } from "../../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::note
This feature is available for Visual Testing Professional (VTP) package.
:::

When comparing images in Visual Testing, the pixel-based method can pick up minor pixel differences that are not critical to human eyes. To reduce the false positives, you can adjust the pixel sensitivity level and apply it to a whole baseline collection.

To adjust the pixel sensitivity level, follow these steps:

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} default>

1. Go to your **Project** > **Visual Testing**. <br/> The **Visual Test Runs** tab appears. Click on a Test Run ID.
2. Select one of the screenshots to adjust the pixel sensitivity level. Here you can preview if the level matches your preference.
    ![Pixel sensitivity adjust bar](https://docs.katalon.com/d6c07880-6f9d-11ed-a602-0242cfbc79b5/pixel-sensi.png)
    
    You can adjust the level to be stricter or more relaxed. Once the **Diffs** number is 0, it means the minor pixel differences are completely eliminated.
3. You can then set the same pixel sensitivity level for the **Visual Baseline Collection**. This level will be applied to all visual test runs that use the same baseline collection.
    
    ![Compare pixel sensitivity in baseline collection](https://docs.katalon.com/d6cbea30-6f9d-11ed-a602-0242cfbc79b5/pixel-bc.png)
    
#### Result
You have successfully set the pixel sensitivity level for a baseline collection.

  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

1. Go to **Executions**. The Executions list appears by default.
2. Select the test run that has the "**VISUAL TESTING**" label.
3. You are navigated to the Execution Overview page. Switch to the **Visual Testing** tab and select **View Details**.
   <img src="https://tw-cdn.katalon.com/katalon-testops/visual-testing/vt-click-view-details.png" alt="Click view details" width="1080" />
4. Select one of the screenshots to  to adjust the pixel sensitivity level.<br/> You can select the level to be stricter or more relaxed. Once the Diffs number is 0, it means the minor pixel differences are completely eliminated.
   <img src="https://tw-cdn.katalon.com/katalon-testops/visual-testing/vt-adjust-pixel-level.png" alt="Pixel-based comparison" width="1080" /><br/>
5. You can then set the same pixel sensitivity level for the **Visual Baseline Collection**. This level will be applied to all visual test runs that use the same baseline collection.

#### Result
You have successfully set the pixel sensitivity level for a baseline collection.
  
  </TabItem>
</Tabs>

