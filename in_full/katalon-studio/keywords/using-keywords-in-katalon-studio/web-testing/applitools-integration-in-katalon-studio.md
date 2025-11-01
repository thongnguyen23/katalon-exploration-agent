---
hide_title: true
title: Applitools integration in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="task-2827" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Applitools integration in Katalon Studio

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">An active Katalon Studio Enterprise license.</p></li><li className="li"><p className="p">You have  installed the Applitools plugin from Katalon Store: <a className="xref j-external-link" href="https://store.katalon.com/product/44/Applitools-Integration" target="_blank">Applitools Integration</a>.</p></li></ul></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To configure Applitools integration, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Plugins</span> &gt; <span className="ph uicontrol">Applitools Integration</span>.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/914ab9b0-22b2-11ed-9930-0242fe3e4a3f/ks-840-applitools-integration.png")} alt="Applitools Integration" /></div></li><li className="li step stepexpand"><span className="ph cmd">Fill in the information:</span><div className="itemgroup info"><ul className="ul"><li className="li"><span className="ph uicontrol">Server URL</span>: The Applitools server URL to integrate with Katalon Studio. This URL can be an Applitools Private Cloud URL.</li><li className="li"><span className="ph uicontrol">API Key</span>: Your Applitools API Key (required). You can learn how to obtain Applitools API Key at Applitools documentation: <a className="xref j-external-link" href="https://applitools.com/docs/topics/overview/obtain-api-key.html" target="_blank">How to obtain Applitools API Key</a>.</li><li className="li"><span className="ph uicontrol">Application Name</span>: The name of the application in Applitools. You do not need to create an application in Applitools beforehand.</li><li className="li"><span className="ph uicontrol">Match Level</span>: The match level in Applitools. To learn more about the match level, you can refer to Applitools documentation: <a className="xref j-external-link" href="https://applitools.com/docs/api/eyes-sdk/enums-gen/enum-global-matchlevel-selenium-java.html" target="_blank">Applitools Match Level.</a></li><li className="li"><p className="p"><span className="ph uicontrol">Visual Grid View Port</span>: [[width1, height1], [width2, height2], ...] (e.g., [[800,600],[1200,630]]). The list of viewports includes width and height for the Applitools visual grid. Once you have specified all browser images, those viewports will be captured and compared. If you leave the <span className="ph uicontrol">Visual Grid View Port</span> empty, Katalon Studio uses the browser viewport at the point of execution.</p><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">For quick testing, you only need to enter the API Key and leave out the rest.</p></li><li className="li"><p className="p">Visual Grid View Port configuration is applicable for both <code className="ph codeph">checkWindow</code> and <code className="ph codeph">checkElement</code> keywords.</p></li></ul></div></li></ul></div></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Use Applitools functions in Recorder

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This plugin provides two custom keywords in <code className="ph codeph">BasicKeywords</code> class, which are helpful to use while recording test cases:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <code className="ph codeph">checkWindow</code> is used to compare the image of the full browser at the point this keyword is called. The images in the last run will be used as baseline for the images in the next run. <ul className="ul"><li className="li">input: a unique string which Applitools will use as the identifier to compare the captured images</li><li className="li">output: compared results from Applitools</li></ul> </li><li className="li"> <code className="ph codeph">checkTestObject</code> is used to compare the image of a specific Test Object at the point this keyword is called. The images in the last run will be used as the baselines for the images in the next run. <ul className="ul"><li className="li">input: a Test Object and unique string that Applitools will use as the identifier to compare the captured images</li><li className="li">output: compared results from Applitools</li></ul> </li></ul> 

## <a id="id_3" class="anchor_top_offset"/>Use Applitools functions in Script mode

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In addition to the two basic custom keywords above, this plugin also provides a set of keywords in <code className="ph codeph">EyesKeywords</code> and <code className="ph codeph">AdvancedKeywords</code> classes which can be use in the script mode:</p> 

```jsx
/**
 * Initialize an Eyes instance without any configuration.
 */
@CompileStatic
@Keyword
static Eyes eyesInit()

/**
 * End the test.
 *
 * @param eyes The initialized eyes object.
 * @return The list of results of the test can be obtained from the object returned.
 */
static List<TestResults> eyesClose(Eyes eyes)

/**
 * Initialize a wrapped WebDriver to starts a test
 *
 * @param testName The name of the test. This name must be unique within the scope of the application name. It may be any string.
 * @param viewportSize Specified viewport for image capturing. If null, the default browser viewport will be used.
 * @return A wrapped WebDriver which enables Eyes trigger recording and frame handling.
 */
static Eyes eyesOpen(String testName, RectangleSize viewportSize)

/**
 * Initialize a wrapped WebDriver to starts a test with a specified baseline name.
 *
 * @param baselineName The environment name that defines baseline. If the name is undefined in the server when the test runs then the name will be created and defined on the server with values of the current test environment defined by a triplet <OS = baselineName, Browser, Viewport>.
 * @param testName The name of the test. This name must be unique within the scope of the application name. It may be any string.
 * @param viewportSize Specified viewport for image capturing. If null, the default browser viewport will be used.
 * @return A wrapped WebDriver which enables Eyes trigger recording and frame handling.
 */
static Eyes eyesOpenWithBaseline(String baselineName, String testName, RectangleSize viewportSize)
```