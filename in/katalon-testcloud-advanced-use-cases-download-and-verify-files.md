---
title: Download and verify files
---
:::caution Requirements
- You have installed the Katalon TestCloud Keywords plugin from Katalon Store. If you have not, visit this site: [Katalon TestCloud Keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
- This keyword is applicable for desktop browser testing on Windows and macOS.
:::

When executing WebUI tests with TestCloud, in some scenarios, you may want to download files and verify them. The following is a ready-to-use `FileExecutor` class that contains custom keywords for downloading and verify files. The keyword file should be placed under the `com.katalon.testcloud` package.

1. In Katalon Studio, click the Profile drop-down and select Reload Plugins to make sure the plugin is installed.
<img width="500" alt="Reload plugins" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/KS_TestCloud_plugin.png" />

2. Add the `FileExecutor.pushFiletoDevice` keyword to your test case.
<img width="600" alt="Add Push file to device keyword" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/add-testcloud-custom-keyword.png" />

3. Configure your TestCloud mobile environment and run the test.


## Read and verify file content
To read the file returned by the keyword <code>FileExecutor.getFileContent</code>, add the following code snippets to your script:

#### Read and verify file as String

```jsx
String fileName = 'sample-1.csv'
String encodedContent = CustomKeywords.'com.katalon.testcloud.FileExecutor.getFileContent'(fileName)
byte[] decodedBytes = Base64.getDecoder().decode(encodedContent);
WebUI.verifyEqual(new String(decodedBytes).contains('Enter stock symbol in cell B4",,,,,POWERED BY'), true)
```

#### Read and verify CSV file as CSV structure 

```jsx
import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.testdata.CSVData
import com.kms.katalon.core.testdata.reader.CSVSeparator

'Get file Content from TestCloud'
String fileName = 'sample-1.csv'
String encodedContent = CustomKeywords.'com.katalon.testcloud.FileExecutor.getFileContent'(fileName)
byte[] decodedBytes = Base64.getDecoder().decode(encodedContent);

'Write the content to a new file'
String newFileLocation = new File(RunConfiguration.getProjectDir() + '/' + fileName).getCanonicalPath()
FileOutputStream outputStream = new FileOutputStream(newFileLocation);
outputStream.write(decodedBytes);
outputStream.close();

'Read the CSV file content (Excluding the headers)'
CSVData csvData = new CSVData(newFileLocation, true, CSVSeparator.COMMA)
List allData = csvData.getAllData()

'Get row 27th, column 2nd'
println allData.get(26).get(1)
```

#### Read and verify CSV file with a dynamic file name in CSV structure

```jsx
import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.testdata.CSVData
import com.kms.katalon.core.testdata.reader.CSVSeparator
import com.kms.katalon.core.webui.driver.DriverFactory
import org.openqa.selenium.WebDriver
import org.openqa.selenium.JavascriptExecutor

'Get name of the latest file downloaded on TestCloud'
WebDriver driver = DriverFactory.getWebDriver()
driver.get('chrome://downloads/')
String fileName = ((JavascriptExecutor) driver).executeScript("return  document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList').items.filter(e => e.state === 2).map(e => e.fileName)[0];")
WebUI.back()

'Get file Content from TestCloud'
String encodedContent = CustomKeywords.'com.katalon.testcloud.FileExecutor.getFileContent'(fileName)
byte[] decodedBytes = Base64.getDecoder().decode(encodedContent);

'Write the content to a new file'
String newFileLocation = new File(RunConfiguration.getProjectDir() + '/' + fileName).getCanonicalPath()
FileOutputStream outputStream = new FileOutputStream(newFileLocation);
outputStream.write(decodedBytes);
outputStream.close();

'Read the CSV file content (Excluding the headers)'
CSVData csvData = new CSVData(newFileLocation, true, CSVSeparator.COMMA)
List<List> allData = csvData.getAllData()

'Get row 27th, column 2nd'
println allData.get(26).get(1)
```