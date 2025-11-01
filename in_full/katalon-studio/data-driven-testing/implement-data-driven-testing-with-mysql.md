---
hide_title: true
title: Implement data-driven testing with MySQL
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Implement data-driven testing with MySQL

<p xmlns="http://www.w3.org/1999/xhtml" className="p">From <span className="ph">Katalon Studio</span> v8.0.0 onwards, the built-in JDBC driver for MySQL is removed; instead, you can choose to install your preferred version of JDBC driver.</p>


<p xmlns="http://www.w3.org/1999/xhtml" className="p">To keep the MySQL database in use, you need to add its driver to the external library for establishing the database connection. To see which libraries <span className="ph">Katalon Studio</span> supports built-in JDBC drivers, you can refer to this document: <a className="xref" href="/katalon-studio/data-driven-testing/configure-database-connection-for-data-driven-testing-in-katalon-studio">Introduce database connection</a>.</p> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document shows you how to add a driver for MySQL database connection.</p> 

## Add an external JDBC driver for MySQL database connection

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">You already set up MySQL Database.</p></li><li className="li"><p className="p">MySQL Database is running.</p></li></ul></div>

1. Download the MySQL library executable .jar file. You can download from the MySQL website: [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/).

    The version of JDBC driver must be compatible with MySQL version. 

    :::note
    Starting version 10.3.0, Katalon Studio works well with the JDBC driver MySQL from version `mysql-connector-java-6.0.3-bin.jar` to `mysql-connector-j-9.3.0.jar` (latest version).
    :::

2. Go to **Project Settings > Library Management**. Click Add button to add the jar file to the external library.

    <img className="image" width={400} src={useBaseUrl("/0f24a2c0-d900-11ed-ae00-0242cfbc79b5/KS-MYSQL-Add-MySQL-library.png")} />

3. In **Project Settings**, switch to **Database** to configure the database connection.
    1. Select **Secure User and Password** to enable **User** and **Password** fields.
    2. Input the **User** and **Password** used for authentication.
    3. Enter **Connection URL**.
    4. Add **Connection Properties for JDBC Driver** if any (available from version 8.6.5).
    5. Click **Test Connection** to verify whether your database is connected successfully.

        <img className="image" width={600} src={useBaseUrl("/0fdd4460-d900-11ed-ae00-0242cfbc79b5/KS-MYSQL-Connect-MySQL.png")} />

    6. Click **Apply and Close** to complete the connection process.