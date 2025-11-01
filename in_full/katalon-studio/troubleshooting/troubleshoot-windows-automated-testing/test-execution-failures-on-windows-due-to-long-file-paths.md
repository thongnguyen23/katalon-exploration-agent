---
hide_title: true
title: Test execution failures on Windows due to long file paths
---

# <a id="troubleshooting-g2z5i9xp" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Test execution failures on Windows due to long file paths

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><div className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">This issue has been resolved in Katalon Studio version 9.7.2.</p></li></ul></div>For Katalon Studio version 9.7.0 onwards, some users have experienced test execution failures on Windows due to long file paths exceeding the limit of 255 characters.</div></section> 

#### Remedy

1. Copy the installation folder `C:\Users\YourUsername\.katalon\packages\Katalon_Studio_Windows_64` to the `C:\` directory.
2. Rename the folder from `C:\Katalon_Studio_Windows_64` to `C:\Studio`.
3. Launch the application using `C:\Studio\katalon.exe`.
