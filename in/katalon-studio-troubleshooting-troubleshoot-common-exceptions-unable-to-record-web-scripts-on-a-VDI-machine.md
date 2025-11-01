---
hide_title: true
title: Unable to record web scripts on a VDI machine
---

# <a id="troubleshooting-2968" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to record web scripts on a VDI machine

On a virtual desktop infrastructure (VDI) machine, you may not be able to record web scripts using Chrome or Edge Chromium browsers. When attempting to do so, you may encounter errors such as:

```
C:\Users\<username>\.katalon\packages\<KSE Version>\jre\bin>javaw -version
This program is blocked by group policy. For more information, contact your system administrator.
```

```
We couldn't load the extension from: C:\Program Files\Katalon\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Edge Chromium\Object Spy\KR. Loading of unpacked extensions is disabled by the administrator.
```

## Cause

- **Blocked Java executables**: The built-in Java package required by Katalon Studio is restricted by group policy.
- **Unpacked browser extensions disabled**: System policies prevent loading unpacked extensions for Chrome and Edge Chromium browsers.

## Remedy

To ensure Katalon Studio works correctly, your system must meet the following requirements:

### 1. Security configurations

Katalon Studio and Katalon Runtime Engine expect the following security-related configurations to be supported by the operating system:

- **Antivirus and security software**: Ensure software such as McAfee, Bitdefender, or Microsoft Defender does not block necessary executables or processes.
- **OS security features**: Configure built-in features like SmartScreen, AppLocker, or similar tools to allow required files and network communications.

### 2. File execution whitelist

**Java executables**

Whitelist the Java executables used by Katalon Studio. Ensure the following path is allowed:

```
C:\Users\<username>\.katalon\packages\<Katalon Folder>\jre\bin
```

**Browser extensions**

Whitelist the unpacked extensions required for Chrome and Edge Chromium browsers. Example paths include:

```
C:\Users\<user folder>\.katalon\packages\Katalon Studio Installation Folder\configuration\resources\extensions
```

Example extension paths:

- Smart Locator:
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Smart Locator
  ```
- Chrome extensions:
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Chrome\Smart Wait
  ```
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Chrome\Object Spy
  ```
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Chrome\Recorder
  ```
- Edge Chromium extensions:
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Edge Chromium\Smart Wait
  ```
  ```
  C:\Program Files\Katalon_Studio_Windows_64-<version>\configuration\resources\extensions\Edge Chromium\Object Spy
  ```

### 3. Port and network requirements

**Listening ports**

Katalon Studio requires one random TCP port to be open for internal communication. Ensure your system’s policies allow listening on such ports using HTTP protocol (plain text).

**Network protocols**

Allowlist necessary domains and IPs. For detailed requirements, refer to the [Katalon domain and IP whitelist](/katalon-platform/troubleshooting/troubleshooting-common-administrative-issues/katalon-domain-and-ip-whitelist).

