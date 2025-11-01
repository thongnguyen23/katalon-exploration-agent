---
hide_title: true
title: Unable to execute the current selected test case
---

# <a id="troubleshooting-6560" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to execute the current selected test case

When executing data-driven tests with Excel files, you might encounter the following error:

```jsx
"Unable to execute the current selected test case.

Reason: 

Java.io.IOException: Cannot find the Excel sheet. Please check your data source and try again."
```
### Cause
This issue occurs when the test case or test suite is configured to use a specific sheet in an Excel file, but that sheet has been deleted, renamed, or moved.

### Remedy
1. Open your test case or test suite.
2. Go to the **Data Binding** tab. Ensure the correct Excel file and sheet are selected.
3. If the sheet was changed, update the binding configuration in Katalon Studio.

