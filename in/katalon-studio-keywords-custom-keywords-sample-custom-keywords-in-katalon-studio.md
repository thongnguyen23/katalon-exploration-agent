---
hide_title: true
title: Sample Custom Keywords in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Sample Custom Keywords in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When creating a <strong className="ph b">New Custom Keyword</strong>, you have the options to generate sample custom keywords used for either Web, Mobile or API testing. They provide a great example to learn how to create custom keywords with proper coding convention in Katalon Studio from scratch.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The options are displayed directly when you create a new custom keyword.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/sample-custom-keywords/Screen-Shot-2018-03-26-at-13.35.02.png")} /><br /><br /></p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id__cfd381e6-0986-407c-a712-aa8e7ce6810c"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1">Option</th><th className="entry anchor_top_offset" id="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate sample keywords for Web</td><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate some sample functions used for Web Testing</td></tr><tr className><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate sample keywords for Mobile</td><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate some sample functions used for Mobile Testing</td></tr><tr className><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate sample keywords for API</td><td className="entry" headers="id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__1 id__cfd381e6-0986-407c-a712-aa8e7ce6810c__entry__2 ">Generate some sample functions used for API Testing</td></tr></tbody></table> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can select <strong className="ph b">one</strong> or <strong className="ph b">all</strong> of these options to have all sample custom keywords generated in one file. For example, select all options, the generated custom keyword will look like as below:</p> 

```jsx
class sampleKeywords {
    /
     * Refresh browser
     */
    @Keyword
    def refreshBrowser() {
        KeywordUtil.logInfo("Refreshing")
        WebDriver webDriver = DriverFactory.getWebDriver()
        webDriver.navigate().refresh()
        KeywordUtil.markPassed("Refresh successfully")
    }

    /
     * Click element
     * @param to Katalon test object
     /
    @Keyword
    def clickElement(TestObject to) {
        try {
            WebElement element = WebUiBuiltInKeywords.findWebElement(to);
            KeywordUtil.logInfo("Clicking element")
            element.click()
            KeywordUtil.markPassed("Element has been clicked")
        } catch (WebElementNotFoundException e) {
            KeywordUtil.markFailed("Element not found")
        } catch (Exception e) {
            KeywordUtil.markFailed("Fail to click on element")
        }
    }

    /**
      Get all rows of HTML table
     * @param table Katalon test object represent for HTML table
     * @param outerTagName outer tag name of TR tag, usually is TBODY
     * @return All rows inside HTML table
     /
    @Keyword
    def List<WebElement> getHtmlTableRows(TestObject table, String outerTagName) {
        WebElement mailList = WebUiBuiltInKeywords.findWebElement(table)
        List<WebElement> selectedRows = mailList.findElements(By.xpath("./" + outerTagName + "/tr"))
        return selectedRows
    }

    /**
      Check if element present in timeout
     * @param to Katalon test object
     * @param timeout time to wait for element to show up
     * @return true if element present, otherwise false
     /
    @Keyword
    def isElementPresent_Mobile(TestObject to, int timeout){
        try {
            KeywordUtil.logInfo("Finding element with id:" + to.getObjectId())

            WebElement element = MobileElementCommonHelper.findElement(to, timeout)
            if (element != null) {
                KeywordUtil.markPassed("Object " + to.getObjectId() + " is present")
            }
            return true
        } catch (Exception e) {
            KeywordUtil.markFailed("Object " + to.getObjectId() + " is not present")
        }
        return false;
    }

    /**
      Get mobile driver for current session
     * @return mobile driver for current session
     /
    @Keyword
    def WebDriver getCurrentSessionMobileDriver() {
        return MobileDriverFactory.getDriver();
    }

    /**
      Send request and verify status code
     * @param request request object, must be an instance of RequestObject
     * @param expectedStatusCode
     * @return a boolean to indicate whether the response status code equals the expected one
     /
    @Keyword
    def verifyStatusCode(TestObject request, int expectedStatusCode) {
        if (request instanceof RequestObject) {
            RequestObject requestObject = (RequestObject) request
            ResponseObject response = WSBuiltInKeywords.sendRequest(requestObject)
            if (response.getStatusCode() == expectedStatusCode) {
                KeywordUtil.markPassed("Response status codes match")
            } else {
                KeywordUtil.markFailed("Response status code not match. Expected: " +
                        expectedStatusCode + " - Actual: " + response.getStatusCode() )
            }
        } else {
            KeywordUtil.markFailed(request.getObjectId() + " is not a RequestObject")
        }
    }

    /**
      if a key is given make an object of objects by this data column key, otherwise make it an object of an array for each line
     * E.g. use method like such Map propertiesJSON = sampleKeywords.toJSONByKey(findTestData('Other/properties'),'env')
     * @param TestData
     * @param String
     * @return
     /
    @Keyword
    def toJSONByKey(TestData data,String key=null){
        String []columnNames = data.getColumnNames()
        JsonSlurper slurper = new JsonSlurper()

        Map dataJSON = key == null ? [:] : slurper.parseText('{}')

        for (def index : (1..data.getRowNumbers())){
            dataJSON[key == null ? index-1 : data.getValue(key, index)]=slurper.parseText('{}')
            for (def col : (1..data.getColumnNumbers())) {
                String columnName = columnNames[col-1]
                String cellValue = data.getValue(col,index).trim()
                dataJSON[key == null ? index-1 : data.getValue(key, index)][columnName]=cellValue
            }
        }
        return dataJSON
    }


    /**
      Add Header basic authorization field,
     * this field value is Base64 encoded token from user name and password
     * @param request object, must be an instance of RequestObject
     * @param username username
     * @param password password
     * @return the original request object with basic authorization header field added
     */
    @Keyword
    def addBasicAuthorizationProperty(TestObject request, String username, String password) {
        if (request instanceof RequestObject) {
            String authorizationValue = username + ":" + password
            authorizationValue = "Basic " + authorizationValue.bytes.encodeBase64().toString()

            // Find available basic authorization field and change its value to the new one, if any
            List<TestObjectProperty> headerProperties = request.getHttpHeaderProperties()
            boolean fieldExist = false
            for (int i = 0; i < headerProperties.size(); i++) {
                TestObjectProperty headerField = headerProperties.get(i)
                if (headerField.getName().equals('Authorization')) {
                    KeywordUtil.logInfo("Found existent basic authorization field. Replacing its value.")
                    headerField.setValue(authorizationValue)
                    fieldExist = true
                    break
                }
            }

            if (!fieldExist) {
                TestObjectProperty authorizationProperty = new TestObjectProperty("Authorization",
                        ConditionType.EQUALS, authorizationValue, true)
                headerProperties.add(authorizationProperty)
            }
            KeywordUtil.markPassed("Basic authorization field has been added to request header")
        } else {
            KeywordUtil.markFailed(request.getObjectId() + "is not a RequestObject")
        }
        return request
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/sample-custom-keywords/Screen-Shot-2018-03-26-at-13.36.40.png")} /><br /><br /></p> 
