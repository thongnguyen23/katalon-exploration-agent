---
hide_title: true
title: '[WebUI] Click Offset'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Click Offset

<div xmlns="http://www.w3.org/1999/xhtml" className="note attention note_attention"><span className="note__title">Attention:</span> <ul className="ul"><li className="li">This keyword is not supported in the Safari browser.</li></ul></div>

## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on the given element with the relative position (x, y) from the in-view center point of that element. If the target element is behind a loading overlay, Katalon Studio repeatedly tries to click the element for a period configured in <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Execution</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Default wait for element timeout</span></span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">clickOffset</code></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/9c9e3220-038d-11ef-a597-0242fe709ecc/KS_default_wait_for_element_timeout.png")} alt="Katalon Studio Execution settings > default wait for element timeout" /></p> 

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">to</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">TestObject</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Yes</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Represents a web element.</td></tr><tr className><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">offsetX</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">int</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Yes</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Offset from the in-view center point of the element. A negative value means an offset left of the point.</td></tr><tr className><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">offsetY</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">int</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Yes</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Offset from the in-view center point of the element. A negative value means an offset above the point.</td></tr><tr className><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">flowControl</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Optional</td><td className="entry" headers="id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__1 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__2 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__3 id_0__9429b7ef-1f12-4dea-8aa9-81ec28bad7ae__entry__4 ">Specify failure handling schema to determine whether the execution should be allowed to continue or stop. To learn more about failure handling settings, you can refer to this document: <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio#id_1">Failure handling</a> </td></tr></tbody></table> 

## <a id="id_0__id_3" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we want to click on the top left cell of the Tic Tac Toe board. By default, the Default wait for element timeout setting is for 30 seconds. If the Tic Tac Toe board is behind a loading overlay, Katalon Studio will try clicking the button for 30 seconds maximum:</p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS

'Open browser and navigate to Tic Tac Toe site.'
WebUI.openBrowser('https://codepen.io/solartic/full/qEGqNL/')

'Click on the top left cell'
WebUI.clickOffset(findTestObject('Object Repository/Page_CodePen - Tic Tac Toe/canvas_tic-tac-toe-board'), 100, 100)

'Close browser'
WebUI.closeBrowser()
```