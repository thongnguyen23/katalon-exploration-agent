---
title: Set up Visual Testing
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

# Set up Visual Testing

To set up Visual Testing, follows these steps:
1. Enable screenshot capture in Katalon Studio. See [Capture Screenshots](/katalon-studio/test-reports/view-test-reports/view-captured-screenshots-in-katalon-studio-reports).
    - You can only apply visual testing for screenshots taken as checkpoints. For new users, we highly recommend using the following keywords:
        - [[WebUI] Take Screenshot As Checkpoint](/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-a-screenshot-as-checkpoint)
        - [[Mobile] Take Screenshot As Checkpoint](/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-mobile-testing-keywords/mobile-take-screenshot-as-checkpoint)
    - You can also use this [Visual testing sample project](https://github.com/katalon-studio-samples/testops-visual-testing-sample) on Katalon Studio for basic setup. To learn more about using the WebUI sample project, see: [Sample WebUI tests project](/katalon-studio/get-started/sample-projects/webui/sample-webui-project-healthcare-sample-in-katalon-studio).

2. Run a test suite in Katalon Studio. If you have enabled Katalon Studio Integration, Katalon Studio automatically uploads the Test Results to Katalon TestOps.

3. Sign in to [Katalon TestOps](https://testops.katalon.io/login) and go to your project.
4. Go to **Reports > Visual Testing**.
    <img src="https://docs.katalon.com/c09137e0-d08e-11ee-9657-0242c7a41fd4/TO_Reports_Visual_Testing_Navbar.png" alt="The Visual Testing tab within the Reports section in Katalon TestOps." />

5. Click on the ID of a Visual Test Run.
    
    The **Results** page appears. You can see the screenshots (known as **Visual Checkpoints**) captured during a test execution.
    <img src="https://docs.katalon.com/8e861b70-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-visual_test-run-results-page.png" alt="Click the ID of a visual test run to view the results." />
    
6. Select a screenshot to see the details.
    - If you run a Test Suite for the first time, there is no baseline image.
    - If you have existing visual data, you can view the screenshots in the **System-generated baseline collection** folder.
#### Result
You have successfully set up Visual Testing in Katalon TestOps.
