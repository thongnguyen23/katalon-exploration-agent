---
hide_title: true
title: About TestOps License Types
---

# About TestOps License Types

This document discusses the different types of licenses shown in the License Management page.

## Seat-Based Licenses

The Seat-Based license model is a system where each user is required to have an exclusive, individual license for a product in order to access it. There are two product licenses available:

* TestOps - Full
* Katalon Studio Enterprise
* Katalon Account Manager

The total number of **Available licenses** corresponds to the maximum number of licenses that are unallocated and can be assigned, while the **Purchased number of licenses** corresponds to the total purchased for the Account overall.

For example, if an organization has 10 seat-based licenses for TestOps - Full that have been assigned to specific users, then those 10 users can access TestOps concurrently at any time.

This licensing model ensures that the licensed users always have access to the products they need while providing dedicated access for those specific team members only.

## Session-Based Licenses

The Session-Based license model is a system where each license is allocated based on active sessions rather than individual users. (A session refers to the period during which the software is actively in use.)

There are four product licenses available:

* TestCloud Desktop Browser
* TestCloud Desktop & Mobile Browser
* TestCloud Mobile Native App
* Katalon Runtime Engine

The total amount of **Purchased licenses** corresponds to the maximum number of licenses that can be used concurrently.

For example, if an organization has 10 session-based licenses for TestCloud Desktop Browser, then up to 10 session can be active any time.

This licensing model offers flexibility, allowing users to easily share licenses based on their needs.

## Application Under Test-Based Licenses

The Application Under Test (AUT) Based license model is a system where the number of licenses purchased determines the number of distinct applications that can be tested concurrently. There is one product license available:

* TrueTest

The total number of **Available licenses** corresponds to the maximum number of licenses that are unallocated and can be assigned, while the **Purchased number of licenses** corresponds to the total purchased for the Account overall.

With an AUT-based license, the number of licenses purchased determines the number of distinct applications that can be tested concurrently. For instance, if an organization has 3 AUT-based licenses, it can simultaneously test up to 3 different applications.

This model ensures that your testing resources are efficiently allocated based on the number of applications under test, making it ideal for teams managing multiple projects or products.

## Offline Licenses

An Offline License allows you to use KSE and KRE without an internet connection. Once an offline license is generated, you cannot revoke or transfer it to a different machine.

By default, an offline license expires at the end of your subscription period. It can also be set to expire earlier by inputting a different expiry date when generating the offline license file.

When an offline license expires, you can generate a new offline license file to continue using KSE/KRE offline, or you can switch to using an online license instead.

As a machine ID is required to create an offline license, Katalon generates a machine ID based on the hardware specifications and the user's account logging in to that machine.

For example, if User A logs in to A's account on Machine A, Katalon generates a machine ID X. If User B logs in to B's account on Machine A, Katalon generates a machine ID Y. This means that you need two offline licenses for User A and User B.

**Once converted to an offline license, a KSE/KRE license is bound to a machine until it expires. You cannot undo this action**.

## About Dedicated, Pool, and Available Licenses

This document discusses licensing labels and their meanings.

<img src="/1cf8a203-1f8e-442b-b279-37c161b4ebdf/TO3G1_Dedicated_Pool_Available.png" alt="Dedicated Pool Available Licenses" width="794"/>

Licenses labeled **Dedicated** are those that are exclusively assigned to a specific Account or Organization, which can then distribute them further to sub-Organizations or individual Users.

If purchased licenses are not dedicated, then users within the Account can use them freely.

Licenses labeled **Pool** represents the remaining number of licenses after deducting those dedicated to direct sub-Organizations. (If no licenses are dedicated to sub-Organizations, the Pool equals the number of Dedicated licenses.)

**Available** licenses are those that remain unassigned.
