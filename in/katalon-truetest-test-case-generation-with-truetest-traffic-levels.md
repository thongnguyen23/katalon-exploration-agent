---
title: "Traffic levels"
---

In any application, users navigate through different paths to achieve their goals. On an e-commerce website, for instance, common flows include searching for products, making a purchase, or checking order history. The frequency of these actions is reflected in the traffic level, which shows how often users go through each flow.

<img src="https://tw-cdn.katalon.com/truetest/traffic-levels/truetest-traffic-level-column.png" alt="TrueTest traffic levels" width="800"/>

<br/>
There are four levels to the traffic volume of user flows:

- **High traffic flows**: These are the most frequently used paths in your application. For example, a common flow might be users logging in and checking their order history. Because many users follow this path, it’s considered high priority and should be tested regularly to ensure it’s working correctly. Any issues in these flows will likely affect a large portion of your user base.
- **Medium traffic flows**: Common flows but not as heavily used as high traffic flows. For example, users might browse products and then leave the site. While fewer users complete this flow, it still represents typical user behavior and should be tested to maintain a good user experience.
- **Low traffic flows**: These flows are followed by fewer users but are still important enough to be included in your testing efforts. For example, adding products to a wishlist may not be as common as purchasing them, but it’s still an action that some users rely on.
- **Trivial traffic flows**: These are the least frequent paths that users take. For example, contacting support on an e-commerce site might happen less often in some cases. While fewer users follow these flows, they still need attention, but perhaps not as frequently as the higher-priority ones.

### Understand traffic levels

#### How it helps

The traffic levels help you focus your testing effort on areas that have the most impact on your users and business. Instead of spending time testing everything equally, you can prioritize what’s most important based on real user behavior. This means:

- Efficient testing: You can focus your resources on the most critical paths, ensuring that the most common user actions are always working properly.

- Faster releases: By prioritizing testing, you reduce the time spent on less critical areas, allowing you to release updates more quickly.

- Improved user experience: By ensuring that the most-used flows are always functional, you improve the overall experience for the majority of your users.

In summary, traffic categories help ensure that your testing aligns with how users interact with your application, enabling you to focus on what really matters.

#### High traffic does not always equate high business value

While traffic levels help prioritize testing, higher-traffic flows are not always the most business-critical. For example, on an e-commerce site, users might frequently view products or exit after browsing, which are high-traffic flows. However, completing a checkout process, even though it may have fewer users, is much more critical to the business.

Additionally, high-traffic flows also tend to be simpler, with fewer steps. In contrast, complex flows—like multi-step checkouts or detailed forms—may have lower traffic but still demand thorough testing due to their business impact. Testing should always balance both user behavior and business value to ensure critical processes are functioning correctly.
