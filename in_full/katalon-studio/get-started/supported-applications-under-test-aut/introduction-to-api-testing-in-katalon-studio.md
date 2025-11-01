---
hide_title: true
title: Introduction to API testing in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Introduction to API testing in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article aims to provide an overview of API testing with   candid answers to the What – When – Why- questions that   hopefully shed light on this mysterious land hidden inside the   boundary of testing – engineering realm.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You will also find potential challenges with API test   implementation – best practices and how to choose right   toolset to help you achieve API testing with a higher success   chance.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>What is API testing?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API testing is a type of software testing that involves testing   application programming interfaces (APIs) directly and as part of   integration testing to determine if they meet expectations for   functionality, reliability, performance, and security. Since APIs   lack a <a className="xref j-external-link" href="https://en.wikipedia.org/wiki/Graphical_user_interface" target="_blank">GUI</a>,   API testing is performed at the message layer and can validate   application logic very quickly and effectively.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API testing is critical for automation testing and CI/CD process   because it can cope with short release cycles and frequent changes   especially the presentation layer without breaking the test   outputs. API testing also requires less maintenance effort compare   to UI automation testing which makes it a preferred choice for   Agile and DevOps teams.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A side note, for Web and mobile applications, API often means   Web services, and API testing refers to the automation test   performed to the Web services.</p> 
    
  
    

## <a id="id_2" class="anchor_top_offset"/>Where is API testing performed?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Commonly, applications have three separate layers or tiers   including Presentation Layer or user interface, Business Layer or   application user interface for business logic processing, and   Database Layer for modeling and manipulating data.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API Testing is performed at the most critical layer, the   Business Layer, where business logic processing is carried out, and   all transactions between User Interface and Database happen.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/Asset-9402x.png")} /><br /><br /> </p> 
    
  
    

## <a id="id_3" class="anchor_top_offset"/>Why do we need to perform API testing?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The figure below shows three different layers of testing called   <a className="xref j-external-link" href="https://martinfowler.com/articles/practical-test-pyramid.html" target="_blank">the     test pyramid</a> initially coined by Mike Cohn in his book   Succeeding with Agile. It has layers representing different types   of testing. Despite its being overly simplistic, it offers us a   general rule of thumb: it suggests how much testing we should focus   on at each layer. As such, API and services tests in the second   layer is an important testing activity that we should focus on.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/Asset-10402x.png")} alt="Why we need perform API testing" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Unit/component tests: This lowest level of testing brings the   highest value and ROI. It is mainly performed by developers. The   unit/component tests can attain between 70% and 80% of code   coverage and require as much effort.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Business rules/Functional tests: This level of testing focuses   on business rules of the application under test. The tests are   designed to test against user stories to ensure that all   implemented functions are working as expected. In Web and mobile   applications, data shown in the user interface is often returned   from servers via API/services. So API testing is performed to   ensure the accuracy of API/services. Testing at this level may need   about 20% of the total testing effort.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Workflow Tests (through the UI): functional UI testing is   performed via the UI of the application to ensure that its features   are built as expected. Due to the fact that automated functional UI   testing is brittle, and any changes in the UI can break the tests,   test automation teams should focus less on this level of   testing.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API testing yields the highest ROI compared to all other testing   type performed by testers as Unit test performed by developers   mostly. It also offers a number of advantages over other kinds of   testing:</p> 
    
  
    

## <a id="id_4" class="anchor_top_offset"/>Advantages of API testing

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As discussed above, API testing is an important activity that   testing teams should focus on. It offers a number of advantages   over other kinds of testing:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <p className="p">Language independent: Data is exchanged via XML and JSON, so any       language can be used for automation, independent from the languages       used to develop the application. XML and JSON are typically       structured data so the verification is fast and stable. There are       also built-in libraries to support comparing data using these data       formats.</p>   </li>   <li className="li">     <p className="p">GUI independent: We can perform API testing within the       application prior to GUI testing. Early testing will get feedback       sooner and improve the team's productivity. Core functionality can       be tested to expose small errors and to evaluate a build's       strengths.</p>   </li>   <li className="li">     <p className="p">Improved test coverage: Most API/services have specifications,       allowing us to create automated tests with high coverage, including       functional testing (happy cases, negative cases) and non-functional       testing. With virtual user techniques, we rarely find API test       cases that could not be automated.</p>   </li>   <li className="li">     <p className="p">Faster releases: It is common that executing a UI regression       test suite takes 8-10 hrs while the same scenario with API testing       takes only 1-2 hours. The flakiness of API testing is also lower       than that of UI testing. All these allow us to release faster with       API testing.</p>   </li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <a className="xref j-external-link" href="https://www.katalon.com/download" target="_blank">     <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/api-testing-interview-question.png")} /><br /><br />   </a> </p> 
    
  
    

## <a id="id_5" class="anchor_top_offset"/>API testing types

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API testing is generally categorized into common categories   below:</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/37314962_134560560788081_95847559624392704_n-1024x576.png")} alt="API Testing Types" /><br /><br /> </p> 
    
                                  

### <a id="id_6" class="anchor_top_offset"/>Validation testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Validation testing is among the final steps and plays an   essential role in the development process. Validation test helps   verify the aspects of product, behavior, and efficiency. In other   words, the validation testing can be seen as an assurance of the   correct development against the stated user needs and   requirements.</p> 

### <a id="id_7" class="anchor_top_offset"/>Functional testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Functional testing includes the testing of particular functions   in the codebase. These features are the representation of specific   scenarios to make sure the API functions are handled well within   the planned parameters.</p> 

### <a id="id_8" class="anchor_top_offset"/>End-to-end testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">UI testing is defined as a test of the user interface for the   API and other integral parts. It is mainly about the UI functions,   in which the interface is naturally graphical or rely on the   command-line endpoint calls.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Generally, the test is more likely of the interface which ties   into the API rather than the API testing itself. Although UI   testing is not a specific test of API in term of the codebase, this   still provides overview information about the health, usability,   and efficiency of both front-end and back-end.</p> 

### <a id="id_9" class="anchor_top_offset"/>Load testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Load testing is generally done after a specific unit, or the   whole codebase has been completed to check if the theoretical   solutions work as the practical plan. Load testing is performed to   ensure the performance under both normal and at peak conditions. To   do so, load testing takes on some various scenarios:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Baseline – tests the API against theoretical regular     traffic that the API expects in ordinary usage;</li><li className="li">Theoretical maximum traffic – this is to make sure during     the full load periods, the solutions respond to those requests     properly;</li><li className="li">Overload test – to test the maximum capability according     to the theory, then add 10-20% more on the peak traffic.   </li></ul> 

### <a id="id_10" class="anchor_top_offset"/>Runtime/Error detection

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This testing type is related to the actual running of the API,   particularly with the universal results of utilizing the API   codebase. Generally, they focus on one of the below aspects:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Monitoring: The runtime of the compiled code is tested for     different implementation errors, handler failures, and other     intrinsic issues to help ensure the codebase does not contain any     insecurity.</li><li className="li">Execution Errors: The code needs to show the response to valid     requests and marks the failure for invalid requests predictably and     in a known way, just the same with valid requests.</li><li className="li">Resource Leaks: The requests which are invalid or commonly     illegal will be submitted to the API to test the memory, resource,     data, or operation leaks/insecurities</li><li className="li">Error Detection: The known failure scenarios will be used to     test the code to make sure the errors are appropriately figured and     resolved</li></ul> 

### <a id="id_11" class="anchor_top_offset"/>Security testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Security, Penetration and Fuzz testing are the three separate   elements of the security auditing process. They are used to ensure   the API implementation is secure from external threats.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Besides enclosing with penetration and fuzz testing, security   testing also includes additional steps like the validation of   encryption methodologies, and of the design of the access control   for the API. It also contains the user rights management and   validating authorization checks to access the resources.</p> 

### <a id="id_12" class="anchor_top_offset"/>Penetration testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Penetration testing is considered the second test in the process   if auditing. In this testing type, the users with limited API   knowledge will try to attack to assess the threat vector from an   outside perspective, which is about functions, resources,   processes, or aim to the entire API and its components.</p> 

### <a id="id_13" class="anchor_top_offset"/>Fuzz testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Fuzz testing is another step in the whole security audit   process. In this testing type, a vast amount of random data   (referred to as "noise" or "fuzz" ), will be input into the system   with the aim to try a forced crash or any negative behavior. This   fuzz test will help test the API in term of the limits to prepare   for the "worst case scenarios."</p> 
    

## <a id="id_14" class="anchor_top_offset"/>API testing best practices

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/API-Testing-Best-Practices-1024x512.png")} alt="API Testing Best Practices" /><br /><br /> </p> 
    
                      
      

### <a id="id_15" class="anchor_top_offset"/>Priorities

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When starting to develop test scenarios, some of us are   relatively common to jump right into some of the negative test   scenarios (to verify invalid information, validation on special   characters, uncommon input, etc.). These types of verification   might cause crashes and other interesting problems. In other words,   easy bugs might be found quickly with negative test scenarios.   Unfortunately, it is not necessarily the best use of a tester's   effort. It is suggested that mainline scenarios should be focus   first with higher priority. A basic guideline is to identify the   most common parameters and conditions that an end developer will   use when calling the APIs and test these scenarios extensively.</p> 
      
    
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="id_16">Functional and non-functional testing priorities</h4> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">API is an essential part of modern web applications, its   non-functional aspects such as performance, security, connectivity   will affect the system heavily. The behavior makes traditional   testing mindset, which focuses on functional testing first, not   suitable anymore. Functional and non-functional testing should be   performed at the same time with equal priority.</p> 
      
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="id_19">Data-driven</h4> 
      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   The most important feature of any API test   tools is the capability of the data-driven approach. Lacking   data-driven ability will lead to test data hardcoded, duplicated   test scripts, test verification, therefore causing massive effort   at maintenance phase.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   Together with data-driven, there are some   important notes for test data that we should pay attention   seriously: data types, blank, empty, null string. With RESTful web   services, the input data is typically in JSON format, and missing   value of a specific key is considered differently (null, empty) in   some cases. To avoid these ambiguous test scenarios, using a subset   of input data models are highly suggested.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <a className="xref j-external-link" href="https://www.katalon.com/download" target="_blank">     <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/api-testing-interview-question.png")} /><br /><br />   </a> </p> 
      
    

### <a id="id_17" class="anchor_top_offset"/>Endpoints management

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   A typical product may have hundreds of API/Web   services endpoints, which look very similar to each other, and   might cause duplication issues to the testing project. How you   organize the tests and the endpoints will influence the   productivity, effectiveness, and maintenance of your tests.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   Test endpoints could be grouped by path   (including path parameters), which generally performance action on   specific object types. For examples:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>api/2/issue: affects to Jira issue{"\n"}{"   "}-- Create issue{"\n"}{"   "}POST /rest/api/2/issue{"\n"}{"   "}-- Create issues{"\n"}{"   "}POST /rest/api/2/issue/bulk{"\n"}{"   "}-- Get issue{"\n"}{"   "}GET /rest/api/2/issue/{"{"}issueIdOrKey{"}"}{"\n"}{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">while</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>api/2/group: affects to Jira Group{"\n"}{"   "}-- Create group{"\n"}{"   "}POST /rest/api/2/group{"\n"}{"   "}-- Get group{"  "}DEPRECATED{"\n"}{"   "}GET /rest/api/2/group{"\n"}{"   "}-- Remove group{"\n"}{"   "}DELETE /rest/api/2/group{"\n"}{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This method will help us preventing missing test endpoints, and   test scenarios.</p> 

### <a id="id_18" class="anchor_top_offset"/>Endpoint as a template

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> This endpoint is a part of the <a className="xref j-external-link" href="http://docs.katalon.com/katalon-studio/tutorials/data-driven-testing/" target="_blank">data-driven approach</a>, which relates to data models more than input data. One of the most challenging issues in API testing is test data mapping with data models, subsets of data models. For examples:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> An API creating new Jira issue requires an input data model having required fields (such as Project Key, Summary) and non-required fields (such as Description, Assignee, etc.). All the combination of required and non-required fields should be tested to ensure that all the test scenarios are covered. For each combination, we then apply data-driven to test with different data set.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> This practice suggests that we consider each combination as a test template for the endpoint, then apply data-driven approach for this test template to generate actual executable test scenarios.</p> 
    

## <a id="id_20" class="anchor_top_offset"/>Challenges in API testing

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/introduction_api_testing/34202954_194986051330169_865881311137497088_n-1-1024x456.png")} alt="challenges api testing" /><br /><br /> </p> 
    
                          

### <a id="id_21" class="anchor_top_offset"/>Initial setup of API testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In API testing, both manual and automated testing matter. While   manual testing confirms whether the app works, automated testing   helps to check how effectively the app performs under pressure.   Setting up the test infrastructure get it working is considered   among the most challenging tasks of the testing process, as it is   not only particularly tricky but also a significantly   motivation-killer. However, it will be a long-term benefit once the   team gets through those challenging setup process.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To avoid these challenges, teams need to start the API testing   in the early stage, specifically in the design phase and make sure   to conduct the interval checking of APIs for 100% uptime.</p> 

### <a id="id_22" class="anchor_top_offset"/>Update the schema of API testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The schema (data formatting which handles requests and responses   for the API) should be maintained during the testing process. Any   changes in the program that create additional parameters for the   API calls must be reflected in the schema configuration.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In today's API economy, the changes in API helps facilitate the   demand, but those changes can cause downtime. To avoid this issue,   the team needs to test the API in beta and alpha environments,   which is seen to reduce 90% of the chances of issues happen.</p> 

### <a id="id_23" class="anchor_top_offset"/>Testing parameter combinations

<p xmlns="http://www.w3.org/1999/xhtml" className="p">APIs handle communication between systems by assigning data   values to parameters and passing these parameters through data   requests. Testing all possible parameter request combinations in   the API is necessary to detect the problems regarding the specific   configurations. A more significant project would end up assigning   two different values to the same parameter, or create instances   where numerical values appear when text values should be. Adding   parameter will aggressively increase the number of possible   combinations.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This challenge can be solved by picking some applications that   aren't very critical to daily operations to utilize the API and   release it to those applications only. By doing this, testers can   know how the API is utilized and whether there are any changes   should be done for a general availability release.</p> 

### <a id="id_24" class="anchor_top_offset"/>Sequencing the API calls

<p xmlns="http://www.w3.org/1999/xhtml" className="p">It is a challenge for testing teams when API needs to be in a   specific order to work correctly. For instance, a call to return a   user's profile information goes through before the profile is   created, the request will return an error. The process can become   even more significantly difficult when involving more   applications.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To help overcome this issue, a flowchart is recommended to   visualize the API calls. Developers then can build and integrate   API calls faster with less unexpected problems.</p> 

### <a id="id_25" class="anchor_top_offset"/>Validating parameters

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Software testing team may find it challenging invalidating the   parameters sent through API requests because of the sheer number of   parameters and use cases for those parameters. Testers need to   ensure all parameter data uses the correct string or numerical data   type, fits within length restrictions, fits within the designated   value range and pass other validation criteria.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To solve this problem, testing team can use the continuous   synthetic API monitoring to detect the problem early. Besides, it   should be combined with an APM solution to get the 360-degree   view.</p> 

### <a id="id_26" class="anchor_top_offset"/>Tracking system integration

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Ensuring the API testing system is working correctly with the   data tracking system is another challenge in API testing. This   integration is essential in bringing back the appropriate responses   on whether a call is working properly. It is also useful in   monitoring the API performance. Tracking system integration is a   late stage in a whole process, which cause the team not to give it   enough attention.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">It can be improved by planning since the design phase to see how   it will integrate with other systems. Each application has various   requirements that need to be met. So, the team should not test in   parallel with other critical integration systems. This can be   achieved by implementing and adding load testing in the continuous   delivery.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See also:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref" href="/katalon-studio/create-test-cases/create-your-first-api-test-with-katalon-studio">Create       your first API test with Katalon Studio</a>   </li><li className="li">Follow this course on Katalon Academy: <a className="xref j-external-link" href="https://academy.katalon.com/courses/api-boost-web-testing-lambdatest/?utm_source=kat_docs_api_intro&utm_medium=bottom_link&utm_campaign=academy_promotion" target="_blank">Leverage       API to Boost Web Testing with Katalon and LambdaTest</a>   </li></ul> 
