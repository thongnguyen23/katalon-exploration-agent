---
hide_title: true
title: Search and view test results in Katalon TestOps
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-4099" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Search and view test results in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon TestOps</span> 


To view test reports in Katalon TestOps:
1. On the main menu, click **Reports > Test Runs**.

2. On **Test Runs**, click the **Test Runs** tab as shown below:
  <img className="image" src={useBaseUrl("/99ad1f90-901b-11ed-998d-0242cfbc79b5/TO-Reports-Test_Runs_tab.png")} alt="select Test runs tab" />

**Test Runs** have the following sections:

- **Search bar**: Enter your keywords in the interactive search field. You may choose custom or preset filters to refine your search results.
  <img className="image" src={useBaseUrl("/984cf350-901b-11ed-998d-0242cfbc79b5/TO-Reports-Test_Runs_search_bar.png")} alt="Test runs search bar" />
    
- **Test Run by Status**: Hover your cursor on the interactive diagram to view the statistics of your **Passed** or **Failed** test runs for the day, week or month.
  <img className="image" src={useBaseUrl("/9925ee30-901b-11ed-998d-0242cfbc79b5/TO-Reports-Test_Run_by_Status.png")} alt="Test run by Status column chart" />

- **All Test Runs**: This section provides a quick summary all the test runs executed for your project in list form, including status and test results with its corresponding test environment and test configuration.
    
  <img className="image" src={useBaseUrl("/9a0f8ae0-901b-11ed-998d-0242cfbc79b5/TO-Reports-All_Test_Runs.png")} alt="All test runs list" />    
    The information is organized in the following columns:
    
    - **Status**: Uses a check or an x icon to indicate whether a test run **Passed** or **Failed**.
    - **ID**: A clickable link that directs you to the corresponding test run details page.
    - **Name**: The label name of the test run and its test suite/test suite collection.
    - **Platform - Profile**: The test run operating system, browser and execution profile.
    - **Time**: The test run duration and execution time-stamp.
    - **Status**: A statistics bar that when hovered, displays all test cases and their corresponding statuses . A test case can either **Passed** or **Failed** or in **Error**, **Incomplete**, or **Skipped** status.
        <img className="image" src={useBaseUrl("/9adbb480-901b-11ed-998d-0242cfbc79b5/TO-Reports-Test_case_status.png")} alt="test case statistics bar" />
        
    - **Configuration**: Contains clickable links to the test run's configuration:
        - If you have run a configuration with an agent, the hyperlinked session ID (e.g, #2288) leads you to the session log.
        - If you have linked a test run to a release/build, the hyperlinked release/build name (e.g, Release 1) leads you to the corresponding release page.
        - If you have specified the build label and URL when running with Katalon Runtime Engine, the hyperlinked build name leads you to the build. To learn more about specifying build label with Katalon command line, see [TestOps integration arguments](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-9115).
    - **By**: The user who executed the test run.
    - You can also **Delete** or **Re-import** the test result by selecting the hamburger icon at the **By** column.
      <img className="image" src={useBaseUrl("/98b9bee0-901b-11ed-998d-0242cfbc79b5/TO-Reports-All_test_runs_hamburger_icon.png")} alt="delete or re-import test run result" />
        

## Search a test result by custom fields and tags

After assigning custom fields or tags to test results, you can query test results by custom fields and tags.

1. Go to **Reports** > **Test Runs**.
2. Navigate to the **All Test Runs** section, then the **Custom Fields** and **Tags** below the search bar as shown below:
  
  <img className="image" src={useBaseUrl("/a44abdf0-76c5-11ed-a602-0242cfbc79b5/TO-Reports-Custom_Fields_and_Tags_filter_query.png")} alt="Test runs query filters" />    
3. Select from the **Custom Fields** and/or **Tags** dropdown lists the custom fields and tags which you want to query your test run results.
4. Click **Update** to add them to your filter.

Your test run result is queried successfully using your selected custom fields and tags filters.

  <img className="image" src={useBaseUrl("/a5ecd530-76c5-11ed-a602-0242cfbc79b5/TO-Test_Management-query_result.png")} alt="test result custom field and tags query result" />