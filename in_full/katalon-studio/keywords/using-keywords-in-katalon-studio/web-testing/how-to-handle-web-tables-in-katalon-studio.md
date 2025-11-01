---
hide_title: true
title: How to handle Web Tables in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_handle_web_tables" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to handle Web Tables in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

## <a id="id_1" class="anchor_top_offset"/>What is Web Tables?
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Web table is a collection of rows and columns. For a Web   table, data is stored in cells. Tables are used not only in data   sheets but also in organizing web pages.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Web table normally contains the following tags:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">table – indicates a table.</li>   <li className="li">tbody – defines a container for rows and columns.</li>   <li className="li">tr – specifies a row in the table.</li>   <li className="li">td / th – table data/table header indicating columns in     respective table rows.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">A basic web table</strong> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_web_tables/A-Basic-Webtable.png")} alt="basic web table" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">A basic web table's HTML code looks like     below:</strong> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_web_tables/web-tables-HTML-code.png")} alt="web table html" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Handling Web tables is perhaps much more complicated than any   other elements or controls. This article will show you how to   handle web tables using Katalon Studio.</p> 

## <a id="id_2" class="anchor_top_offset"/>Handle web tables with Katalon Studio

### <a id="id_3" class="anchor_top_offset"/>Example 1: You want to get a text from a Web table and         verify it

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Scenario:</strong>  Let's say we need to find out   which country the 'Pay talk' company in the above table belongs   to.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">First of all, we will find the location of table then we will   store all table elements in the list. Next, we will run a loop and   iterate through each row and column and capture the value in each   cell.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode:</strong> </p> 

```jsx
import org.openqa.selenium.By as By
import org.openqa.selenium.WebDriver as WebDriver
import org.openqa.selenium.WebElement as WebElement
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

WebUI.openBrowser('D:\\Katalon Tutorial\\Katalon Tutorial\\WebTable_Handling_Scenario1.html')
 
WebUI.maximizeWindow()
WebDriver driver = DriverFactory.getWebDriver()

'Expected value from Table'
String ExpectedValue = "Pay Talk";

'To locate table'
WebElement Table = driver.findElement(By.xpath("//table/tbody"))

'To locate rows of table it will Capture all the rows available in the table'
List<WebElement> rows_table = Table.findElements(By.tagName('tr'))

'To calculate no of rows In table'
int rows_count = rows_table.size()
 
'Loop will execute for all the rows of the table'
Loop:
for (int row = 0; row < rows_count; row++) {
    'To locate columns(cells) of that specific row'
    List<WebElement> Columns_row = rows_table.get(row).findElements(By.tagName('td'))
    
    'To calculate no of columns(cells) In that specific row'
    int columns_count = Columns_row.size()
    
    println((('Number of cells In Row ' + row) + ' are ') + columns_count)
    
    'Loop will execute till the last cell of that specific row'
    for (int column = 0; column < columns_count; column++) {
        'It will retrieve text from each cell'
        String celltext = Columns_row.get(column).getText()
        
        println((((('Cell Value Of row number ' + row) + ' and column number ') + column) + ' Is ') + celltext)
        
        'Checking if Cell text is matching with the expected value'
        if (celltext == ExpectedValue) {
            'Getting the Country Name if cell text i.e Company name matches with Expected value'
            println('Text present in row number 3 is: ' + Columns_row.get(2).getText())
        
            'After getting the Expected value from Table we will Terminate the loop'
            break Loop;
        }
    }
}
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode:</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch to <strong className="ph b">manual mode</strong> tab to view test case   step by step.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_web_tables/Handle-webtable.png")} alt="Handle-webtable" /><br /><br /> </p> 

### <a id="id_4" class="anchor_top_offset"/>Example 2: You want to perform actions on the Web table         below

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_web_tables/Web-table.png")} alt="Web-table" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Scenario:</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Let's say we need to edit a student record that has the   graduation year of 2018</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode:</strong> </p> 

```jsx
import org.openqa.selenium.By as By
import org.openqa.selenium.WebDriver as WebDriver
import org.openqa.selenium.WebElement as WebElement
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

WebUI.openBrowser('D:\\Katalon Tutorial\\Katalon Tutorial\\WebTable_Handling_Scenario1.html')

WebUI.maximizeWindow()
 
WebDriver driver = DriverFactory.getWebDriver()

'Expected value from Table'
String ExpectedValue = "Pay Talk";

'To locate table'
WebElement Table = driver.findElement(By.xpath("//table/tbody"))

'To locate rows of table it will Capture all the rows available in the table'
List<WebElement> rows_table = Table.findElements(By.tagName('tr'))

'To calculate no of rows In table'
int rows_count = rows_table.size()
 
'Loop will execute for all the rows of the table'
Loop:
    for (int row = 0; row < rows_count; row++) {
        'To locate columns(cells) of that specific row'
        List<WebElement> Columns_row = rows_table.get(row).findElements(By.tagName('td'))
        
        'To calculate no of columns(cells) In that specific row'
        int columns_count = Columns_row.size()
        
        println((('Number of cells In Row ' + row) + ' are ') + columns_count)
        
        'Loop will execute till the last cell of that specific row'
        for (int column = 0; column < columns_count; column++) {
            'It will retrieve text from each cell'
            String celltext = Columns_row.get(column).getText()
                
            println((((('Cell Value Of row number ' + row) + ' and column number ') + column) + ' Is ') + celltext)
                
            'Checking if Cell text is matching with the expected value'
            if (celltext == ExpectedValue) {
                'Getting the Country Name if cell text i.e Company name matches with Expected value'
                println('Text present in row number 3 is: ' + Columns_row.get(2).getText())
                
                'After getting the Expected value from Table we will Terminate the loop'
                break Loop;
            }
        }
    }
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode:</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch to <strong className="ph b">manual mode</strong> tab to view test case   step by step.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_web_tables/Handle-webtable-2.png")} alt="Handle-webtable-2" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Examples above provide a basic understanding on how to handle   web tables in Katalon Studio. If you are new to automation testing,   it is recommended to take advantage of Manual Mode in Katalon   Studio. For advanced testers, Script Mode provides you flexibility   in creating and manipulating tests. Please download the source code   <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, please refer to <a className="xref" href="/katalon-studio/get-started/workspace-settings/set-up-overview-in-katalon-studio">Katalon Studio     Tutorials</a> and <a className="xref j-external-link" href="https://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
