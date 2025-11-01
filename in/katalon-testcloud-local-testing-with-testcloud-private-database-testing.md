---
title: Private database testing with TestCloud tunnel
---
:::note
- The following method applies only when running tests from TestOps. If you're running tests locally using Katalon Studio Enterprise in TestCloud environments, you do not need to use TestCloud Tunnel. Simply connect to your database directly using its actual host and port, as the test is executed from your own machine, which already has access to your internal network.
:::

## Introduction
In data-driven testing, you might need to connect to private resources (e.g., databases, SSH services, internal APIs) and run tests in TestCloud. However, due to network restrictions, TestCloud environments cannot access these resources.

Port forwarding allows you to securely forward network traffic from a local port to a remote private service. When enabled, TestCloud Tunnel automatically opens specified local ports and redirects traffic to the designated private resources within your network. You can then access private resources through these local ports in your test scripts.

#### How it works
- The Tunnel Client opens local ports on the TestCloud test node.
- Traffic sent to these local ports is automatically forwarded through the tunnel to the defined private destination addresses.
- This enables TestCloud test nodes to securely access internal resources via forwarded connections.

This guide walks you through setting up **Port Forwarding Rules** with TestCloud Tunnel to securely access your private resources from your local machine.

:::caution Requirements
- You have configured TestCloud tunnel. This step is required to generate a `tunnelconfig`, which allows you to establish connection to the private database. Follow this guide: [Configure TestCloud tunnel in TestOps](/katalon-testcloud/local-testing-with-testcloud/local-testing-with-testcloud-in-testops).
- After copying the command from the **Generate Configuration** section and opening your Terminal or Command Prompt, follow the remaining instructions to connect to private databases using TestCloud Tunnel on TestOps.
:::


## Configure forwarding rules

:::caution Forwarding Rule Requirements
To ensure secure and valid forwarding, each port forwarding rule must meet the following requirements:
- Each rule must follow the format: `testcloud_local_port:destination_host:destination_port`.
- TestCloud local port must be in the range: `50000` to `60000`.
- The rules must not have duplicate source ports (the local port is unique within the rules collection).
- `RULE_NAME` must contain only alphabetic characters, and cannot contain numbers or special characters. 
- The maximum number of rules allowed per configuration is 5.
:::
There are two options to configure forwarding rules: directly via the CLI (Command-line Interface), or via the `tunnelconfig` file.

### Use the command-line interface
You can configure forwarding rules directly via the CLI, using the following format. This will automatically update your `tunnelconfig` file with the forwarding rules. 
```jsx
kt config --forwarding-mode static \
  --tcp RULE_1=testcloud_local_port_1:destination_host_1:destination_port_1 \
  --tcp RULE_2=testcloud_local_port_2:destination_host_2:destination_port_2
```

- `RULE`: A short name you choose for your tunnel. It helps identify the connection.
- `testcloud_local_port`: A port you choose (between 50000–60000) opened on the Test Node. You’ll connect to this as if your database is running locally.
- `destination_host`: The actual hostname of your private database.
- `destination_port`: The port your database uses (typically, based on the type of DB).

**Example**
```jsx
kt config --server=https://tunnel-manager.katalon.com --api-key=xxxx --username=demo_user@katalon.com --organization-id=123456 --tenant=TestOps --private-tunnel=false --team-id=123456 --forwarding-mode static \
  --tcp QA_BOOKS_DB=50000:qa-books-postgresql.rds.amazonaws.com:5432 \
  --tcp STAGING_BOOKS_DB=50001:staging-books-postgresql.rds.amazonaws.com:5432 \
  --tcp QA_USERS_DB=59999:qa-users-sqlserver.rds.amazonaws.com:1433 \
  --tcp STAGING_USERS_DB=60000:staging-users-sqlserver.rds.amazonaws.com:1433
```

:::tip Run `./kt config --help` to see usage instructions.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/tc-tunnel-config-help-log.png" alt="config command" width="700" />
:::

### Use the tunnelconfig file
After successfully running the command to generate the TestCloud tunnel configuration in the Generate configuration section, a `tunnelconfig` file will be created.
1. Open the `tunnelconfig` file.
2. Add or update the `forwarding_mode` settings to **static**. This will only traffic matching the pre-defined forwarding rules will be allowed. Other requests are rejected.
   ```jsx 
   forwarding_mode = "static"
   ```
3. In the `[tcp]` section, add the forwarding rules.
    ```jsx
    [tcp]
    RULE_1 = "testcloud_local_port_1:destination_host_1:destination_port_1"
    RULE_2 = "testcloud_local_port_2:destination_host_2:destination_port_2"
    ```

- `RULE`: A short name you choose for your tunnel. It helps identify the connection.
- `testcloud_local_port`: A port you choose (between 50000–60000) opened on the Test Node. You’ll connect to this as if your database is running locally.
- `destination_host`: The actual hostname of your private database.
- `destination_port`: The port your database uses (typically, based on the type of DB).

**Example**
```jsx
allow_hosts = []
api_key = 'xxxxx'
group = 'yyyyy'
inactive_tunnel_timeout = 0
organization_id = 1111
private_tunnel = false
proxy_host = ''
proxy_password = ''
proxy_port = ''
proxy_username = ''
relay_protocol = ''
retry = 3
server = 'https://tunnel-manager.katalon.com'
team_id = 1111
tenant = 'TestOps'
username = 'demouser@katalon.com'
forwarding_mode = "static"

[tcp]
QA_BOOKS_DB = "50000:qa-books-postgresql.rds.amazonaws.com:5432"
STAGING_BOOKS_DB = "50001:staging-books-postgresql.rds.amazonaws.com:5432"
QA_USERS_DB = "59999:qa-users-sqlserver.rds.amazonaws.com:1433"
STAGING_USERS_DB = "60000:staging-users-sqlserver.rds.amazonaws.com:1433"
```

## Start the tunnel
Once the configuration is set, simply start the tunnel as usual:

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="windows" label="Windows" default>
    ```jsx 
    kt start 
    ```
  </TabItem>
  <TabItem value="macos" label="macOS">
    ```jsx
    /Applications/kt start 
    ```
  </TabItem>
  <TabItem value="linux" label="Linux">
   ``` jsx
    ./kt start 
    ```
  </TabItem>
</Tabs>

The Tunnel Client will automatically open and forward the specified ports.


## Use forwarded ports in test scripts
For convenience, TestCloud Tunnel exposes each forwarded local port as an environment variable. 

The environment variable for each rule is named as `TUN_<RULE_NAME>`.

You can use this environment variable in your test scripts to connect to the private service without hardcoding any connection details. For example, for the rule `QA_BOOKS_DB = "50000:qa-books-postgresql.rds.amazonaws.com:5432"`, TestCloud Tunnel will automatically set an environment variable named `TUN_QA_BOOKS_DB` on the Test Node.

<details>
 <summary>**Simple example with PostgreSQL**</summary>
    ```jsx 
    import java.sql.Connection
    import java.sql.DriverManager
    import java.sql.ResultSet
    import java.sql.ResultSetMetaData
    import java.sql.Statement

    'Connect to the DB'
    String hostAndPort = System.getenv("TUN_QA_BOOKS_DB") // localhost:50000
    hostAndPort = (hostAndPort == null) ? 'qa-books-postgresql.rds.amazonaws.com:5432': hostAndPort // If you're running tests on your local machine, you don’t need to use TestCloud tunnels. Just connect to your database using its actual host and port directly.
    String dbName = 'books'
    String connUrl =  "jdbc:postgresql://" + hostAndPort + "/" + dbName
    String username = 'mydemouser'
    String password = 'mydemopwd'
    Connection connection = DriverManager.getConnection(connUrl, username, password)

    'Query data from the DB'
    Statement stmt
    ResultSet resultSet
    List<Map<String, Object>> rows = []
    Map<String, Object> row
    try {
        stmt = connection.createStatement()
        resultSet = stmt.executeQuery('select * from books where id = 1  limit 10')
        ResultSetMetaData metaData = resultSet.getMetaData()

        while (resultSet.next()) {
            row = [:]
            for (int i = 1; i <= metaData.columnCount; i++) {
                String columnName = metaData.getColumnName(i)
                Object value = resultSet.getObject(i)
                row[columnName] = value
            }
            rows.add(row)
        }
    } finally {
        try {
            if (resultSet) resultSet.close()
        } catch (Exception ignored) {}
        try {
            if (stmt != null) stmt.close()
        } catch (Exception ignored) {}
    }

    'Verify the data is correct'
    println rows // [[id:1, name:Katalon Testing Book, owner:5, created_at:2025-06-20 13:43:28.890988, updated_at:2025-06-20 13:43:28.890988]]
    WS.verifyEqual(rows[0]['name'], 'Katalon Testing Book')

    'Close the DB connection after use'
    connection.close()
    ```
</details>

#### Result
Once you've finished the setup, enable the **Private testing** toggle to run tests in tunnel mode with TestCloud environment on TestOps.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/private-testing-on testops.png" alt="Private testing on TestOps" width="600" />