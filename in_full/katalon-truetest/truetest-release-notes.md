---
title: TrueTest Release Notes
---

## September 24, 2025

### New features
- Introduced **AI-powered Manual to Automation Conversion**: A seamless integration between Manual Testing and TrueTest. This integration allows testers to **automatically convert manual execution sessions into automated test cases**.
  - **Key benefits**:
    - Remove friction between manual and automation testers by aligning tools and workflows.
    - Accelerate automation at scale by reducing manual scripting effort.
    - Unify test strategy by connecting manual, automated, and AI-generated test cases in one platform.
  
Learn more about this feature: [Generate automated tests with TestPak extension](/katalon-truetest/test-case-generation-with-truetest/generate-automated-tests-with-testpak-extension).
## July 30, 2025

### New features
- Introduced **Session Atrributes Customization** feature: You can now inject custom attributes into a user session using TrueTest’s Web toolkit. This allows users to tailor user sessions to the specific business metadata and requirements, and provides better support for advanced use cases like role-based testing or experiment validation. Learn more with our guide: [Set custom session attributes](/katalon-truetest/test-case-generation-with-truetest/custom-session-attributes).

## July 16, 2025

### Enhancements
- Provided the option to edit the name of a data tracking environment. This enhancement is applicable if there are no test cases generated on that tracking environment. 
- Added free-text filtering for flows in the Map view. You can now search using partial or incomplete text to find flows that contain matching words. For example, entering “google” will match flow(s) that contains the word “googlePixel".
- Added the ability to pause or resume data tracking on an AUT in [Katalon TestOps](https://platform.katalon.io). This setting is located in the **TrueTest AUT Detail** page.


## June 30, 2025

### New features
- Introduced **Test Gap Analysis** feature: a powerful capability that ensures your testing activities align with real user behavior in production. This feature helps teams detect and close coverage gaps by comparing actual user flows with existing test coverage, making regression testing more focused, efficient, and accurate. 
  - The analysis identifies gaps by highlighting pages and actions present in the primary map but missing from the secondary map. It also automatically filters for partially covered/uncovered flows, helping you focus on what is not covered. From there, you can automatically generate test cases for the uncovered flows to achieve complete coverage of critical user journeys seen in production.
  - Learn more about this feature in our guide here: [Test Gap Analysis](/katalon-platform/create-tests/test-case-generation-with-truetest/test-gap-analysis).
- Introduced the TrueTest configuration flow on [Katalon TestOps](https://platform.katalon.io).
  - The concept of Application under Test (AUT) is applied to all accounts, whether or not you use TrueTest. An AUT represents a target application that you test using our platform.
  - You can define multiple AUTs, and for each AUT, they can specify multiple test environments, such as production, staging, QA, etc.
  - Two-level configuration system to support flexible and secure workflows:
    - **Account Level**: **Account Admin** can purchase TrueTest licenses and assign them to desired AUTs with TrueTest enabled. **System Admin** can configure AUT, data tracking, and test execution environments with TrueTest enabled. See [Configure TrueTest Agent](/katalon-platform/create-tests/test-case-generation-with-truetest/configure-truetest-agent#configure-truetest-agent-to-track-data).
    - **Project Level**: **Project Admin** can link a project to an AUT with TrueTest enabled, select a Git repo, and configure other advanced settings for the selected AUT. See [Associate AUT to Project](/katalon-platform/create-tests/test-case-generation-with-truetest/configure-truetest-agent#associate-the-aut-to-a-project).


## May 27, 2025

### New features
- You can now generate a journey map with the data tracked from a specific environment. This means multiple environments (e.g. Production, Staging or AUT) can be specified for data tracking under the same AUT. Data from each environment is used to generate separate journey maps, allowing user behavior to be analyzed independently across different deployment stages.

### Enhancements
- You can now manually edit the AI-generated summary and description of a captured flow before generating test cases. This allows for clearer alignment with testing scope, ease in review, organize, and communication before moving forward with test generation.

## April 24, 2025

### Enhancements
- Improved support for Shadow DOM: The TrueTest Agent now captures smart locator and CSS information for interactive elements, improving the clarity and reliability of generated test objects and steps in Shadow DOM applications.
- Allows users to rename page nodes on the user journey map: You can now edit the default paths (e.g., "/checkout/payment-method") to more clearer, user-friendly labels (e.g., “Payment Info”) for better readability.

## March 20, 2025

### Enhancements
- Added support for linking multiple projects to one application under test. This enables teams to work independently while leveraging the same underlying data, improves scalability, collaboration, and test coverage across business units.
- Improved TrueTest Agent to detect a broader range of HTML elements (e.g. `ENTER` and `TAB` keys, slider, dropdown) and automatically generate corresponding test objects and Katalon Studio keywords.

## Jan 10, 2025

### New features
- Automatically updates test object locators to adapt to UI changes in the application under test (AUT). This feature detects changes like layout or styling updates, and adjusts locators accordingly. This feature helps reduce test failures and maintenance efforts while preserving test reliability.


## Nov 29, 2024

### New features
- TrueTest now supports test data generation to simplify test creation and reduce manual effort. User can choose to:
  - Provide the test data manually.
  - Use TrueTest to generate synthetic data.
  - Use the tracking data as test data in the test cases.
- You can generate test cases directly when viewing the details and test steps of a flow.

## Oct 22, 2024

### New features
- Review and retain obsolete flows: You can review obsolete flows which already have correspondingly generated test cases and decide which to keep. These flows will be retained along with the newly generated set of flows. See [Retain obsolete flows](/katalon-platform/create-tests/test-case-generation-with-truetest/generate-user-journey#retain-obsolete-flows).
- You can now add tags while generating test cases in the **Add tag** field in the **Generate Test Case** dialog.

## September 18, 2024

### New features
- When TrueTest detects dynamic elements, it will generate a single, generalized test object that encapsulates these variations - acknowledged as dynamic test objects. Users can then add variables to the dynamic object to include properties that are relevant to the AUT before executing test cases containing those dynamic test objects. Learn more with the documentation: [Dynamic test objects in TrueTest](/katalon-platform/create-tests/test-case-generation-with-truetest/dynamic-test-objects-in-truetest).
- You can store TrueTest artifacts on Katalon Cloud and download them for local review and execution.

## August 9, 2024

### New features
- View details of a flow: Each flow has a summary, a description, a traffic category and detailed test steps. Users can now easily view those details for each flow shown on the Map view and from the flow list. 
- TrueTest now automatically identifies dynamic elements in URLs and replaces them with placeholders. This ensures generated test cases remain valid and reusable across different URL variations.
