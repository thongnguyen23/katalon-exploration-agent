---
title: Configure time zones
---

:::info notes
This feature is only available on macOS and Windows.
:::
In case you want to customize the testing environment to test how your AUT performs in different time zones, you can use the `timezone` capability to configure the time zone on TestCloud real devices and desktop.

1. In Katalon Studio, go to **Project** > **Settings** > **Desired Capabilities** and select **TestCloud**.
2. In the TestCloud settings table, add the `katalon:options` property and set the **Type** as **Dictionary**.
    1. In the **Value** column, add the `timezone` capability with **String** value type, then specify the UTC time. Refer to the [Supported time zones](/katalon-testcloud/advanced-use-cases/configure-time-zones#supported-time-zones) table for details.
   <img width="600" alt="Configure time zone capability" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/tc-configure-time-zone-and-region.png" />
3. Click **OK** and **Apply & Close** to save the settings.
4. Configure your TestCloud environment and run the test.

## Supported time zones

The table below provides the list of supported time zones and their corresponding UTC times.

| Time zone | UTC Time |
| --------- | -------- |
| Pacific/Tongatapu | UTC+13:00 |
| Pacific/Auckland | UTC+12:00 |
| Asia/Vladivostok | UTC+11:00 |
| Australia/Sydney | UTC+10:30 | 
| Asia/Tokyo | UTC+09:00 |
| Asia/Taipei | UTC+08:00 |
| Asia/Hanoi | UTC+07:00 |
| Asia/Yangon | UTC+06:30 | 
| Asia/Almaty | UTC+06:00 |
| Asia/Kathmandu | UTC+05:45 |
| Asia/Mumbai | UTC+05:30 |
| Asia/Oral | UTC+05:00 | 
| Asia/Kabul | UTC+04:30 |
| Europe/Moscow | UTC+04:00 |
| Asia/Kuwait | UTC+03:00 |
| Asia/Beirut | UTC+02:00 | 
| Europe/Prague | UTC+01:00 |
| Etc/GMT | UTC+00:00 |
| Atlantic/Azores | UTC-01:00 |
| America/Cayenne | UTC-03:00 | 
| America/Santiago | UTC-04:00 |
| America/New York | UTC-05:00 | 
| America/Mexico City | UTC-06:00 |
| America/Los Angeles | UTC-08:00 |
| America/Hawaii | UTC-10:00 |
| Niue | UTC-11:00 |  