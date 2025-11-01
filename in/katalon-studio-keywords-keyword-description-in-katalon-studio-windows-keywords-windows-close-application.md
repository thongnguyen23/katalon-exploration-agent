---
hide_title: true
title: '[Windows] Close Application'
---

# <a id="topic-5571" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Close Application


## Description

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Trigger a closing event of the running application on the Windows system. This action is similar to pressing <span className="ph uicontrol">ALT</span> + <span className="ph uicontrol">F4</span> and does not force the application to close. </p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If there is a pop-up confirmation, you need to take some extra steps to actually close it.</p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">closeApplication</code></p> 
        

## Example

```jsx
"Start the note pad application"
Windows.startApplication('C:\\Windows\\System32\\notepad.exe')

"Close note pad application"
Windows.closeApplication()
```