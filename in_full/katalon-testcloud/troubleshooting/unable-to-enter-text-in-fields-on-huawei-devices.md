---
title: "Unable to enter text in fields on Huawei devices"
---

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When testing on some Huawei devices, tapping the Password field might cause the on-screen keyboard to display and cover the field. This prevents the test to successfully enter a password, leading to failed tests.</p></section> 

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">To resolve the issue, use the <code>Mobile.hideKeyboard()</code> keyword to dismiss the keyboard when it obstructs the password field.</span></div></section></div>

```jsx
import com.kms.katalon.core.model.FailureHandling as FailureHandling

Mobile.hideKeyboard(FailureHandling.OPTIONAL)
```
