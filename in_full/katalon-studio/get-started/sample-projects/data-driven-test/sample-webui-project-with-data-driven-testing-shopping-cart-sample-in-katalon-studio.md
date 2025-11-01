---
title: Sample WebUI project with data-driven testing (Shopping Cart sample) in Katalon Studio
---
This sample demonstrates WebUI testing with data-driven testing in Katalon Studio. This sample also shows you an extensive use of custom keywords in the test case.

The Application Under Test (AUT) is the Katalon shop website: [`http://cms.demo.katalon.com`](http://cms.demo.katalon.com/). You can learn more about WebUI testing in this document: [Introduction to WebUI testing](https://docs.katalon.com/katalon-studio/get-started/supported-applications-under-test-aut/introduction-to-web-testing-in-katalon-studio#id_1).

## Open the Shopping Cart sample project

To open the Shopping Cart sample project, in Katalon Studio, go to **File** > **New Sample Project** > **Sample Web UI Tests Project (Shopping Cart)**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Open-sample-shopping-cart.png"alt="Open Shopping cart sample in Studio"width="700"/>

<br/>

Alternatively, you can download the Shopping Cart sample project from our GitHub repository: [Shopping Cart sample](https://github.com/katalon-studio-samples/shopping-cart-tests).

### Trust dialog on first open

When you open a sample project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

<img alt="trust dialog shopping cart"src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-pop-up/trust dialog shopping cart.png" width="500"/>

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.

:::note NOTES
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::

- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

## Shopping Cart sample project components

## Profiles

To open the execution profile, go to **Profiles** > **default**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Execution-profiles.png"alt="Default profile in the Shopping Cart sample"width="700"/>

<br/>

You can create and save all global variables in the execution profile. They can be used across test cases in your project. To learn more about execution profile, you can refer to this document: [Execution profile](https://docs.katalon.com/katalon-studio/data-driven-testing/global-variables-and-execution-profile).

Katalon creates 19 global variables in this sample project as follows:

| **Name** | **Value** |
| --- | --- |
| urlLogin | http://cms.demo.katalon.com/my-account |
| username | customer |
| password | crz7mrb.KNG3yxv1fbn |
| waitPresentTimeout | 5 |
| urlShop | [http://cms.demo.katalon.com](http://cms.demo.katalon.com/) |
| companyName | KMS |
| address | 119 Nguyen Thi Thap |
| city | HCM |
| country | Vietnam |
| postCode | 70000 |
| Phone | 0359912894 |
| uploadPlaceOrderTimeout | 60 |
| dataFile | Product List |
| inputColumHeader | productName |
| urlProduct | http://cms.demo.katalon.com/product |
| productName | Flying Ninja |
| coupon | KBAW662S |
| firstName | katalon |
| lastName | customer |

## Custom keywords

Katalon also creates sample custom keywords in this sample project. To learn more about custom keywords, you can refer to this document: [Introduction to custom keywords](https://docs.katalon.com/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio).

To view our sample custom keywords, in the **Test Explorer** panel, go to **Keywords** > **sample**. Double-click one of the following .groovy files:

| **Custom-keyword files** | **Description** |
| --- | --- |
| BlockUIDismissed.groovy | This file contains a custom keyword that waits for the overlay in the **Checkout** page to disappear. |
| Checkout.groovy | This file contains custom keywords that perform checkout actions. |
| Login.groovy | This file contains custom keywords that perform login actions. |
| Select2.groovy | This file contains custom keywords that perform selecting actions. |
| Shop.groovy | This file contains custom keywords that perform adding-to-the-cart actions. |
| Utils.groovy | This file contains keywords that assist the keywords in the `Select2.groovy` file. |

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Open-custom-keywords.png"alt="Custom keywords in the Shopping Cart sample"width="400"/>

<br/>

Custom keywords can be reused many times in test cases to perform different actions such as logging in, adding items to the cart, and checking out. You can see the use of custom keywords in our sample test cases as below: [Test cases](https://docs.katalon.com/katalon-studio/get-started/sample-projects/data-driven-test/sample-webui-project-with-data-driven-testing-shopping-cart-sample-in-katalon-studio).

## Test cases

1. Custom-keyword samples test cases
    
    To view the **Custom-keyword samples** test cases in this project, in the **Test Explorer** panel, go to **Test Cases** > **Custom-keyword samples**. Double-click to open one of the following test cases:

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-custom-keywords-Test-case.png"alt="Custom-keyword test cases"width="500"/>

    <br/>
    
    - The test case **Order and check out a single product** adds a single product to the shopping cart, and checks out. The flow in this test case is as follows:
    - We use the `loginIntoApplicationWithGlobalVariable` custom keyword to:
        - Open the [`http://cms.demo.katalon.com`](http://cms.demo.katalon.com/) website with maximized windows.
        - Log in with the username and password defined as the global variables in the execution profile.
    - We go to the **Shop** page.
    - Next, we use the `addToCartWithGlobalVariable` custom keyword to:
        - Add the product to the cart. The product is defined as a global variable in the execution profile.
        - Go to the **Cart** page.
        - Click **Proceed to checkout** to go to the **Checkout** page.
    - For the checkout step, we use the `CheckoutShop` custom keyword to:
        - Click the **Checkout** page.
        - Fill in checkout information. The checkout information is defined as test case variables in the **Variables** tab.
            
            <img src="https://docs.katalon.com/91091cd0-22b2-11ed-9930-0242fe3e4a3f/KS-830-TC-Order-check-out-1-product-variables-tab.png" alt="Order and check out a single product" width="700"/>
            
    - Finally, we use the `logoutFromApplication` custom keyword to:
        - Go to the **My account** page.
        - Click **Log out**.
            
            <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-TC1.gif" alt="Order and check out a single product using coupon" width="800" />
            
            You can see the test script as follows:
            
            ```
            import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
            import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
            import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
            import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
            import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
            import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
            import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
            import com.kms.katalon.core.model.FailureHandling as FailureHandling
            import com.kms.katalon.core.testcase.TestCase as TestCase
            import com.kms.katalon.core.testdata.TestData as TestData
            import com.kms.katalon.core.testobject.TestObject as TestObject
            import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
            import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
            import internal.GlobalVariable as GlobalVariable
            
            CustomKeywords.'sample.Login.loginIntoApplicationWithGlobalVariable'()
            
            WebUI.waitForElementPresent(findTestObject('Pages/Shop page/lnkShop'), GlobalVariable.waitPresentTimeout)
            
            WebUI.click(findTestObject('Pages/Shop page/lnkShop'))
            
            CustomKeywords.'sample.Shop.addToCartWithGlobalVariable'()
            
            CustomKeywords.'sample.Checkout.CheckoutShop'(firstName,lastName,companyName, country, address, city, postCode, Phone)
            
            CustomKeywords.'sample.Login.logoutFromApplication'()
            
            WebUI.closeBrowser()
            ```
            
    - The test case **Order and check out a single product using coupon** adds a single product to the shopping cart, applies a 50% off coupon, then checks out. The flow in this test case is as follows:
    - We use the `loginIntoApplicationWithGlobalVariable` custom keyword to:
        - Open the [`http://cms.demo.katalon.com`](http://cms.demo.katalon.com/) website with maximized windows.
        - Log in with the username and password defined as the global variables in the execution profile.
    - We go to the **Shop** page.
    - Next, we use the `applyCouponAndAddToCartWithGlobalVariable` custom keyword to:
        - Add the product to the cart. The product is defined as a global variable in the execution profile.
        - Go to the **Cart** page.
        - Fill in the coupon code defined as a global variable.
    - For the checkout step, we use the `CheckoutShopWithGlobalVariable` custom keyword to:
        - Click the **Checkout** page.
        - Fill in checkout information. The checkout information is defined as global variables in the execution profile.
    - Finally, we use the `logoutFromApplication` custom keyword to:
        - Go to the **My account** page.
        - Click **Log out**.

            <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-TC2.gif" alt="Order and check out a single product using coupon" width="700" />
            
            You can see the test script as follows:
            
            ```
            import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
            import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
            import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
            import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
            import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
            import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
            import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
            import com.kms.katalon.core.model.FailureHandling as FailureHandling
            import com.kms.katalon.core.testcase.TestCase as TestCase
            import com.kms.katalon.core.testdata.TestData as TestData
            import com.kms.katalon.core.testobject.TestObject as TestObject
            import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
            import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
            import internal.GlobalVariable as GlobalVariable
            
            CustomKeywords.'sample.Login.loginIntoApplicationWithGlobalVariable'()
            
            WebUI.waitForElementPresent(findTestObject('Pages/Shop page/lnkShop'), GlobalVariable.waitPresentTimeout)
            
            WebUI.click(findTestObject('Pages/Shop page/lnkShop'))
            
            CustomKeywords.'sample.Shop.applyCouponAndAddToCartWithGlobalVariable'()
            
            CustomKeywords.'sample.Checkout.CheckoutShopWithGlobalVariable'()
            
            CustomKeywords.'sample.Login.logoutFromApplication'()
            
            WebUI.closeBrowser()
            ```
            
2. Data-driven samples test cases
    
    To view the **Data-driven samples** test cases in this project, in the **Test Explorer** panel, go to **Test Cases > Data-driven samples > Order and check out multiple products**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-DDT-Test-case.png" alt="DDT test cases" width="400" />
    
    The test case **Order and check out multiple products** adds products from the product list to the shopping cart, and checks out. The flow in this test case is as follows:
    
    - We use the `loginIntoApplicationWithGlobalVariable` custom keyword to:
        - Open the [`http://cms.demo.katalon.com`](http://cms.demo.katalon.com/) website with maximized windows.
        - Log in with the username and password defined as the global variables in the execution profile.
    - We go to the **Shop** page.
    - Next, we want the test case to read the data files. To do so, we use the `getAllData()` keyword to extract product names from the product list as follows:
        
        ```
        TestData product = findTestData(GlobalVariable.dataFile)
        List<String> productList = product.getAllData().stream()
        .map{data -> data[0]}/*get first column of each row in data file */
        .collect(Collectors.toList())/add collect and parse to list/
        ```
        
    - Then, we use the `addToCart` custom keyword to add extracted product names to the cart.
        
        ```
        for(def productName : productList){
        CustomKeywords.'sample.Shop.addToCart'(productName.toString(), GlobalVariable.urlProduct)
        }
        ```
        
    - Finally, we use the `CheckoutShopWithGlobalVariable` custom keyword to:
        - Click the **Checkout** page.
        - Fill in checkout information. The checkout information is defined as global variables in the execution profile.

            <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-TC3.gif" alt="Order and check out multiple products" width="700" />

            
            You can see the test script as follows:
            
            ```
            import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
            import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
            import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
            import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
            
            import java.util.stream.Collectors
            
            import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
            import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
            import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
            import com.kms.katalon.core.model.FailureHandling as FailureHandling
            import com.kms.katalon.core.testcase.TestCase as TestCase
            import com.kms.katalon.core.testdata.TestData as TestData
            import com.kms.katalon.core.testobject.TestObject as TestObject
            import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
            import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
            import internal.GlobalVariable as GlobalVariable
            
            CustomKeywords.'sample.Login.loginIntoApplicationWithGlobalVariable'()
            
            WebUI.waitForElementPresent(findTestObject('Pages/Shop page/lnkShop'), GlobalVariable.waitPresentTimeout)
            
            WebUI.click(findTestObject('Pages/Shop page/lnkShop'))
            
            TestData product = findTestData(GlobalVariable.dataFile)
            List<String> productList = product.getAllData().stream()
                        .map{"data -> data[0]"}/*get first column of each row in data file */
                        .collect(Collectors.toList())/*add collect and parse to list*/
            
            for(def productName : productList){
            CustomKeywords.'sample.Shop.addToCart'(productName.toString(), GlobalVariable.urlProduct)
            }
            CustomKeywords.'sample.Checkout.CheckoutShopWithGlobalVariable'()
            WebUI.closeBrowser()
            ```
            

## Data Files

To view the data files in this sample project, in the **Test Explorer** panel, go to **Data Files > Product List/Multiple Checkout**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Data-files.png" alt="Data files in the Shopping Cart sample" width="400"/>

<br/>

Alternatively, you can go to `<your-project-folder>\Data Files` and choose the file you want to open:

- `Constants.xlsx` contains `Product List` and `Multiple Checkout` sheets.
- `Product List.dat` is a list of products you want to add to the shopping cart.
- `Multiple Checkout.dat` is a list of the customer's personal information needed for shipping on the **Checkout** page.

## Test Suites

The sample test suites demonstrate the data-driven testing in Katalon Studio. To view sample test suites, go to the **Test Suite** folder in the **Test Explorer** panel. Double-click to open one of the three following test suites:

1. The test suite **Order and check out a single product multiple times** demonstrates data-driven testing by data-binding.
    
    This test suite binds the test case **Order and check out a single product** with the **Multiple Checkout** data file. After opening the **Test Suite**, click **Show Data Binding** to see the binding data.
    
    To learn more about binding data, you can refer to the following document: [Data Binding](https://docs.katalon.com/katalon-studio/data-driven-testing/manage-data-binding).
    
    <img src="https://docs.katalon.com/910b66c0-22b2-11ed-9930-0242fe3e4a3f/KS-830-TS-Order-check-1-product-multiple-times.png" alt="Order and check out a single product multiple times" width="800" />

    
2. The test suite **Order and check out multiple products** demonstrates data-driven testing by the Groovy script.
    
    This test suite calls the test case **Order and check out multiple products** . This test case reads the **Product list** test data file by using the Groovy script. In the script mode of the test case **Order and check out multiple products**, you can see the following sample code:
    
    ```
    TestData product = findTestData(GlobalVariable.dataFile)
    List<String> productList = product.getAllData().stream()
    .map{data -> data[0]}/*get first column of each row in data file */
    .collect(Collectors.toList())/add collect and parse to list/
    
      /Add extracted product names to cart/
    for(def productName : productList){
    CustomKeywords.'sample.Shop.addToCart'(productName.toString(), GlobalVariable.urlProduct)
    }
    ```
  
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Test-suites-data-testing-goorvy-script.png"alt="Order and check out multiple products"width="800" />

    
3. The test suite **Order and check out with Global Variable** demonstrates data-driven testing by global variables.
    
    In **Order and check out with Global Variable** test suite, we call the **Custom-keywords samples** test cases. These test cases use custom keywords with global variables.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Test-suite-global-variables.png"alt="Order and check out multiple products"width="800" />

    

## Test suite collection

The test suite collection **Shopping-cart-tests - Run All Test Suites** combines the three test suites shown above with different testing environments.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-SHOPPING-Test-suite-collection.png"alt="Shopping-cart-tests - Run All Test Suites"width="1000" />


## Execute selected test case or test suite/test suite collection

To execute a test case or a test suite/test suite collection in the sample project:

1. Select the test case/test suite/test suite collection you want to execute.
2. Click **Run** or press Ctrl + Shift + A (macOS: Cmd+Shift+A).
    
    You can choose different browsers to execute your test in the dropdown list next to **Run**.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/shopping-cart-samples/KS-TOOLBAR-Chrome.png"alt="Run the test case"width="200" />

    
3. Observe the test result in the **Log Viewer** tab. To learn more about analyzing test execution logs, you can refer to this document: [[WebUI] Analyze Test Execution Logs and Debug the Test Case](https://docs.katalon.com/katalon-studio/get-started/sample-projects/webui/webui-analyze-test-execution-logs-and-debug-the-test-case-in-katalon-studio#concept-1867).
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/healthcare-samples/KS-SAMPLES-View-results-in-log-viewer.png"alt="Observe results in the log Viewer" width="800" />

    <br/> 

    :::note Notes

    - You can view test results in the **Result** tab at the test suite or test suite collection level. The test results can be Passed, Failed, Error, or Incomplete. To learn more about the test status, you can refer in this document: [View and Customize Execution Log](https://docs.katalon.com/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio#id_1).
    - After executing test suites or test suite collections, you can view your reports and details in `<your-project-folder>/Reports`. Katalon Studio also supports exporting test reports into different formats, such as HTML, CSV, PDF, and JUnit.
    - For real-time monitoring and better reporting capabilities, consider integrating your project with Katalon TestOps. Learn more about test result reports here: [Upload Test Results to Katalon TestOps from Katalon Studio](https://docs.katalon.com/katalon-studio/get-started/sample-projects/data-driven-test/sample-webui-project-with-data-driven-testing-shopping-cart-sample-in-katalon-studio#).

    :::

    ## See also

   - [Create test cases using Record & Playback](https://docs.katalon.com/katalon-studio/get-started/sample-projects/webui/webui-create-and-run-web-ui-test-case-using-record-and-playback-in-katalon-studio#id_1)