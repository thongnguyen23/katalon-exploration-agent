---
hide_title: true
title: '[Mobile] Start Existing Application'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] Start Existing Application


## <a id="id_0__id_1" class="anchor_top_offset"/>Description

              
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This keyword is to start an Appium driver and to activate an   installed application by its given application ID.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">startExistingApplication</code></p> 
            
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">The <code className="ph codeph">startExistingApplication</code> keyword is not supported by <span className="ph">TestCloud</span>.</p></div>

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__2">Parameter type</th><th className="entry anchor_top_offset" id="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__1 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__2 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__3 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__4 ">AppId</td><td className="entry" headers="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__1 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__2 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__3 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__4 ">String</td><td className="entry" headers="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__1 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__2 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__3 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__4 ">Yes</td><td className="entry" headers="id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__1 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__2 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__3 id_0__f7d7de49-b6d1-42ef-a620-b53b0910147c__entry__4 ">ID of the tested application that's either         the package name of an Android app or the bundle identifier of an         iOS app.</td></tr></tbody></table> 
                      

## <a id="id_0__id_3" class="anchor_top_offset"/>Example

You want to take a raw screenshot of the Facebook app on your mobile device:

<div xmlns="http://www.w3.org/1999/xhtml" className="p">
  <pre className="pre codeblock"><code>'Start an installed Facebook app on the selected Android device'{"\n"}Mobile.startExistingApplication("com.facebook.katana")</code></pre>
</div>
      
