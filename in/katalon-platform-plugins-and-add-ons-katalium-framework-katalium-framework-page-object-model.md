---
hide_title: true
title: Katalium Framework Page Object Model
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalium Framework Page Object Model

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Page Object Model (POM) is a Design Pattern for enhancing test   maintenance and reducing code duplication. Please refer to <a className="xref j-external-link" href="https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#page-object-design-pattern" target="_blank">here</a>   for a detailed explanation and benefits of POM.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Framework provides an abstract class   <code className="ph codeph">com.katalon.kata.selenium.PageTemplate</code> with some   convenient utilities:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Page objects will be initialized automatically in test classes       that extends <code className="ph codeph">com.katalon.kata.testng.TestTemplate</code>.</p>   </li><li className="li">     <p className="p">       <code className="ph codeph">waitUntil</code> methods which wraps       <code className="ph codeph">WebDriverWait</code> patterns to keep the code concise.</p>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is a very simple Selenium Page (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/java/com/katalon/kata/sample/page/CuraAppoinmentPage.java" target="_blank">source     code</a>):</p> 

```jsx
package com.katalon.kata.sample.page;

import com.katalon.kata.selenium.PageTemplate;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;

public class CuraAppoinmentPage extends PageTemplate {
    @FindBy(id = "appointment") private WebElement divAppointment;

    @FindBy(id = "combo_facility") private WebElement facilitySelect;

    @FindBy(id = "txt_comment") private WebElement commentInput;

    @FindBy(id = "txt_visit_date") private WebElement visitDateInput;

    @FindBy(id = "btn-book-appointment") private WebElement bookAppointmentBtn;

    @FindBy(id = "radio_program_medicaid") private WebElement medicaidCheck;

    @FindBy(id = "radio_program_none") private WebElement medicareCheck;

    @FindBy(id = "txt_comment") private WebElement noneCheck;

    @FindBy(name = "hospital_readmission") private WebElement readMissionCheck;

    public boolean isOnPage() {
        try {
            log.info("Check is on appointment page.");
            return divAppointment.isDisplayed();
        } catch (Exception ex) {
            return false;
        }
    }

    public void fillAppointmentDetails(String facility, String visitDate, String comment) {
        log.info("Fill appointment details.");
        waitUntil(ExpectedConditions.elementToBeClickable(facilitySelect));
        Select facilitySelectBox = new Select(facilitySelect);
        facilitySelectBox.selectByVisibleText(facility);
        medicaidCheck.click();
        readMissionCheck.click();
        visitDateInput.sendKeys(visitDate);
        commentInput.sendKeys(comment);
        bookAppointmentBtn.click();
    }
}
```