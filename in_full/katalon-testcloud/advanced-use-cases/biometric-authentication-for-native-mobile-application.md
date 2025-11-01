---
title: Biometric authentication for native mobile application
---

:::caution requirements
You have installed the Katalon TestCloud Keywords plugin to automatically load all TestCloud keywords into your project without having to manually define them. If you have not, visit Katalon Store: [Katalon TestCloud keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
:::

Biometric authentication in TestCloud supports the following OS and API:

| **OS** | **Supported API** |
| --- | --- |
| Android 11 or higher | <ul><li>`BiometricPrompt` class's `authenticate` method from the AndroidX Biometric library. See: [Androidx Biometric](https://developer.android.com/jetpack/androidx/releases/biometric). </li><li>Android's native `BiometricPrompt` API. See: [Biometric Prompt](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt).</li></ul> |
| iOS 13 or higher | <ul><li>`LAContext` class: This class is used to interact with the local authentication framework. </li><li>`evaluatePolicy`: The evaluatePolicy(_:localizedReason:reply:) method of LAContext that performs biometric authentication, such as verifying a user's face or fingerprint. </li><li>`canEvaluatePolicy`: The canEvaluatePolicy(\_:error:) method of LAContext that checks whether a specific biometric authentication policy can be evaluated on the device.</li></ul> |

The `BiometricsAuthenticator.authenticateFail` and `BiometricsAuthenticator.authenticatePass` keywords in Katalon TestCloud allows users to simulate biometric inputs to test native mobile applications. To use it, follow these steps:

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to make sure the plugin is installed.
    <img src="https://docs.katalon.com/3a871180-56d3-4a86-aa06-9441c30937e4/KS_TestCloud_plugin.png" alt="TestCloud keywords plugin" width="500" />
    
2. Go to **Project Settings** > **Desired Capabilities** > **TestCloud**.
3. In the TestCloud table, add a `katalon:options` property, set **Type** as `Dictionary`, then click the `...`.
    <img src="https://docs.katalon.com/3d76cb0e-d7e8-4c16-8323-869daa78a0ac/KS_TestCloud_desired_caps_menu.png" alt="TestCloud desired caps settings" width="600" />
    
4. In the **Dictionary Property Builder**, add the boolean properties `enableBiometricsAuthentication=True` and `autoAcceptAlerts=False`.
    <img src="https://docs.katalon.com/13f429c6-0b14-46cc-8fd1-8e55087e75f8/KS_TestCloud_biometric_authentication.png" alt="TestCloud set biometric cap" width="500" />
    
    - The `autoAcceptAlerts` desired capability ensures that your test cases run smoothly with the biometric authentication feature.
5. Add the `authenticateFail` and `authenticatePass` keywords to your test case as needed.
    <img src="https://docs.katalon.com/417c9667-990d-4ce2-956c-7f873aebee6f/add-testcloud-custom-keyword.png" alt="TestCloud custom keyword" width="500" />
   
6. Configure your TestCloud mobile environment and run the test.