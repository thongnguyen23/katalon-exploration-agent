---
title: Local testing with TestCloud
---

This document introduces the concept of TestCloud Tunnel and testing local applications with TestCloud.

If you want to test an application that is hosted locally and not ready public environments, you need to set up a tunnel. A tunnel establishes a connection to secure the movement of data from one network to another.

**TestCloud Tunnel** is designed specifically to enable a secure connection from TestCloud server to local resources so that users can test applications in a restricted environment, avoiding unwanted external access from the global network.

TestCloud Tunnel services can:

- Scale up with team size and work requirements.
- Reduce latency to a minimum by deploying the QUIC technology.
- Prevent overload and crashes when running many tunnel clients.
- Provide security by limiting access to authorized users with API keys.
- Save time by running multiple concurrent tests using multiple Edge servers.

## Key information

The following diagram shows the overview of TestCloud Tunnel solution:

<img src="https://docs.katalon.com/3c183940-0c0e-11ee-bd0e-0242c7a41fd4/TestCloud_Tunnel_Integration_Overview.jpg" alt="TestCloud tunnel integration diagram" width="800" />

The tunnel client program needs to be installed on the user's machine that has access to their private network. After starting, the tunnel client does two things:

- Connect you to the TestCloud Tunnel server.
- Open a tunnel session that is used only for testing.

For each test execution, a separate tunnel session is created. By default, a tunnel session is closed after 30 minutes if there is no request or traffic (i.e. after the tunnel remains idle for 30 minutes).

The tunnel solution uses HTTPS and QUIC protocols. See: [Network configurations](/katalon-testcloud/network-configuration-for-testcloud).

## Configure TestCloud Tunnel

TestCloud Tunnel can be configured with Katalon TestOps or Katalon Studio. See:

- [Local testing with TestCloud in TestOps](/katalon-testcloud/local-testing-with-testcloud/local-testing-with-testcloud-in-testops)
- [Local testing with TestCloud in Katalon Studio](/katalon-testcloud/local-testing-with-testcloud/local-testing-with-testcloud-in-katalon-studio)

The tunnel-sharing feature is available in Katalon Studio and TestOps. The tunnel created in Studio and tunnel created in TestOps can be shared with each other. You can use tunnels from TestOps and Studio interchangeably.

## Debug TestCloud Tunnel

If you have any trouble with the tunnel client connectivity, you can start the client in debug mode with verbose flag:

```jsx
./kt start -vvv
```
With this flag, the client displays logs for troubleshooting.

See also: [Network configuration for TestCloud](/katalon-testcloud/network-configuration-for-testcloud).

## Configure proxy settings

When you configure TestCloud Tunnel with the `/kt config` command, the client produces the `tunnelconfig` file that stores settings information.

If you are running the tunnel client behinds an HTTP/HTTPS proxy, make sure you add the proxy settings to the

```
tunnelconfig
```

file. The required proxy variables are:

- `proxy_host`, `proxy_port`: Proxy address and port, e.g. localhost:9070.
- `proxy_username`, `proxy_password`: Username and password.

```jsx
allow_hosts = []
api_key = "54316023-e777-436a-xxxx-xxxxxxxxxxxx"
group = "0027a725-xxx-4d92-xxx-1e6534d7acd9"
inactive_tunnel_timeout = 0
organization_id = 704xxx
private_tunnel = false
proxy_host = ""
proxy_password = ""
proxy_port = ""
proxy_username = ""
retry = 3
server = "[https://tunnel-manager.katalon.com"{"\n"}team_id](https://tunnel-manager.katalon.com"{"%5Cn"}team_id/) = 644xxx
tenant = "TestOps"
username = "[john.doe@katalon.com](mailto:john.doe@katalon.com)"`
```

## TestCloud Tunnel usage recommendations

We recommend the following practices to optimize your tunnel usage:

- Use a single tunnel or tunnel pool for each test suite or build, then tear it down at the end of your test.
- Launch the tunnel client before the test suite is triggered, then shut the tunnel client down once the test suite is finished.
- Use a machine with stable internet connection and large bandwidth to connect the tunnel client. This is to prevent test failure.
- Use a machine with high specs (e.g., RAM, CPU) when you run many concurrent tests.
- Run one tunnel client on one machine to avoid timeout and bandwidth issues that could cause test failure.
- To save your machine's bandwidth and resources, you can quickly close the tunnel using the shortcut Ctrl+C in the command-line interface (CLI) after you finish running tests.
- Reuse your TestCloud Tunnel configuration in a new machine: In the case that you encounter a test failure and decide to change your machine, first copy the current tunnel configuration to a new machine. Then delete the `client_id` in the command-line interface. You can then run the tests on the new machine.

## Set up TestCloud Tunnel in AWS network

This guide shows an example of configuring network rules for TestCloud Tunnel in the context of AWS.

**AWS environment context**

Assuming you have a VPC that includes:

1. A Public Subnet that has access to an Internet Gateway for internet access (both ingress and egress).
2. A Private Subnet that only has access to internet through a NAT Gateway, that stay in the Public Subnet in #1.
3. The EC2 instance that will be used to deploy TestCloud Tunnel Client stay in the Private Subnet.
4. A strict network configuration with the least open Security Group(s) and NACL(s), i.e. everything (protocol, port, ip address…) is blocked/denied unless specifically allowed. No Security Group and NACL are shared.

**Solution**

You need to whitelist these domains to use TestCloud Tunnel.

- `tunnel-manager.katalon.com:443` (HTTPS)
- `tunnel-proxy-1.katalon.com:2345` (QUIC) or:
- 44.223.117.82:2345
- 107.21.215.109:2345
- 44.222.19.4:2345
- `tunnel-proxy-2.katalon.com:2345` (QUIC) or:
- 3.215.206.237:2345
- 34.197.20.29:2345
- 44.194.125.0:2345

**Security group configuration**

- Security Group Name: TestCloudSG (for example)
- Inbound Rules: Not required
- Outbound Rules:
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 107.21.215.109/32
    ```
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 44.222.19.4/32
    ```
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 44.223.117.82/32
    ```
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 3.215.206.237/32
    ```
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 34.197.20.29/32
    ```
    
    ```jsx
    Type: UDP
    Protocol: UDP
    Port Range: 2345
    Source: 44.194.125.0/32
    ```
    

**NACL configuration**

Inbound Rules:

```jsx
Rule #: 101 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 44.223.117.82/32
Allow/Deny: Allow`
```

```jsx
Rule #: 102 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 107.21.215.109/32
Allow/Deny: Allow`
```

```jsx
Rule #: 103 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 44.222.19.4/32
Allow/Deny: Allow`
```

```jsx
Rule #: 104 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 3.215.206.237/32
Allow/Deny: Allow`
```

```jsx
Rule #: 105 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 34.197.20.29/32
Allow/Deny: Allow`
```

```jsx
Rule #: 106 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 1024-65535
Source: 44.194.125.0/32
Allow/Deny: Allow`
```

Outbound Rules:

```jsx
Rule #: 101 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 44.223.117.82/32
Allow/Deny: Allow`
```

```jsx
Rule #: 102 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 107.21.215.109/32
Allow/Deny: Allow`
```

```jsx 
Rule #: 103 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 44.222.19.4/32
Allow/Deny: Allow`
```

```jsx
Rule #: 104 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 3.215.206.237/32
Allow/Deny: Allow`
```

```jsx
Rule #: 105 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 34.197.20.29/32
Allow/Deny: Allow`
```

```jsx
Rule #: 106 (or next sequential)
Type: Custom UDP Rule
Protocol: UDP (17)
Port Range: 2345
Destination: 44.194.125.0/32
Allow/Deny: Allow`
```

- Place these rules in your NACL in the correct order, typically after any rules that explicitly deny traffic, and before any default deny rules if applicable. This ensures that UDP traffic on port 2345 is permitted as intended.
- When considering inbound rules, it is necessary to enable traffic from your services to return to the node. Since traffic entering the node arrives on a random port within the range of 1024 - 65535, these ports must be opened accordingly.