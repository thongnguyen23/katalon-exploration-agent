---
hide_title: true
title: Upload test execution results from Katalon Studio to TestRail
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Upload test execution results from Katalon Studio to TestRail
Katalon Studio supports uploading test execution results of a test suite to TestRail as a Test Run in two ways:

- **To a new Test Run**:  By prefixing the test suite name with `S<ID>`, where `<ID>` is a unique suite identifier. Katalon will create a new TestRail Test Run during execution.

- **To an existing Test Run**: By prefixing the test suite name with `R<ID>`, where `<ID>` corresponds to the ID of an existing Test Run in TestRail. The test results will be appended to that Test Run.

## Requirements

- You have configured TestRail integration in Katalon Studio. See [Configure TestRail integration in Katalon Studio](/katalon-studio/integrations/test-management/configure-testrail-integration-in-katalon-studio)

## Upload test results to a new test run in TestRail

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To upload test results from <span className="ph">Katalon Studio</span> to a new test run in TestRail, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, create a new test suite or a dynamic test suite.</span></li><li className="li step stepexpand"><span className="ph cmd">Prepend the name of the test suite with the text <code className="ph codeph">S&lt;ID&gt;</code>, where <code className="ph codeph">&lt;ID&gt;</code> is the test suite ID of your choice.</span><div className="itemgroup stepxmp"><img className="image" width={500} src={useBaseUrl("/243c7ba0-666f-11ed-a602-0242cfbc79b5/ks-new-test-suite.png")} alt="Create a new test suite to upload results to TestRail" /></div></li><li className="li step stepexpand"><span className="ph cmd">Add the mapped test cases to the test suite.</span><div className="itemgroup stepxmp"><img className="image" width={600} src={useBaseUrl("/24457c50-666f-11ed-a602-0242cfbc79b5/ks-add-maped-test-case.png")} alt="Add mapped test cases to test suites" /></div></li><li className="li step stepexpand"><span className="ph cmd">Execute a test suite.</span><div className="itemgroup stepresult">A new Test Run is created in your TestRail project.<p className="p"><img className="image" src={useBaseUrl("/92cc77b0-22b2-11ed-9930-0242fe3e4a3f/KS-View-Test-Run-in-TestRail.png")} alt="View Test Runs in TestRail" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">To view the Test Run details, click on the Test Run.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/92cc0280-22b2-11ed-9930-0242fe3e4a3f/KS-Test-Run-details-in-TestRail.png")} alt="View Test Run details in TestRail" /></div></li><li className="li step stepexpand"><span className="ph cmd">In case you want to upload multiple test results to TestRail at the same time, you can add mapped test suites to a test suite collection.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/92cb6640-22b2-11ed-9930-0242fe3e4a3f/KS-upload-multiple-test-runs-TSC.png")} alt="Add mapped test suites to a test suite collection" /></div><div className="itemgroup stepresult"><span className="ph">Katalon Studio</span> will generate separate Test Runs in TestRail in correspondence with the executed Katalon test suites.</div></li></ol> 

## Upload test results to an existing Test Run in TestRail

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To upload test results to an existing Test Run in TestRail, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, create a new test suite or a dynamic test suite.</span></li><li className="li step stepexpand"><span className="ph cmd">Prepend the name of the test suite with the text <code className="ph codeph">R&lt;ID&gt;</code>, where <code className="ph codeph">&lt;ID&gt;</code> is the <span className="ph uicontrol">Test Suite ID</span> of your choice.</span><div className="itemgroup info">To view the <span className="ph uicontrol">Test Run ID</span>, open your TestRail project and click on the Test Run. The ID is displayed next to the Test Run name.</div><div className="itemgroup stepxmp">We can see that <code className="ph codeph">R8</code> is the ID of the created Test Run.<p className="p"><img className="image" src={useBaseUrl("/92cfac00-22b2-11ed-9930-0242fe3e4a3f/KS-TestRail-Test-Run-ID.png")} alt="View Test Run ID in TestRail" /></p><p className="p">We prepend the Test Suite with the text <code className="ph codeph">R8</code> as follows:</p><p className="p"><img className="image" width={500} src={useBaseUrl("/244bbde0-666f-11ed-a602-0242cfbc79b5/ks-r08.png")} alt="Create test suite for uploading results to an existing test run" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Add the mapped test cases to the test suite.</span><div className="itemgroup info">If you are executing a dynamic test suite, you can query test cases associated with an existing Test Run in TestRail. See <a className="xref" href="/katalon-studio/integrations/test-management/configure-testrail-integration-in-katalon-studio#task-6760">Query test cases linked to TestRail in a dynamic test suite</a>.</div></li><li className="li step stepexpand"><span className="ph cmd">Execute a test suite.</span><div className="itemgroup stepxmp">After we execute the Test Suite, the <span className="ph uicontrol">R8</span> Test Run is updated with new test results.<p className="p"><img className="image" src={useBaseUrl("/92d10b90-22b2-11ed-9930-0242fe3e4a3f/KS-Test-Result-to-TestRail-existing.png")} alt="Upload test results to an existing Test Run in TestRail" /></p></div></li></ol> 

## Best practices

To successfully upload test results from Katalon Studio to TestRail:

- Ensure mapped test cases are added to the test suite.
- The plugin must be properly configured in the **Project > Settings > Plugins >** TestRail section.
- A valid TestRail API token or password must be provided.
- All required custom fields must be configured with valid static values.
- Use a **Test Suite Collection** to upload multiple test suites simultaneously—each suite will be associated with its own Test Run in TestRail.

If the configuration is invalid or required fields are missing or incorrectly typed, the plugin will either:
- Skip uploading that field;
- Log a warning, or;
- Prevent the upload entirely depending on the severity of the mismatch.

