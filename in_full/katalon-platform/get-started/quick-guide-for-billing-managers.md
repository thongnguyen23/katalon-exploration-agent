---
hide_title: true
title: Quick guide for billing managers
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel, MarjNote_Value } from "../../../reusable-component";

# <a id="concept-4192" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Quick guide for billing managers

This guide is made for Billing Managers or anyone responsible for billing tasks in your organization.

:::info tip
If you don't find the answer you're looking for, please contact our team via [billing@katalon.com](mailto:billing@katalon.com)
:::

## Requirements

You must be assigned the **Account Admin** role to perform any billing actions. Learn more about [roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) and how to [assign Account Admins](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators).

<Tabs>
  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default="true" >

## Activate your Katalon TestOps account
:::info notes
Didn’t receive the email? Contact our self-serve team: [sse@katalon.com](mailto:sse@katalon.com)
:::

If you're a first-time customer, an activation email (**Proof of Delivery**) instructions will be sent to the email used during purchase.

To activate your account, sign in to Katalon TestOps using the **same email address used for the payment**.

## Check your Katalon licenses
:::warning requirements
Make sure you are assigned as an **Account Admin** to view your account's license details.
:::
Log in to [purchase.katalon.com](https://purchase.katalon.com/). Go to the **Subscriptions** tab to view your current subscriptions and how many seats or sessions you currently have.

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/purchase-details.png" alt="Purchase page" /> <br/>

Or, for a detailed view of all your current licenses: Click on **Manage Licenses**

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/license-management.png" alt="License management TO page" /> <br/>

- **Dedicated Licenses**: These licenses are exclusively assigned to a specific Account or Organization. They can be further distributed to sub-Organizations or individual Users.
    
    If licenses are not marked as Dedicated, any user within the Account can access and use them freely.
- **Pool Licenses**: This refers to the number of licenses remaining after subtracting those assigned to direct sub-Organizations. If no licenses are dedicated to sub-Organizations, the Pool equals the total number of Dedicated licenses.
- **Available Licenses**: These are licenses that have not yet been assigned to any sub-Organization or user.

## Payment Method
:::warning requirements
Make sure you are assigned as an **Account Admin** to manage your account's payment.
:::
Katalon offers 2 payment methods to pay your bill:

- Bank Transfer
- Credit Card

### Bank transfer payment

Katalon supports Bank Transfers through both ACH credit transfer and wire transfer. When you place an order using the Bank Transfer option, you will receive payment instructions that include all the necessary information to complete the transaction.

Important: Please ensure that your transfer amount covers all bank fees so that Katalon receives the full amount as stated on the order. Any shortfall due to bank charges may delay the processing of your order.

The payment deadline for any order is set at 7 days from the date of your order placement. Katalon will activate your subscription as soon as the payment is completed. If Katalon does not receive any payment by the end of the 7th day, your order will be automatically canceled. If the order is canceled but you still wish to make your purchase, you will have to place your order again.

If you pay the renewal fee via Bank Transfer, you will receive *a reminder email* 7 days before the renewal date (or expiry date), providing details about your upcoming renewal with a payment instruction. On the renewal date, if you have not completed your renewal amount, your subscription will expire and be terminated. You then get a confirmation email for the cancellation.

- Payment may take 1-3 business days to reach Katalon's bank account. It must be received by the due date to avoid any order cancellation.
- You can make either a single payment or multiple partial payments within 7 days, but make sure the total sums match the total invoice amount.
- You cannot place a new order until you settle the outstanding balance of your pending payment.

For further assistance, please contact our self-serve team via [billing@katalon.com](mailto:billing@katalon.com).

### Credit card payment

Katalon supports Credit Card payment. You can only use **one card** in each Account for all your subscription purchases, including renewals.

When you place an order with a credit card, you will receive a confirmation email once your payment is successful, and Katalon will activate your subscription instantly.

- If you pay the renewal fee with your Credit Card, you will receive *a reminder email* 7 days before the renewal date (or expiry date), providing details about your upcoming renewal.
    - On the renewal date, your credit card will be charged the renewal fee.
    - In case of a payment failure, the system will offer a 7-day period from the renewal date, you will be notified to update your payment details within this period. Make sure the payment is completed within this 7-day period; otherwise, your subscription will be terminated until a successful payment is made.

The following is a guide on how to manage your card information.

### Update new credit card information

In Katalon TestOps, you can only save **one card** in each organization. If you want to replace your credit card, follow these steps to update your card information:

1. Go to the [purchase.katalon.com](http://purchase.katalon.com/), click **Payment & Billing** tab,
2. Choose **Card** as **Payement Method**
3. Click **Update**.
4. Enter your new payment information, then click **Save**. The new card is now used by default for all billing purposes, including subscription renewals.

    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/update-card.png" alt="Purchase page update credit card" width="900"/> <br/>

### Delete an existing credit card
:::info notes
- You cannot undo this action. Once you delete the card, it is permanently removed from your organization.
- Once you delete the card, Bank Transfer is **automatically** set as the **default** payment method.
:::
Follow these steps to delete an existing credit card:

1. Go to the [Purchase - Katalon Studio](http://purchase.katalon.com/) , click **Payment & Billing** tab
    
2. Click **`...`** icon, then choose **Delete**

    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/delete_card.png" alt="Purchase page delete card" width="900"/> <br/>

---

## Subscription Management

:::warning requirements
Make sure you are assigned as an **Account Admin** to manage your account's payment.
:::
### View renewal date

Renewal dates for Katalon subscriptions vary depending on the purchase date of each subscription. Your subscription will automatically renew on the expiry date.

Go to the [purchase.katalon.com](http://purchase.katalon.com/), click **Payment & Billing** tab. The renewal date for each subscription will show as: 
`Status: Auto renews on July 29, 2025`

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/check-renew.png" alt="Purchase page subs details" width="900"/> <br/>

### Cancel your subscription:

If you cancel your subscription before the expiry date, you will not be charged for your next billing cycle and will continue to use the subscription until the end of its expiry date.

Subscription cancellation **does not issue a refund** and the subscription remains active until the end of the current billing period.

1. Go to the [purchase.katalon.com](http://purchase.katalon.com/).
2. Click **Payment & Billing** tab.    
3. Turn off the Auto-renew on **toggle** for the subscription you want to cancel.
4. A confirmation popup will appear. Click **Turn off** to proceed.

    **Note:** You can also reactivate your subscription if it has not reached the expiry date yet.

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/turn-off-renew.png" alt="Purchase page turn off renew" width="900"/> <br/>

### Add more session or license to your Katalon subscription

You can upgrade your subscription at any time. Upgrading your subscription does not require you to cancel your existing subscription.

Your account will be upgraded immediately upon successful payment of the **prorated** amount. Any new license or session you add will **co-term with your existing subscription end date**.

For example, if your subscription ends on **Jan 1, 2026**, and you add licenses in **July 2025**, you'll only pay a **pro-rated amount** for the period from July 2025 to Jan 1, 2026—not for a full year.

<details>
  <summary>Depending on your work requirements, you can:</summary>
  <ul>
    <li>
      Purchase more <a href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-studio-enterprise-per-user-license">Katalon Studio Enterprise per-user license </a> for all users to avoid mixed Katalon Studio and KSE licenses within an Organization.
    </li>
    <li>
      Purchase more <a href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-runtime-engine-floating-license">Katalon Runtime Engine floating license </a> to run more execution sessions on the same machine.
    </li>
    <li>
      Purchase more TestCloud sessions to increase the number of parallel test executions. To learn more about TestCloud sessions, see: <a href="/katalon-platform/administer/katalon-platform-packages/katalon-platform-quotas#testcloud-sessions"> Quotas overview. </a>
    </li>
  </ul>
</details>


1. Go to the [purchase.katalon.com](http://purchase.katalon.com/).
2. Click **Expand your plan**.
3. Choose the plan you want to purchase more sessions or licenses for.
4. Click **Proceed to checkout**. You are redirected to the checkout page.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/expand_plan.png" alt="Purchase page buy more licenses" width="900"/> <br/>

5. Fill in or update the required information for billing and payment method (if needed), then click **Checkout** to complete your purchase.

### Upgrade existing subscription to annual billing
:::warning warning
- You cannot change your annual subscription back to a monthly one.
- You can only subscribe monthly again once your annual subscription has ended.
:::
1. Go to [Purchase - Katalon Studio](http://purchase.katalon.com/). 
2. Click **Expand your plan**. 
3. Turn the toggle to Annual for the subscription you want to upgrade.
3. Review the new plan's price, then click **Proceed to checkout**. You are redirected to the checkout page.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/switch_annual.png" alt="Purchase page buy more licenses" width="900"/> <br/>

4. Update the required information for billing and payment method (if needed), then click of **Checkout** to complete the payment. Successful payment will immediately change your subscription type.
    
    **Note**: We’ll automatically apply a credit for the unused days on your monthly plan toward the annual subscription cost.


</TabItem>
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

In this guide, you'll explore how to manage subscriptions and payments and view license management settings.

## Legacy

### Check the license details of your Organization

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">The following is a guide on how to check the type of licenses your Organization has on Katalon.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">Go to <span className="ph">Katalon TestOps</span> to view the details of your current license. </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">Log in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon TestOps</a> and choose your Account.</span></li><li className="li step"><span className="ph cmd">In the Account admin page, select your Organization. <img className="image" width={800} src={useBaseUrl("/d0466f70-bfef-11ee-ac6d-0242c7a41fd4/KT-Acount-page.png")} alt="Click on the organization which you want to check the license of." /></span></li><li className="li step"><span className="ph cmd">Once you're in the Organization admin page, select the <span className="ph uicontrol">License</span> section on the sidebar to open <span className="ph uicontrol">License Management</span> page. </span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You are now on the <span className="ph uicontrol">License Management</span> page, where active subscriptions for <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-studio-enterprise-per-user-license">Katalon Studio Enterprise (per-user)</a> are shown by default under the <span className="ph uicontrol">Subscription Details</span> section. You can also view your licenses for <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-runtime-engine-floating-license">Katalon Runtime Engine (Floating)</a> and <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-runtime-engine-devops-sunsetting">Katalon Runtime Engine DevOps</a> by clicking on the associated tab.<img className="image" width={700} src={useBaseUrl("/d050f6c0-bfef-11ee-ac6d-0242c7a41fd4/KT-License_Management.png")} alt="The License Management page shows all subscriptions in that organization." /></section> 

<!-- ## <a id="task-gdr2mxxt" class="anchor_top_offset"/>Subscribe to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon TestOps</span>  via <span xmlns="http://www.w3.org/1999/xhtml" className="ph">TestOps</span>  website
### <a id="task-gdr2mxxt" class="anchor_top_offset"/>Subscribe to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon TestOps</span>  via <span xmlns="http://www.w3.org/1999/xhtml" className="ph">TestOps</span>  website

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">Katalon Platform is currently offering two plans. To learn more about Katalon Platform plans and its feature comparison, see: <a className="xref" href="#">Version 8.0.0 - 8.0.1</a>.</p><p className="p">Follow these steps to subscribe to <span className="ph">Katalon TestOps</span> via the <span className="ph">Katalon TestOps</span> website:</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://my.katalon.com/" target="_blank">TestOps Admin</a> and choose your Account.</span></li><li className="li step stepexpand"><span className="ph cmd">In your Account admin page, select <span className="ph uicontrol">Subscriptions</span> section to open <span className="ph uicontrol">Subscription Management</span> page.</span></li><li className="li step stepexpand"><span className="ph cmd">Navigate to <span className="ph uicontrol">Select Platform Tier</span> dropdown menu in the <span className="ph uicontrol">Get more single products</span> section.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/4682ec80-bfe7-11ee-ac6d-0242c7a41fd4/KT-Select_tier.png")} alt="Choose Platform Tier" /></div></li><li className="li step stepexpand"><span className="ph cmd">Choose the test management plan that best aligns with the needs of your organization and select between annual or monthly billing cycle. Then click <span className="ph uicontrol">Checkout</span>.</span><div className="itemgroup info"><p className="p">You can also refer to <span className="ph uicontrol">Katalon Starter Plan</span> - our current Katalon Platform-specific offers, for packages that align with your specific needs at optimal prices.</p></div></li></ol>  -->

<!-- ## <a id="task-q39m18ta" class="anchor_top_offset"/>Purchase Katalon product via <span xmlns="http://www.w3.org/1999/xhtml" className="ph">TestOps</span>   website

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">The following guide shows you how to purchase <span className="ph">Katalon Studio Enterprise (KSE)</span>,  <span className="ph">Katalon Runtime Engine (KRE)</span> licenses, and  <span className="ph">TestCloud</span> sessions.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">Katalon licenses are purchased and managed via the Account level. To learn more about licenses, see: <a className="xref" href="#">Activate a KRE license with Private Instance</a>.</p><p className="p"><a className="xref" href="/katalon-testcloud/testcloud-overview">TestCloud</a> sessions are accessible to all users of an Account once you purchase them. To learn more about <span className="ph">TestCloud</span>, see: <a className="xref" href="/katalon-platform/administer/katalon-platform-packages/testcloud-feature-comparison">TestCloud trial and per Session</a>.</p><p className="p">If you need further assistance with Katalon Pricing and Subscription, contact our sales team via business@katalon.com.</p><div className="note warning note_warning"><span className="note__title">Warning:</span> <ul className="ul"><li className="li"><p className="p">The Owner or Admin of an Organization needs to purchase and assign a paid license to all of their users to avoid mixed <span className="ph">Katalon Studio</span> and <span className="ph">Katalon Studio Enterprise</span> licenses within an organization. For further information,  refer to the <strong className="ph b">Free Offerings</strong> term in <a className="xref j-external-link" href="https://katalon.com/terms#customer-terms-of-use" target="_blank">Terms of Use</a>.</p></li></ul></div>   <p className="p">Follow these steps  to purchase licenses in <span className="ph">TestOps</span>.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://my.katalon.com/" target="_blank">TestOps Admin</a> and select your  Account.</span></li><li className="li step stepexpand"><span className="ph cmd">In your Account admin page, select <span className="ph uicontrol">Subscriptions</span> section to open <span className="ph uicontrol">Subscription Management</span> page.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Get more single products</span> section, navigate to the product you want to purchase.</span><ol type="a" className="ol substeps"><li className="li substep"><span className="ph cmd">Specify the number of licenses or sessions to purchase, and select between annual or monthly billing cycle.</span></li></ol><div className="itemgroup info"><img className="image" width={750} src={useBaseUrl("/1d94d8c0-bce9-11ee-ac6d-0242c7a41fd4/KT-_Purchase_licenses_and_sessions.png")} alt="get more single products section" /></div></li><li className="li step stepexpand"><span className="ph cmd">When you're done, click <span className="ph uicontrol">Checkout</span>. You are redirected to the checkout page.</span></li><li className="li step stepexpand"><span className="ph cmd">Fill in or update the required information for billing and payment method (if needed), then click <span className="ph uicontrol">Check out</span> to complete your purchase.</span><div className="itemgroup info">Billing Information will be display on your receipts.</div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">You purchase is completed.</p><div className="p"><ul className="ul"><li className="li"><p className="p">You need to activate KSE and KRE licenses to start using them. See: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate licenses</a>.</p></li><li className="li"><p className="p">With TestCloud session, you can start scheduling test runs on TestOps. See: <a className="xref" href="#">January 19th 2021</a>.</p></li><li className="li"><p className="p">You can also manage available licenses such as attribute, transfer, and remove granted licenses. Refer to the following topic for more information: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/manage-katalon-licenses">Manage Katalon Licenses</a>.</p></li></ul></div> </section>  -->

### <a id="id_5-hykf5hv4" class="anchor_top_offset"/>Renew Subscription

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Your subscription will automatically renew on the expiry date. If you cancel your subscription before the expiry date, you will not be charged for your next billing cycle and will continue to use the subscription until the end of its expiry date.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to your Account admin page and select the <span className="ph uicontrol">Subscriptions</span> section to open the <span className="ph uicontrol">Subscription Management</span> page. You can check your current subscription(s) details as well as the expiry date as the following screenshot.</p> 
<img xmlns="http://www.w3.org/1999/xhtml" className="image" width={700} src={useBaseUrl("/0df55d90-bce9-11ee-ac6d-0242c7a41fd4/KT-_Subsciption_Management.png")} alt="Subscription Management page" /> 

### Payment Method

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">You must be the Owner or Billing Manager of your Account.</p></li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon offers 2 payment methods to pay your bill:<ul className="ul"><li className="li"><p className="p">Bank Transfer</p></li><li className="li"><p className="p">Credit Card</p></li></ul> </div>

#### Bank transfer payment

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">Only applicable to US customers with a business domain and an annual subscription.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon supports Bank Transfers through both ACH credit transfer and wire transfer. When you place an order using a Bank Transfer payment, you will receive payment instructions including all the required related information for completing the payment.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The payment deadline for any order is set at 7 days from the date of your order placement. Katalon will activate your subscription as soon as the payment is completed. If Katalon does not receive any payment by the end of the 7<sup className="ph sup">th</sup> day, your order will be automatically canceled. If the order is canceled but you still wish to make your purchase, you will have to place your order again.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you pay the renewal fee via Bank Transfer, you will receive <em className="ph i">a reminder email</em> 7 days before the renewal date (or expiry date), providing details about your upcoming renewal with a payment instruction. On the renewal date, if you have not completed your renewal amount, your subscription will expire and be terminated. You then get a confirmation email for the cancellation.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can check the expiry date of your current subscription(s) on the <span className="ph uicontrol">Subscription Management</span> page. See: <a className="xref" href="/katalon-platform/get-started/quick-guide-for-billing-managers#id_5-hykf5hv4">Renew Subscription</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note warning note_warning"><span className="note__title">Warning:</span> <ul className="ul"><li className="li">Payment may take 1-3 business days to reach Katalon's bank account. It must be received by the due date to avoid any order cancellation.</li><li className="li">You can make either a single payment or multiple partial payments within 7 days, but make sure the total sums match the total invoice amount.</li><li className="li">You cannot place a new order until you settle the outstanding balance of your pending payment.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further assistance, please contact our self-serve team via business@katalon.com.</p> 

#### Credit card payment

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon supports Credit Card payment. You can only use one card in each Account for all your subscription purchases, including renewals.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you place an order with a credit card, you will receive a confirmation email once your payment is successful, and Katalon will activate your subscription instantly.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you pay the renewal fee with your Credit Card, you will receive <em className="ph i">a reminder email</em> 7 days before the renewal date (or expiry date), providing details about your upcoming renewal. On the renewal date, your credit card will be charged the renewal fee. In case of a payment failure, the system will offer a 7-day period from the renewal date, you will be notified to update your payment details within this period. Make sure the payment is completed within this 7-day period; otherwise, your subscription will be terminated until a successful payment is made. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following is a guide on how to manage your card information.</p> 
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="task-3789">Update credit card information</h4> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">In <span className="ph">Katalon TestOps</span>, you can only save one card in each organization. If you want to replace your credit card, follow these steps to update your card information.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to the <span className="ph uicontrol">Payment Methods</span> page, click <span className="ph uicontrol">Update</span> found next to your card information.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/120b3eb0-bf80-11ee-ac6d-0242c7a41fd4/KT-_Credit_card_payment_method.png")} alt="Payment methods section" /></div></li><li className="li step stepexpand"><span className="ph cmd">Enter your new credit card information, then click <span className="ph uicontrol">Save</span>.</span><div className="itemgroup info"><img className="image" width={750} src={useBaseUrl("/46b8f0a0-bfe7-11ee-ac6d-0242c7a41fd4/KT-_Edit_card.png")} alt="Payment method page" /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">Your payment method is now updated with new card details. </p><p className="p">The new card is now used by default for all billing purposes, including subscription renewals.</p></section> 
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="task-9420">Delete an existing credit card</h4> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="note warning note_warning"><span className="note__title">Warning:</span> <ul className="ul"><li className="li">You cannot undo this action. Once you delete the card, it is permanently removed from your organization.</li><li className="li">Once you delete the card, Bank Transfer is automatically set as the default payment method.</li></ul></div><p className="p">Follow these steps to delete an existing credit card:</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to the <span className="ph uicontrol">Payment Methods</span> page, then click <span className="ph uicontrol">Delete</span> found next to your card information.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/120b3eb0-bf80-11ee-ac6d-0242c7a41fd4/KT-_Credit_card_payment_method.png")} alt="Payment methods section" /></div></li><li className="li step stepexpand"><span className="ph cmd">The <span className="ph uicontrol">Delete card</span> dialog pops up. Click <span className="ph uicontrol">Delete</span> to confirm your action.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have deleted your current credit card permanently.</section> 

</TabItem>
</Tabs>