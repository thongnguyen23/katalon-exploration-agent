---
hide_title: true
title: Supported actions
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-4286" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Supported actions

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Learn the list of actions or operations that are permitted or supported in <span className="ph">Katalon Cloud Studio (Beta)</span>. These actions are already pre-defined for users to accomplish tasks or functions in <span className="ph">Katalon Cloud Studio (Beta)</span>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">You can use the following built-in keywords and add them as test steps to execute your test cases on a web browser.<table className="table anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980"><caption /><colgroup><col style={{width: '100%'}} /><col /><col /><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1">Supported action</th><th className="entry anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2">Keyword</th><th className="entry anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3">What does it do?</th><th className="entry anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4">Return value</th><th className="entry anchor_top_offset" id="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5">Throws an error if</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Check on the <code className="ph codeph">Checkbox object</code> checkbox</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">check</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">Checks a checkbox when the user checks the checkbox object, or it checks on the label associated with the checkbox.</li><li className="li"><p className="p">You can use this keyword with <code className="ph codeph">input[type=checkbox]</code> or <code className="ph codeph">[role=checkbox]</code> objects.</p></li><li className="li"><p className="p">If the checkbox is already checked, the engine does nothing.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object you selected does not exist, or the local engine cannot check the object within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Click on <code className="ph codeph">object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">click</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Clicks on the center of the selected object. </p></li><li className="li"><p className="p">The local engine scrolls the object into view if needed. </p></li><li className="li"><p className="p">The local engine currently does not support clicking on iframe and shadow DOM elements.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object you selected does not exist, or the engine cannot click on the object within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Close the browser</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">closeBrowser</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Closes the browser opened by the local engine.</p></li><li className="li"><p className="p">If there is no browser to close, the local engine does nothing.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 " /></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Double-click on <code className="ph codeph">object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">doubleClick</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Double-clicks on the center of the selected object. </p></li><li className="li"><p className="p">The local engine scrolls the object into view if needed.</p></li><li className="li"><p className="p">The local engine currently does not support clicking on iframe and shadow DOM elements.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the engine cannot click on the object within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Enter <code className="ph codeph">text</code> in <code className="ph codeph">Input field object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">setText</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Sets your provided text into an input field.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or the local engine cannot set your provided text within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Enter a <code className="ph codeph">password</code> in <code className="ph codeph">Password field object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">setEncryptedText</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Sets your encrypted text into a field, which is usually the password field. </p></li><li className="li"><p className="p">The encrypted text cannot be decrypted.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">URL of the current browser window in string format.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the test object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or the engine cannot set encrypted text within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Get URL of the current browser window</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">getURL</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Gets the HTTP/HTTPS URL of the current browser window.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">URL of the current browser window in string format.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no open browser.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Get inner text of <code className="ph codeph">object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">getText</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Gets the visible inner text of the object (the object that doesn't have attribute <code className="ph codeph">visibility: hidden</code> or <code className="ph codeph">display: none</code>), including sub-objects, without any leading or trailing whitespace.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">The inner text of the object in string format.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no open browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Hover over</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">hoverOver</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Simulates the action of hovering the cursor over your target object.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The local engine cannot hover over the object.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Open the browser and navigate to <code className="ph codeph">URL</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">openBrowser</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Opens a browser and navigate to the specified URL. </p></li><li className="li"><p className="p">If the browser has already been opened by the local engine, the local engine uses the opened browser to navigate to the given URL.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">The URL parameter is invalid.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Scroll to <code className="ph codeph">object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">scrollToElement</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Scrolls your selected object into the center of the viewport of the browser window.</p></li><li className="li"><p className="p">The object may not be scrolled completely to the center depending on the layout of the other objects.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Select <code className="ph codeph">value</code> from Dropdown <code className="ph codeph">object</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">selectOptionByValue</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Selects an option from the drop-down list that matches the value you provided. </p></li><li className="li"><p className="p">The local engine currently does not support selecting multiple options from a drop-down list.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or there is no option that matches the given value, or the local engine cannot select the object within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Take screenshot of the current viewport</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">takeScreenshot</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Takes a screenshot of the current viewport.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">The path to the screenshot.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Uncheck on the <code className="ph codeph">Checkbox object</code> checkbox</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">uncheck</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Unchecks a checkbox.</p></li><li className="li"><p className="p">If the checkbox is not checked, the engine does nothing.</p></li><li className="li"><p className="p">You can use this keyword with <code className="ph codeph">input[type=checkbox]</code> or <code className="ph codeph">[role=checkbox]</code> objects.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the local engine cannot uncheck the object within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Verify <code className="ph codeph">element</code> attribute value</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementAttributeValue</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if your selected object has an attribute with the specified name, and the attribute value matches your specified value within the default timeout (30 seconds).</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">3e523ff5-dd45-4bb5-8bda-251ee31d238f:comment:linh.hnguyen@katalon.com:1701234971603The 3e523ff5-dd45-4bb5-8bda-251ee31d238f</p></li></ul><p className="p"><code className="ph codeph">attributeName</code> or <code className="ph codeph">attributeValue</code> is undefined.</p><ul className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The object does not have the attribute, or the actual value of the object's attribute does not match the expected value.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Verify if the <code className="ph codeph">object</code> is not present in the DOM (Document Object Model)</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementNotPresent</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if your selected object is not present in the DOM within your specified timeout.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is not present in the DOM.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object is present in the DOM within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Verify if the <code className="ph codeph">object</code> is present in the DOM (Document Object Model)</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementPresent</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if your selected object is present in the DOM within the default timeout (30 seconds).</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is present in the DOM.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object is not present in the DOM within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Verify that <code className="ph codeph">object</code> contains <code className="ph codeph">expected-text</code></p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementText</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies the inner text of the object matches the text you provided within the default timeout (30 seconds).</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the inner text of the object matches the expected text.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The </p></li></ul><p className="p"><code className="ph codeph">expectedText</code>21b3132c-e11d-4da3-aaff-42a6db96896a:comment:linh.hnguyen@katalon.com:1701234787825 parameter is undefined.21b3132c-e11d-4da3-aaff-42a6db96896a</p><ul className="ul"><li className="li"><p className="p">The object does not exist, or the engine cannot get the text, or the actual inner text of the object does not match the expected text within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Verify that <code className="ph codeph">object</code> is visible</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementVisible</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if the selected element is visible in the current viewport within the default timeout (30 seconds).</p></li><li className="li"><p className="p">If the object is not visible, the display type is <code className="ph codeph">display:none</code>, the computed style is <code className="ph codeph">visibility:hidden</code>, and its size is zero.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is visible.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the object is not visible within the default timeout (30 seconds).</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify URL</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">waitForElementPresent</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Waits for a specific timeout for your selected object to be present in the DOM.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li" /></ul><code className="ph codeph">true</code> if the object is found in the DOM within the specified timeout.<ul className="ul"><li className="li" /></ul><code className="ph codeph">false</code> if the object is not found in the DOM within the specified timeout.</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><p className="p">Wait for <code className="ph codeph">element</code> present</p></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyURL</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if the URL of the current browser window matches your expected URL. </p></li><li className="li"><p className="p">You can specify the expected URL as a complete URL string or using a wildcard.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">No return value</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The </p></li></ul><p className="p"><code className="ph codeph">expectedURL</code> parameter is undefined.</p><ul className="ul"><li className="li"><p className="p">The actual URL of the current browser does not match the expected URL.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify number greater than</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyNumberGreaterThan</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if the object displays a number greater than the expected number. The keyword can compare number value, percentage value, and currency value.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found greater than the expected number. </p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not greater than the expected number. </p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify number less than</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyNumberLessThan</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">Verifies if the object displays a number less than the expected number. The keyword can compare number value, percentage value, and currency value.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found less than the expected number. </p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not less than the expected number. </p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify number greater than or equal</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyNumberGreaterThanOrEqual</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">Verifies if the object displays a number greater than or equal to the expected number. The keyword can compare number value, percentage value, and currency value.</li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found greater than or equal to the expected number. </p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not greater than or equal to the expected number.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul><p className="p">An error is also thrown after a specific timeout if:</p><ul className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The actual number is not greater than or equal to the expected number.</p></li><li className="li"><p className="p">The inner text of the object doesn't contain any number.</p></li></ul> </td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify number less than or equal</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyNumberLessThanOrEqual</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">Verifies if the object displays a number less than or equal to the expected number. The keyword can compare number value, percentage value, and currency value.</li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found less than or equal to the expected number. </p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not less than or equal to the expected number.</p></li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul><p className="p">An error is also thrown after a specific timeout if:</p><ul className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The actual number is not less than or equal to the expected number.</p></li><li className="li"><p className="p">The inner text of the object doesn't contain any number.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 ">Verify element checked</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><span className="keyword">verifyElementChecked</span></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"> Verifies if the object is checked. </li><li className="li">The keyword can be used on </li></ul><code className="ph codeph">input[type=checkbox]</code>, <code className="ph codeph">input[role=checkbox]</code>, <code className="ph codeph">input[type=radio]</code> or <code className="ph codeph">input[role=radio]</code> objects.</td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li"><code className="ph codeph">true</code> if the object is checked</li></ul></td><td className="entry" headers="concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__1 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__2 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__3 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__4 concept-4286__f6f0c40d-13e5-4d18-b1be-64a52a7a5980__entry__5 "><ul className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li></ul><p className="p" /><p className="p">An error is also thrown after a specific timeout if:</p><ul className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The object is unchecked.</p></li><li className="li"><p className="p">The object is not <code className="ph codeph">input[type=checkbox]</code>, <code className="ph codeph">input[role=checkbox]</code>, <code className="ph codeph">input[type=radio]</code>, or <code className="ph codeph">input[role=radio].</code></p></li></ul></td></tr></tbody></table></div>

## <a id="topic-6199" class="anchor_top_offset"/>check

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Check on the <code className="ph codeph">Checkbox object</code> checkbox</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Checks a checkbox when the user checks the checkbox object, or it checks on the label associated with the checkbox.</p></li><li className="li"><p className="p">You can use this keyword with <code className="ph codeph">input[type=checkbox]</code> or <code className="ph codeph">[role=checkbox]</code> objects.</p></li><li className="li"><p className="p">If the checkbox is already checked, the engine does nothing.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object you selected does not exist, or the local engine cannot check the object within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-4241" class="anchor_top_offset"/>click

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on <code className="ph codeph">object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Clicks on the center of the selected object.</p></li><li className="li"><p className="p">The local engine scrolls the object into view if needed.</p></li><li className="li"><p className="p">The local engine currently does not support clicking on iframe and shadow DOM elements.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object you selected does not exist, or the engine cannot click on the object within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-7903" class="anchor_top_offset"/>closeBrowser

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Close the browser</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Closes the browser opened by the local engine.</p></li><li className="li"><p className="p">If there is no browser to close, the local engine does nothing.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

## <a id="topic-2865" class="anchor_top_offset"/>doubleClick

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Double-click on <code className="ph codeph">object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Double-clicks on the center of the selected object.</p></li><li className="li"><p className="p">The local engine scrolls the object into view if needed.</p></li><li className="li"><p className="p">The local engine currently does not support clicking on iframe and shadow DOM elements.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the engine cannot click on the object within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-8246" class="anchor_top_offset"/>setText

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Enter <code className="ph codeph">text</code> in <code className="ph codeph">Input field object</code></p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Sets your provided text into an input field.</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or the local engine cannot set your provided text within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-9193" class="anchor_top_offset"/>setEncryptedText

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Enter a <code className="ph codeph">password</code> in <code className="ph codeph">Password field object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Sets your encrypted text into a field, which is usually the password field.</p></li><li className="li"><p className="p">The encrypted text cannot be decrypted.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The URL of the current browser window in string format.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the test object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or the engine cannot set encrypted text within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-8344" class="anchor_top_offset"/>getURL

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get <code className="ph codeph">URL</code> of the current browser window</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Gets the HTTP/HTTPS URL of the current browser window.</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The URL of the current browser window in string format.</p> 

### Throws an error if

<p xmlns="http://www.w3.org/1999/xhtml" className="p">There is no open browser.</p> 

## <a id="topic-3551" class="anchor_top_offset"/>getText

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get inner text of <code className="ph codeph">object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Gets the visible inner text of the object (the object that doesn't have attribute <code className="ph codeph">visibility: hidden</code> or <code className="ph codeph">display: none</code>), including sub-objects, without any leading or trailing whitespace.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The inner text of the object in string format.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no open browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-6535" class="anchor_top_offset"/>hoverOver

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Hover over</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Simulates the action of hovering the cursor over your target object.</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The local engine cannot hover over the object.</p></li></ul> 

## <a id="topic-6099" class="anchor_top_offset"/>openBrowser

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open the browser and navigate to <code className="ph codeph">URL</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Opens a browser and navigate to the specified URL.</p></li><li className="li"><p className="p">If the browser has already been opened by the local engine, the local engine uses the opened browser to navigate to the given URL.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The URL parameter is invalid.</p> 

### <a id="task-7759" class="anchor_top_offset"/>Edit timeout window for OpenBrowser keyword

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">You can now edit the timeout window when you select the OpenBrowser keyword as your test step in your <span className="ph">Katalon Cloud Studio (Beta)</span> test case.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">The default timeout for <span className="keyword">openBrowser</span> keyword is 30 seconds. In some cases, the AUTs may need more time to load, resulting in the test step failure. <p className="p">You can now set the desired timeout (in seconds) for the engine to wait for the browser to be fully loaded. See the following steps how.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open your test case in Editor view.</span></li><li className="li step stepexpand"><span className="ph cmd">On the Editor view, hover and click the pencil icon to edit the existing OpenBrowser test step in your test case. <img className="image" width={700} src={useBaseUrl("/7da9bb40-1659-11ee-bd0e-0242c7a41fd4/Cloud_Studio_edit_test_step.png")} alt="Click pencil icon to edit the OpenBrowser test step." /></span></li><li className="li step stepexpand"><span className="ph cmd">Tick the checkbox beside <span className="ph uicontrol">Override timeout</span> and provide a timeout value in seconds. <img className="image" width={700} src={useBaseUrl("/cfd01290-8e4d-11ee-ab4f-0242c7a41fd4/Cloud_Studio_override_timeout.png")} alt="Click Override timeout and provide a value." /></span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> The timeout must be set to a value greater than 0 seconds.</div></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save</span> when done.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">The timeout window is now updated with your desired value. <a className="xref" href="/katalon-platform/create-tests/create-tests-using-katalon-cloud-studio-beta/create-and-manage-a-test-case/playback-a-cloud-studio-beta-test-case">Playback a Cloud Studio (Beta) test case</a> to test your changes.</section> 

## <a id="topic-9028" class="anchor_top_offset"/>scrollToElement

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Scroll to <code className="ph codeph">object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Scrolls your selected object into the center of the viewport of the browser window.</p></li><li className="li"><p className="p">The object may not be scrolled completely to the center depending on the layout of the other objects.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-3078" class="anchor_top_offset"/>selectOptionByValue

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Select <code className="ph codeph">value</code> from Dropdown <code className="ph codeph">object</code></p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Selects an option from the drop-down list that matches the value you provided.</p></li><li className="li"><p className="p">The local engine currently does not support selecting multiple options from a drop-down list.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The value parameter is null.</p></li><li className="li"><p className="p">The object does not exist, or there is no option that matches the given value, or the local engine cannot select the object within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-2296" class="anchor_top_offset"/>takeScreenshot

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Take screenshot of the current viewport</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Takes a screenshot of the current viewport.</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The path to the screenshot.</p> 

### Throws an error if

<p xmlns="http://www.w3.org/1999/xhtml" className="p">There is no opened browser.</p> 

## <a id="topic-4803" class="anchor_top_offset"/>uncheck

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Uncheck on the <code className="ph codeph">Checkbox object</code> checkbox</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Unchecks a checkbox.</p></li><li className="li"><p className="p">If the checkbox is not checked, the engine does nothing.</p></li><li className="li"><p className="p">You can use this keyword with <code className="ph codeph">input[type=checkbox]</code> or <code className="ph codeph">[role=checkbox]</code> objects.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the local engine cannot uncheck the object within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-9652" class="anchor_top_offset"/>verifyElementAttributeValue

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify <code className="ph codeph">element</code> attribute value</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if your selected object has an attribute with the specified name, and the attribute value matches your specified value within the default timeout (30 seconds).</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">attributeName</code> or <code className="ph codeph">attributeValue</code> is undefined.</p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The object does not have the attribute, or the actual value of the object's attribute does not match the expected value.</p></li></ul> 

## <a id="topic-5529" class="anchor_top_offset"/>verifyElementNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify if the <code className="ph codeph">object</code> is not present in the DOM (Document Object Model)</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if your selected object is not present in the DOM within your specified timeout.</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> if the object is not present in the DOM.<code className="ph codeph">true</code>.</p> 

## <a id="topic-8514" class="anchor_top_offset"/>verifyElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify if the <code className="ph codeph">object</code> is present in the DOM (Document Object Model)</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if your selected object is present in the DOM within the default timeout (30 seconds).</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> if the object is present in the DOM.<code className="ph codeph">true</code>.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object is not present in the DOM within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-567" class="anchor_top_offset"/>verifyElementText

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify that <code className="ph codeph">object</code> contains <code className="ph codeph">expected-text</code></p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies the inner text of the object matches the text you provided within the default timeout (30 seconds).</p> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <code className="ph codeph">true</code> if the inner text of the object matches the expected text.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedText</code> parameter is undefined.</p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The object does not exist, or the engine cannot get the text, or the actual inner text of the object does not match the expected text within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-7331" class="anchor_top_offset"/>verifyElementVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify that <code className="ph codeph">object</code> is visible</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Verifies if the selected element is visible in the current viewport within the default timeout (30 seconds).</p></li><li className="li"><p className="p">If the object is not visible, the display type is <code className="ph codeph">display:none</code>, the computed style is <code className="ph codeph">visibility:hidden</code>, and its size is zero.</p></li></ul> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is visible.</p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The object does not exist, or the object is not visible within the default timeout (30 seconds).</p></li></ul> 

## <a id="topic-3878" class="anchor_top_offset"/>waitForElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Wait for <code className="ph codeph">element</code> present</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Waits for a specific timeout for your selected object to be present in the DOM.</p> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found in the DOM within the specified timeout.</p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is not found in the DOM within the specified timeout.</p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li></ul> 

## <a id="topic-6065" class="anchor_top_offset"/>verifyURL

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify URL</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Verifies if the URL of the current browser window matches your expected URL.</p></li><li className="li"><p className="p">You can specify the expected URL as a complete URL string or using a wildcard.</p></li></ul> 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p">No return value.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedURL</code> parameter is undefined.</p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The actual URL of the current browser does not match the expected URL.</p></li></ul> 

## <a id="topic-4290" class="anchor_top_offset"/>verifyNumberGreaterThan

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify number greater than</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if the object displays a number greater than the expected number. The keyword can compare number value, percentage value, and currency value.</p> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found greater than the expected number.</p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not greater than the expected number.</p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul> 

## <a id="topic-6956" class="anchor_top_offset"/>verifyNumberLessThan

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify number less than</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if the object displays a number less than the expected number. The keyword can compare number value, percentage value, and currency value.</p> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found less than the expected number.</p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not less than the expected number.</p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">There is no opened browser.</p></li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul> 

## <a id="topic-2375" class="anchor_top_offset"/>verifyNumberGreaterThanOrEqual

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify number greater than or equal</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if the object displays a number greater than or equal to the expected number. The keyword can compare number value, percentage value, and currency value.</p> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found greater than or equal to the expected number.</p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not greater than or equal to the expected number.</p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
An error is also thrown after a specific timeout if:
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The actual number is not greater than or equal to the expected number.</p></li><li className="li"><p className="p">The inner text of the object doesn't contain any number.</p></li></ul> 

## <a id="topic-2230" class="anchor_top_offset"/>verifyNumberLessThanOrEqual

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify number less than or equal</p> 

### Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifies if the object displays a number less than or equal to the expected number. The keyword can compare number value, percentage value, and currency value.</p> 

### Return value

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><code className="ph codeph">true</code> if the object is found less than or equal to the expected number.</p></li><li className="li"><p className="p"><code className="ph codeph">false</code> if the object is found not less than or equal to the expected number. </p></li></ul> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li><li className="li"><p className="p">The <code className="ph codeph">expectedNumber</code> parameter is undefined.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
An error is also thrown after a specific timeout if:
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The actual number is not less than or equal to the expected number.</p></li><li className="li"><p className="p">The inner text of the object doesn't contain any number.</p></li></ul> 

## <a id="topic-5257" class="anchor_top_offset"/>verifyElementChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### WebUI name

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify element checked</p> 

### Description

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Verifies if the object is checked.</li><li className="li">The keyword can be used on the following objects:<ul className="ul"><li className="li"><code className="ph codeph">input[type=checkbox]</code></li><li className="li"><p className="p"><code className="ph codeph">input[type=radio]</code></p></li><li className="li"><p className="p"><code className="ph codeph">input[role=radio]</code></p></li></ul></li></ul> 
 

### Return value

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><code className="ph codeph">true</code> if the object is checked.</p> 

### Throws an error if

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">There is no opened browser.</li><li className="li"><p className="p">The locator of the object is invalid.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
An error is also thrown after a specific timeout if:
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The object does not exist.</p></li><li className="li"><p className="p">The object is unchecked.</p></li><li className="li"><p className="p">The object is not <code className="ph codeph">input[type=checkbox]</code>, <code className="ph codeph">input[role=checkbox]</code>, <code className="ph codeph">input[type=radio]</code>, or <code className="ph codeph">input[role=radio]</code>.</p></li></ul> 
