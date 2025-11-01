---
hide_title: true
title: Select test object by indexing
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="task-6572" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Select test object by indexing

Select a specific test object from multiple test objects located by indexing.

<img src="https://docs.katalon.com/4034afa0-fbae-11ee-a597-0242fe709ecc/mobile_text_object_similar_values.png" alt="Select a specific test object from multiple test objects located by indexing" />

In this example, you want to select an object with the following attributes:

```
//*[@class = 'android.widget.TextView' and (@text = '2059010625' or . = '2059010625') and @resource-id = 'com.cardinalhealth.vantus.debug:id/tv_account_id']
```

But there are multiple objects that have similar attributes. If locating with ID, you'll get 6 objects of the same IDs. The only difference here is the text value, `@text = '2059010625'`. In this case, you can remove the `text` attribute and apply indexing to differentiate between objects.

Follow the steps to select a test object by indexing:

1. In Katalon Studio, open **Object Spy > Captured Objects**, and locate similar test objects.
2. Update/add the following XPath expression in the **Locator** field:For the second test object:
    
    ```
    (//*[@class = 'UI element name' and @resource-id = 'resource ID name'])[index number]
    ```
    
    In this example, the XPath expression to be updated/added for the first test object would be:
    
    ```
    (//*[@class = 'android.widget.TextView' and @resource-id = 'com.cardinalhealth.vantus.debug:id/tv_account_id'])[1]
    ```
    
    ```
    (//*[@class = 'android.widget.TextView' and @resource-id = 'com.cardinalhealth.vantus.debug:id/tv_account_id'])[2]
    ```
    
#### Result
Your desired test object is correctly identified based on the indexing values you specified in the XPath expression.

