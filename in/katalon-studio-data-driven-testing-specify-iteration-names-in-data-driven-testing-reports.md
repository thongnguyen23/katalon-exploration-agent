---
title: Specify iteration names in data-driven testing reports
---

When a test case is executed with a test data row, it is counted as an iteration. This document shows you how to differentiate iterations in test reports.
:::note
- This feature is available for data-driven tests with test suites. The changes only apply in the test suite reports and the **Test Case Table**.
- To learn more about data-driven tests, see [Data-driven Testing with Katalon Studio](/katalon-studio/data-driven-testing/data-driven-testing-with-katalon-studio).
:::

When working with data-driven tests, to quickly identify failed data inputs and parts of the application under test (AUT) that might have a problem, you can add a specific variable from the data file at the end of each iteration name. With this input for iteration name or iteration names, you can differentiate between each iteration in your data-driven testing reports at a glance.

## Set iteration names in data binding

To set iteration names using one of the variables in the test data, do as follows:
1. Perform data-binding from internal data, Excel, CSV, or database data. To learn more about data binding, see [Run Test Case with an external data source](/katalon-studio/data-driven-testing/data-driven-testing-in-a-test-suite).
2. In the **Variable binding** section, click on the **Select** toggle next to **Set Test Name**.

<img src= "https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/specify-iteration-names/set-test-name.png" alt="Set test name" width="800" />

3. A list of variables appears. Choose an option to add to your iteration name.

<img src= "https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/specify-iteration-names/select-variable-name.png" alt="select variable name" width="800" />

4. Save and run your test.

## View data-driven testing reports

### In test cases table

After you set iteration names in data binding, locate and open your test report under **Reports**. In the **Test Cases Table**, you can see your iteration names are marked with the variable in the following syntax: `”Test case name”/”Data binding value” (”Elapsed time”)`.

  <img src= "https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/specify-iteration-names/test-cases-table.png" alt="Test case table" width="800" />

To learn more about Test Case Table and reports, see [Test Suite and Test Suite Collection Reports](/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio). 

### In other reports
  
Katalon Studio supports exporting your test suite execution to HTML, CSV, and PDF formats. The iteration names are marked with the data binding value in the following syntax: `"Test Case ID" | "Data binding value"`. 

:::info
- Katalon Studio version 10.2.0 and is required to view iteration names in CSV and PDF reports.
- This syntax is also supported in **Test case result table** of email reports. To learn more email reports, see: [Share test reports via email](/katalon-studio/test-reports/share-test-reports-via-email-in-katalon-studio).
:::

- In HTML report:
  <img src="https://tw-cdn.katalon.com/katalon-studio/ks-data-driven-specify-iteration-names/ks-html-report.png" alt="View iteration names HTML report" width="800" />
  
- In CSV report (available from 10.2.0):
  <img src="https://tw-cdn.katalon.com/katalon-studio/ks-data-driven-specify-iteration-names/ks-csv-report-1.png" alt="View iteration names in CSV report" width="800" />

- In PDF report (available from 10.2.0):
  <img src="https://tw-cdn.katalon.com/katalon-studio/ks-data-driven-specify-iteration-names/ks-pdf-report.png" alt="View iteration names in PDF report" width="600" />
  
To learn how to export reports to other formats, see [Export reports to other formats](/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio#id_7).
