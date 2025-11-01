---
title: "Manage Android's permission in Katalon Studio"
---

To manage Android's permission, you need to set the value of 'autoGrantPermissions' desired capabilities:

```jsx
/**
 * 
 * Enable all permission
 * 
 * @param isEnable
 */
 @Keyword
 public static void EnablePermission(boolean isEnable) {
    DesiredCapabilities.android().setCapability("autoGrantPermissions", isEnable);
} 
```
