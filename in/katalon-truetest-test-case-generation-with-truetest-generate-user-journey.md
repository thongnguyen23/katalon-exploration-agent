---
title: Generate user journey
---
import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel } from "../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


After setting up the traffic agent, TrueTest collects and models user journeys that will in turn enable the generation of relevant flows.

TrueTest uses the [MutationObserver API](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver) and [Javascript Listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) to track user interactions on the AUT, such as clicks, inputs, and selections by monitoring changes to the DOM and attaching a listener to DOM elements. The technology combination allows TrueTest to collect detailed data on user behavior. TrueTest then uses the data to generate user journey maps in your AUT.


<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} default>

   To view the list of application domains with generated user journey map, on the TestOps navigation bar, click **TrueTest**. 

   <img src="https://tw-cdn.katalon.com/truetest/TrueTest-G2-Homepage.png" alt="TrueTest journey maps in TestOps" />

   You can click the ID of a map or View details to access its detail page. The detail page includes user flows. See: [View user journey map](/katalon-platform/create-tests/test-case-generation-with-truetest/generate-user-journey#view-user-journey-map).
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

:::caution Prerequisites
- AI features are enabled for your Organization. See [Configure AI services](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/configure-ai-services).
- Make sure the Account Admin/System Admin has configured TrueTest Agent to track data on your AUT. If not, follow this guide: [Configure TrueTest Agent](/katalon-platform/create-tests/test-case-generation-with-truetest/configure-truetest-agent).
:::

  To view the list of application domains with generated user journey map: From the sidebar, go to **Test** > **Journey Maps**.

   <img src="https://tw-cdn.katalon.com/truetest/truetest-journey-map-list-gen3.png" alt="TrueTest journey maps in TestOps" />
  
  </TabItem>
</Tabs>


## Generate new user journey map

You can generate a new user journey map with different time frame.

- Ignore previous flows and overwrite existing test cases: When this option is turned off and you generate a new map, TrueTest will compare all new flows from the new map with the previous map to determine the **Flow Status**. When selected, all new flows are generated independently of the previous map, and the list will display **New** flows only.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

  On the **User Journeys** page, click **Generate New User Journey Map** > select data tracking environment and set time period.
   <img width="500" src="https://tw-cdn.katalon.com/truetest/truetest-generate-journey-map-dialog.png" alt="Generate journey maps in TestOps G2" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

  On the **User Journeys** page, click **Generate New User Journey Map** and select a time period, or customize your preferred time period.
   <img width="500" src="https://tw-cdn.katalon.com/truetest/truetest-gen3-generate-map-dialog.png" alt="Generate journey maps in TestOps G3" />
  
  </TabItem>
</Tabs>


<br/>

The user account that triggers to generate a new map will receive a notification email when the generation is finished. <br/>
A user journey map contain several flows built from user interaction with the AUT. You can select the flows to generate test cases.

## View user journey map

From the map list on the **User Journeys** page, you can click the ID of a map or **View details** to access its detail page. 

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

   <img src="https://tw-cdn.katalon.com/truetest/TrueTest_journey_map_list.png" alt="User journey map" width="800" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

   <img src="https://tw-cdn.katalon.com/truetest/gen3-truetest-view-map-details.png" width="800" alt="View map details in TestOps G3" />
  
  </TabItem>
</Tabs>

<br/> 
A user journey detail page has two sections: visualized map and flows.

### View visualized maps

Here you can find user journeys visualized as a map. The map contains pages and actions representing connections from the source pages to the target pages. You can:
- Select a flow to highlight it in the map.
- Click and drag the pages to re-organize the map.
- Switch on the Highlight traffic volume toggle to see the amount of user activity.
- Double-click on the page to edit page information.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

   <img src="https://tw-cdn.katalon.com/truetest/G2-truetest-fast-hq.gif" alt="Perform actions with user journey map G2" width="800" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

   <img src="https://tw-cdn.katalon.com/katalon-testops/truetest/truetest-view-visualized-map.gif" alt="Perform actions with user journey map G3" width="800" />
  
  </TabItem>
</Tabs>


### View flows

A flow represents an end-to-end path performed by a number of users on the AUT. For example, a common flow on e-commerce applications is: `View a product` > `Add it to cart` > `View cart` > `Complete checkout`.

A user journey map could have a number of different flows. To quickly view the test steps of a flow, click the see more arrow. Click **Edit flow info** to update the summary or description of a flow.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

  <img src="https://tw-cdn.katalon.com/truetest/truetest-rename-flow-final.gif" alt="View and edit flow" /><br/>
  
  To view the flow entity more easily, click the icon to switch to the Flows section.
  <img src="/f26df0f0-5cc3-4f35-b5bf-c4b4eb33d53e/TrueTest_click_expand_flows.png" width="1080" alt="Expand flows view" /><br/>
  
  <img src="/1d444ef0-d52b-11ee-9719-0242c7a41fd4/TrueTest_flow_filtering.png" width="1080" alt="Filter flow" />

  You can filter the flows by their traffic level, availability of test cases, and by flow popularity. You can also search the flows by their summary and description text.
  
  The flow popularity filter allows you to focus on the most frequently used flows by narrowing down the list of flows to a specific percentage.
  
  **Availability of test cases** indicates whether the flows have generated test cases or not.
  
  Click **Export** to export and download all user flows as CSV file.
  
  To view the visualized flow in Map View, click the flow map icon.
  <img src="/2c2ef3d1-933b-41b1-abec-fb9e9fbaebe8/TrueTest_click_map_view.png" width="700" alt="Open map view" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

  <img src="https://tw-cdn.katalon.com/truetest/G3-flow-truetest-fast-hq.gif" alt="View and edit flow in G3" /><br/>
  
  Use the toggle in the upper-left corner to switch between viewing as a branching structure and viewing as a list.
  <img src="https://tw-cdn.katalon.com/truetest/truetest-gen3-switch-flow-view.png" alt="View and edit flow in G3" />

  <br/>

  You can filter the flows by their traffic level, availability of test cases, and by flow popularity.
  <img src="https://tw-cdn.katalon.com/truetest/truetest-gen3-flow-filter-options.png" alt="Filter options for TrueTest flows" />
  <br/>

  1. **Search** – Find flows by entering keywords from their summary or description.
  2. **Traffic** – Filter flows based on traffic levels.
  3. **Status** – Narrow flows by their stability status.
  4. **Flows** – Choose to display all flows or a subset based on availability or other criteria.
  5. **Top Flow %** – Focus on the most frequently used flows by selecting a percentage range (e.g., top 100%, 50%).

The **Test Cases** column shows whether test cases have been generated for each flow.<br/> To export the flow data, click the **Export** icon.
  
  </TabItem>
</Tabs>


**Traffic level** <br/>
Traffic level indicates the relative volume of user sessions that go through a particular flow. It is a good practice to test all flows regularly.

There are four levels based on the percentage of the highest traffic volume observed:
- **High** traffic flows: The most common use flows in your application. It means many users follow this path. For example, a highly common flow can be users logging in and checking their order history.
- **Medium** traffic flows: Common flows but not as heavily used as high traffic flows. For example, users browse products and then leave the site.
- **Low** traffic flows: Flows with fewer users, for example, users adding products to a wishlist.
- **Trivial** traffic flows: The least common paths that users take. For example, contacting support on an e-commerce site might happen less often in some cases.

**Flow Status** <br/>
From the second journey map generation onwards, TrueTest categorizes the flows as stable, new, or obsolete to simplify the review process.
- **Stable**: Flows with no changes that present in both the new and previous maps. Test artifacts remain intact and you can skip reviewing these flows.
- **New**: Flows that did not exist in the previous map and require review.
- **Obsolete**: Flows that appear in the previous map but are no longer in the new map. See more: [Retain obsolete flows](/katalon-platform/create-tests/test-case-generation-with-truetest/generate-user-journey#retain-obsolete-flows).


### Generate test cases

After TrueTest has identified the flows from user interaction, you can decided which flows are relevant to generate test cases. In the **Flow** section, select the flow and click **Generate Test Cases**.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

  <img src="/f103cfff-13c6-403d-9ca0-57cfd2a1e8d6/TrueTest_generate_test_cases_from_flows.png" width="800" alt="Generate test cases from flows" />
  
  <br/>

  Once the test case generation has finished, you can revisit the flow and click **View test case** to view its details.
  
  The generated test cases are stored in the registered script repository. Test case names are automatically generated based on the flow.
  
  <img width="800" src="/18930580-d8fc-11ed-ae00-0242cfbc79b5/ATG_generated_test_cases.png" alt="Generated test cases" />
  
  <br/>
  
  If you store test artifacts in Katalon Cloud and there is at least one test case generated, the download icon is shown and you can download the zipped file of the generated test case.
  
  <img width="800" src="/5fd06af5-0273-4398-adb5-5e0d87958496/truetest-download-zipped-test-case.png" alt="Download zipped test case" />
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

  <img src="https://tw-cdn.katalon.com/truetest/truetest-gen3-click-generate-test-cases.png" alt="Click Generate test cases in G3" width="800" />

  Once the test case generation has finished, you can revisit the flow and click **View test case** to view its details.
  
  The generated test cases are stored in the registered script repository. Test case names are automatically generated based on the flow.
  
  <img width="800" src="https://tw-cdn.katalon.com/truetest/truetest-gen3-view-generated-test-cases.png" alt="View generated test cases" />

  </TabItem>
</Tabs>


### Retain obsolete flows

You can review obsolete flows which already have correspondingly generated test cases and decide which to keep. For obsolete flows, TrueTest will archive within the Git repository. 

A use flow is tagged as **Obsolete** in the following cases:
- The features related to those flows no longer exist in the application
- The application has been updated to introduce new flows
- No users follow the flows during the data collecting period

Follow these steps to retain obsolete flows.

<Tabs groupId="testops-version">
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

1. In the **User Journey Map** section, click **Review obsolete flows** of the relevant map.
   <img src="https://tw-cdn.katalon.com/truetest/TrueTest_review_obsolete_flow_icon.png" width="800" alt="Click review obsolete flows" />
2. The **Obsolete flows list** appears. Select the checkbox of the flow you want to keep, then click **Retain**.
   <img src="/7ddd97fc-99b7-4cea-8c92-dd49f15b1ef6/truetest-select-flows-to-retain.png" width="800" alt="Select flows to retain" />

    A dialog appears to confirm your action. Select **Proceed**.
    <img src="/b8af733f-cc72-4ac5-9ae6-b712c295902c/truetest-retain-flows-confirmation-dialog.png" width="600" alt="Retain flows confirmation dialog" />

3. In case you don't want to keep any flows, select **Archive All**.


<section class="result">
  You are directed to the <strong>User Journey Map</strong> page where you can see the update process of the selected map.
</section>
  
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

1. In the **User Journey Map** section, click the **Review obsolete flows** warning icon of the relevant map.
   <img src="https://tw-cdn.katalon.com/truetest/gen3-truetest-review-obsolete-flow.png" width="700" alt="Click review obsolete flows" width="800" />
2. The **Review Obsolete Flows** window appears. Select the checkbox of the flow you want to keep, then click **Retain** at the lower right of the window.
   <img src="https://tw-cdn.katalon.com/truetest/truetest-gen3-select-flow-to-retain.png" width="800" alt="Select flows to retain" />

    A dialog appears to confirm your action. Select **Proceed**.
    <img src="https://tw-cdn.katalon.com/truetest/truetest-gen3-confirm-retain-flows.png" width="600" alt="Retain flows confirmation dialog" />

3. If you don't want to keep any flows, select **Archive All**.


<section class="result">
  The selected map is updated with the retained flows.
</section>
  
  </TabItem>
</Tabs>


