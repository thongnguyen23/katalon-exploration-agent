---
hide_title: true
title: Create a Test Case in Katalium Framework
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create a Test Case in Katalium Framework

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test cases are essentially TestNG's test classes. Katalium   Framework provides an abstract class   <code className="ph codeph">com.katalon.kata.testng.TestTemplate</code> with some   convenient utilities:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">WebDriver is initialized before each test method and can be       accessed with <code className="ph codeph">this.driver</code> or <code className="ph codeph">driver</code>. If       the test method ends with a <code className="ph codeph">driver.quit()</code> statement, a       new WebDriver will be created for the next test method.</p>   </li><li className="li">     <p className="p">Page instances are also preinitialized using Selenium's       <code className="ph codeph">PageFactory</code>. Refer to <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalium-framework/katalium-framework-page-object-model">this         article</a> to learn more about the Page Object Model.</p>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is a very simple Selenium test (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/java/com/katalon/kata/sample/testcase/simple/LoginTest.java" target="_blank">source     code</a>):</p> 

```jsx
package com.katalon.kata.sample.testcase.simple;

import com.katalon.kata.sample.Constants;
import com.katalon.kata.sample.page.CuraAppoinmentPage;
import com.katalon.kata.sample.page.CuraHomePage;
import com.katalon.kata.sample.page.CuraLoginPage;
import com.katalon.kata.testng.TestTemplate;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends TestTemplate {

  private CuraHomePage curaHomePage = new CuraHomePage(Constants.baseUrl);
  private CuraLoginPage curaLoginPage;
  private CuraAppoinmentPage curaAppoinmentPage;

    @Test
    public void shouldLogin() {
        curaHomePage.open();
        curaHomePage.makeAppointment();
        curaLoginPage.login(Constants.username, Constants.password);
        boolean exist = curaAppoinmentPage.isOnPage();
        Assert.assertTrue(exist);
        driver.quit();
    }
}
```