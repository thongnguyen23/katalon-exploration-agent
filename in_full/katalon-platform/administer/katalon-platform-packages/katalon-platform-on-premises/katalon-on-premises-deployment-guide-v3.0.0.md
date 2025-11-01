---
hide_title: true
title: Katalon On-Premises deployment guide v3.0.0
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Katalon On-Premises deployment guide v3.0.0

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">This guide provides instructions on how to install Katalon On-Premises version 3.0.0, covering both License Server and Katalon Platform options.</p> 

## On-Premises License Server

:::info notes
- The On-Premises License Server only applicable to users with any On-Premises plan.
- The On-Premises License Server only supports Linux.
- Existing On-Premises package users can contact our Sales team at [business@katalon.com](http://business@katalon.com) for information regarding Katalon Studio plan upgrades and data migration.
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Katalon Studio On-Premises License Server allows the installation and activation of Katalon Studio at the client's network location. It is best for users who need to work within a restricted network environment.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are two package plans available:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">License Server only.</p>   </li><li className="li">     <p className="p">License Server with Katalon Platform.</p>   </li></ul> 
To install Katalon Platform On-Premises successfully, ensure your Linux host meets the following general requirements.

## <a id="concept-52ax6ht3" class="anchor_top_offset"/>Prerequisites

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Before deploying Katalon Platform On-Premises, you need to satisfy the following prerequisites:</p> 

### Katalon Platform Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Supported platforms:</strong></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><div className="p">64-bit Linux (x86_64 architecture) distributions:<ul className="ul"><li className="li"><p className="p">Ubuntu</p></li><li className="li"><p className="p">Debian</p></li><li className="li"><p className="p">Red Hat Enterprise Linux (RHEL)</p></li></ul></div></li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Katalon On-Premises has not tested or verified installations on other platforms.</p></li></ul></div></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">General system requirements:</strong></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="concept-52ax6ht3__3a60d1ed-2ce4-41ea-9c11-edd76514f5b9"><caption /><colgroup><col style={{width: '40%'}} /><col style={{width: '60%'}} /></colgroup><tbody className="tbody"><tr className><td className="entry">Operating System</td><td className="entry">64-bit Linux (Debian or CentOS based)</td></tr><tr className><td className="entry">CPU</td><td className="entry">Minimum 4 cores</td></tr><tr className><td className="entry">Memory</td><td className="entry">Minimum 16 GiB</td></tr><tr className><td className="entry">Hard Drive</td><td className="entry">Minimum 100 GiB available hard disk space</td></tr></tbody></table></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Docker and Docker Compose v2 are installed on Katalon Platform server. If Docker and Docker Compose are not available via your Linux server's package manager, refer to the following instructions for manual installation.<ul className="ul"><li className="li"><p className="p">To install Docker for Linux, see Docker's guide here: <a className="xref j-external-link" href="https://docs.docker.com/desktop/install/linux-install/" target="_blank">Install Docker Desktop on Linux</a> or <a className="xref j-external-link" href="https://docs.docker.com/engine/install/" target="_blank">Install Docker Engine</a>.</p></li><li className="li"><p className="p">To install Docker Compose (version 2.20.x or latest) for Linux, see Docker's guide here: <a className="xref j-external-link" href="https://docs.docker.com/compose/install/" target="_blank">Install Docker Compose</a>.</p></li></ul></div>

### User Managed PostgreSQL Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In general, the Katalon On-Premises Platform only supports the PostgreSQL database management system.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">The recommended version of PostgreSQL is 14.3.x</p></li><li className="li"><p className="p">CPU: Minimum 2 cores</p></li><li className="li"><p className="p">Memory: Minimum 8 GiB</p></li><li className="li"><div className="p">A PostgreSQL Database Server to host the platform database instances:<ul className="ul"><li className="li"><p className="p">k1</p></li><li className="li"><p className="p">kit</p></li><li className="li"><p className="p">keycloak</p></li></ul></div></li><li className="li"><p className="p">Enable extension: pg_stat_statements</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following table lists the minimum and recommended values for the configuration parameters:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="concept-52ax6ht3__76fffa39-27ed-49be-959d-f55b866cbac5"><caption /><colgroup><col style={{width: '40%'}} /><col style={{width: '30%'}} /><col style={{width: '30%'}} /></colgroup><tbody className="tbody"><tr className><td className="entry"><strong className="ph b">Parameter</strong></td><td className="entry"><strong className="ph b">Minimum Value</strong></td><td className="entry"><strong className="ph b">Recommended Value</strong></td></tr><tr className><td className="entry">max_connections</td><td className="entry">200</td><td className="entry">400</td></tr><tr className><td className="entry">shared_buffers</td><td className="entry">2 GiB</td><td className="entry">8 GiB</td></tr></tbody></table></div>

### Network Configuration

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To access Katalon Platform On-Premises, configure to open these ports in firewall/security group. Make sure to open these ports (inbound/outbound) in Katalon Platform Server:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">443: HTTPS Port</p></li><li className="li"><p className="p">8000: License Server Port</p></li><li className="li"><p className="p">8080: TestOps Port</p></li><li className="li"><p className="p">8081: Authorizer Port</p></li></ul></div>

### SSL Certificate

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To run the License Server with Katalon Platform with HTTPS, you need to run with three sub-domains that meet:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">A domain for License Server (ex: admin.my-domain.com);</p></li><li className="li"><p className="p">A domain for TestOps (ex: testops.my-domain.com);</p></li><li className="li"><p className="p">A domain for Authorizer (ex: login.my-domain.com); and</p></li><li className="li"><p className="p">SSL Certificate for your domain.</p></li></ul></div>

## Install the Katalon Platform On-Premises License Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following is the complete process of installing and configuring the Katalon Platform On-Premises License Server. Make sure your environment meets all of the system requirements and prerequisites as outlined, see <a className="xref" href="/katalon-platform/administer/katalon-platform-packages/katalon-platform-on-premises/katalon-on-premises-deployment-guide-v3.0.0#concept-52ax6ht3">Prerequisites</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You will learn how to:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Back up your existing databases.</p></li><li className="li"><p className="p">Create and configure the Keycloak database.</p></li><li className="li"><p className="p">Download, configure, and deploy the License Server and TestOps.</p></li><li className="li"><p className="p">Set up TestOps storage.</p></li><li className="li"><p className="p">Configure SSL certificates and update environment variables.</p></li><li className="li"><p className="p">Start the services using Docker Compose. </p></li></ul> 

### Back up the database

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="note warning note_warning"><span className="note__title">Warning:</span> <ul className="ul"><li className="li"><p className="p">This backup step is critical. Ensure all existing databases are backed up before proceeding with the upgrade to avoid potential data loss.</p></li></ul></div></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Stop the existing services.</span><div className="itemgroup info">To stop the Katalon On-Premises version 2.0.x, run the following commands.<div className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">The steps below assume the install directory is <code className="ph codeph">/katalon/katalon-2.0.x</code>. If your install directory differs, substitute your own installation path.</p></li></ul></div></div> <ul className="ul"><li className="li"><div className="p">On a Terminal, navigate to the install directory:<pre className="pre codeblock"><code>cd /katalon/katalon-2.0.x/</code></pre></div></li><li className="li"><div className="p">(If using only the License Server) Enter the following command to stop all containers:<pre className="pre codeblock"><code>docker compose down</code></pre></div></li><li className="li"><div className="p">(If using both License Server and TestOps) Enter the following command to stop all containers:<pre className="pre codeblock"><code>docker compose --profile testops down</code></pre></div></li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Backup PostgreSQL (k1, kit).</span><div className="itemgroup info">You can back up your PostgreSQL database using any of the following methods:<ul className="ul"><li className="li"><p className="p">Method 1: Using <code className="ph codeph">psql</code> prompt. See PostgreSQL documentation: <a className="xref j-external-link" href="https://www.postgresql.org/docs/current/app-psql.html" target="_blank">psql</a>.</p><div className="p">Here's an example of how to back up the <code className="ph codeph">k1</code> and <code className="ph codeph">kit</code> databases using the <code className="ph codeph">psql</code> prompt:<pre className="pre codeblock"><code>pg_dump --file "kit_backup_DATE.sql" --host "&lt;DB_HOST&gt;" --port "&lt;DB_PORT&gt;" --username "&lt;DB_USERNAME&gt;" --format=p --verbose kit{"\n"}pg_dump --file "k1_backup_DATE.sql" --host "&lt;DB_HOST&gt;" --port "&lt;DB_PORT&gt;" --username "&lt;DB_USERNAME&gt;" --format=p --verbose k1{"\n"}</code></pre></div></li><li className="li"><p className="p">Method 2: Via AWS console.</p><ul className="ul"><li className="li"><p className="p">On your AWS console, navigate to the RDS dashboard.</p></li><li className="li"><p className="p">Select your RDS. </p></li><li className="li"><p className="p">Select <span className="ph menucascade"><span className="ph uicontrol">Actions</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Take snapshot</span></span>.</p></li></ul></li><li className="li"><p className="p">Method 3: Using database management tools such as pgAdmin (see <a className="xref j-external-link" href="https://www.pgadmin.org/docs/" target="_blank">pgAdmin documentation</a>), DBeaver (see <a className="xref j-external-link" href="https://dbeaver.com/docs/dbeaver/" target="_blank">DBeaver documentation</a>), etc.</p></li></ul></div></li></ol> 

### Create the Keycloak database

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">In Katalon On-Premises version 3.0.0, a new database named <code className="ph codeph">keycloak</code> is required in addition to the existing <code className="ph codeph">k1</code> and <code className="ph codeph">kit</code> databases.</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Access the PostgreSQL server.</span><div className="itemgroup info">You can access PostgreSQL using one of the following methods:<ul className="ul"><li className="li"><div className="p">Method 1: Using <code className="ph codeph">psql</code> prompt:<pre className="pre codeblock"><code>psql -h &lt;DB_HOST&gt; -U &lt;USER_NAME&gt; -p &lt;DB_PORT&gt;</code></pre></div></li><li className="li"><div className="p">Method 2: Via AWS console.<ul className="ul"><li className="li"><p className="p">On your AWS console, navigate to the RDS dashboard.</p></li><li className="li"><p className="p">Select your RDS. </p></li><li className="li"><p className="p">Select <span className="ph menucascade"><span className="ph uicontrol">Actions</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Take snapshot</span></span>.</p></li></ul></div></li><li className="li"><p className="p">Method 3: Using database management tools such as pgAdmin, DBeaver, etc.</p></li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Create the <code className="ph codeph">keycloak</code> database.</span><div className="itemgroup info">Once connected to PostgreSQL, run the following command to create the <code className="ph codeph">keycloak</code> database:<div className="p"><pre className="pre codeblock"><code>CREATE DATABASE keycloak;{"\n"}</code></pre></div></div></li><li className="li step stepexpand"><span className="ph cmd">Verify the databases.</span><div className="itemgroup info">After creating the <code className="ph codeph">keycloak</code> database, ensure that all three required databases (<code className="ph codeph">k1</code>, <code className="ph codeph">kit</code>, and <code className="ph codeph">keycloak</code>) exist in PostgreSQL by running the following command:<pre className="pre codeblock"><code>\l{"\n"}</code></pre><p className="p">The output should include the three required databases:</p><pre className="pre codeblock"><code>psql (14.12 (Ubuntu 14.12-0ubuntu0.22.04.1)){"\n"}SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off){"\n"}Type "help" for help.{"\n"}{"\n"}postgres=# \l{"\n"}{"                              "}List of databases{"\n"}{"   "}Name{"    "}|{"  "}Owner{"   "}| Encoding | Collate |{"  "}Ctype{"  "}|{"   "}Access privileges{"   "}{"\n"}-----------+----------+----------+---------+---------+-----------------------{"\n"} k1{"        "}| postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | {"\n"} keycloak{"  "}| postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | {"\n"} kit{"       "}| postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | {"\n"} postgres{"  "}| postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | {"\n"} template0 | postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | =c/postgres{"          "}+{"\n"}{"           "}|{"          "}|{"          "}|{"         "}|{"         "}| postgres=CTc/postgres{"\n"} template1 | postgres | UTF8{"     "}| C.UTF-8 | C.UTF-8 | =c/postgres{"          "}+{"\n"}{"           "}|{"          "}|{"          "}|{"         "}|{"         "}| postgres=CTc/postgres{"\n"}(6 rows){"\n"}{"\n"}postgres=# </code></pre></div></li></ol> 

### Download the Katalon On-Premises package and configure

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">After creating the Keycloak database, download and configure the Katalon On-Premises package for version 3.0.0.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">You will receive the On-Premises package from the Katalon Sales team. If you have not yet received the package, contact the team at <a className="xref j-external-link" href="http://business@katalon.com" target="_blank">business@katalon.com</a>.</p></li></ul></div></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Prepare the installation directory.</span><ol type="a" className="ol substeps"><li className="li substep"><span className="ph cmd">Open a Terminal.</span></li><li className="li substep"><span className="ph cmd">Enter the following command to create the installation directory: <code className="ph codeph">mkdir -p /katalon/katalon-3.0.0/</code></span></li><li className="li substep"><span className="ph cmd">Enter the following command to copy the downloaded package to the installation directory: <code className="ph codeph">cp katalon-op-3.0.0.zip  /katalon/katalon-3.0.0/</code></span></li></ol></li><li className="li step stepexpand"><span className="ph cmd">Verify the package.</span><div className="itemgroup info"><div className="p">Run the following command to verify if the package was copied successfully:<pre className="pre codeblock"><code>ls -al</code></pre></div><div className="p">You should see an output similar to this:<pre className="pre codeblock"><code>drwxr-xr-x 3 root root{"       "}4096 Jun{"  "}4 03:43 .{"\n"}drwxr-xr-x 5 root root{"       "}4096 May 30 14:45 ..{"\n"}-rw-r--r-- 1 root root 5008436657 Jun{"  "}3 09:02 katalon-op-3.0.0.zip</code></pre></div></div></li><li className="li step stepexpand"><span className="ph cmd">Unzip the package.</span><div className="itemgroup info"><div className="p">Unzip the package by running the following command:<pre className="pre codeblock"><code>unzip katalon-op-3.0.0.zip</code></pre></div><div className="p">This will create the <code className="ph codeph">katalon-op</code> directory:<pre className="pre codeblock"><code>drwxr-xr-x 3 root root{"       "}4096 Jun{"  "}4 03:43 .{"\n"}drwxr-xr-x 5 root root{"       "}4096 May 30 14:45 ..{"\n"}drwxrwxr-x 3 root root{"       "}4096 Jun{"  "}4 07:56 katalon-op{"\n"}-rw-r--r-- 1 root root 5008436657 Jun{"  "}3 09:02 katalon-op-3.0.0.zip</code></pre></div></div></li><li className="li step stepexpand"><span className="ph cmd">Navigate to the unzipped folder.</span><div className="itemgroup info"><div className="p">Change to the <code className="ph codeph">katalon-op</code> directory and list its contents:<pre className="pre codeblock"><code>cd katalon-op{"\n"}ls -al</code></pre></div><div className="p">You should see a list of files similar to the example below:<pre className="pre codeblock"><code>drwxrwxr-x 3 root root{"       "}4096 Jun{"  "}4 07:56 .{"\n"}drwxr-xr-x 3 root root{"       "}4096 Jun{"  "}4 03:43 ..{"\n"}-rw-rw-r-- 1 root root{"        "}960 Jun{"  "}4 07:56 .env{"\n"}-rw-rw-r-- 1 root root{"       "}1090 Jun{"  "}3 08:59 Build-Info.txt{"\n"}-rw-rw-r-- 1 root root{"       "}6105 Jun{"  "}3 08:44 docker-compose.yml{"\n"}-rw-rw-r-- 1 root root 5033163363 Jun{"  "}3 08:59 images_3.0.0.tar.gz{"\n"}-rw-rw-r-- 1 root root{"       "}1305 Jun{"  "}3 08:44 katalon-op.crt{"\n"}-rw-rw-r-- 1 root root{"       "}1703 Jun{"  "}3 08:44 katalon-op.key{"\n"}drwxr-xr-x 2 root root{"       "}4096 Jun{"  "}4 04:32 logs</code></pre></div></div></li><li className="li step stepexpand"><span className="ph cmd">Load Docker images.</span><div className="itemgroup info">To load the images for version 3.0.0, run the following command:<pre className="pre codeblock"><code>docker load &lt; images_3.0.0.tar.gz</code></pre></div></li><li className="li step stepexpand"><span className="ph cmd">Verify Docker images.</span><div className="itemgroup info"><div className="p">Run the following command to verify if the Docker images were successfully loaded:<pre className="pre codeblock"><code>docker images</code></pre></div><div className="p">You should see a list of Docker images similar to the example below:<pre className="pre codeblock"><code>REPOSITORY{"                       "}TAG{"       "}IMAGE ID{"       "}CREATED{"        "}SIZE{"\n"}katalon-op/testops{"               "}3.0.0{"     "}bc8505e7d8dd{"   "}3 days ago{"     "}422MB{"\n"}katalon-op/license-server{"        "}3.0.0{"     "}5d8fd0ce786e{"   "}3 days ago{"     "}1.03GB{"\n"}katalon-op/keycloak{"              "}3.0.0{"     "}bae44d368348{"   "}3 days ago{"     "}449MB{"\n"}katalon-op/repo-scanner{"          "}3.0.0{"     "}52d01a25eaa4{"   "}6 days ago{"     "}724MB{"\n"}katalon-op/organizing-be{"         "}3.0.0{"     "}fc3d1ddb9185{"   "}8 days ago{"     "}477MB{"\n"}katalon-op/envoy{"                 "}3.0.0{"     "}5c7ce86459f0{"   "}9 days ago{"     "}170MB{"\n"}katalon-op/kafka{"                 "}3.0.0{"     "}577b760f3875{"   "}9 days ago{"     "}551MB{"\n"}katalon-op/authorizer{"            "}3.0.0{"     "}2697d9fc45bd{"   "}11 days ago{"    "}160MB{"\n"}katalon-op/keycloak-config-cli{"   "}3.0.0{"     "}08ea2d10abfd{"   "}13 days ago{"    "}275MB{"\n"}katalon-op/testops-engine{"        "}3.0.0{"     "}d06b7736e9f2{"   "}4 weeks ago{"    "}5.27GB{"\n"}katalon-op/redis{"                 "}3.0.0{"     "}92714677dba2{"   "}2 months ago{"   "}116MB{"\n"}katalon-op/zookeeper{"             "}3.0.0{"     "}b191a95f8d52{"   "}N/A{"            "}510MB</code></pre></div></div></li><li className="li step stepexpand"><span className="ph cmd">Verify image details.</span><div className="itemgroup info"><div className="p">To ensure the image versions match your Katalon On-Premises plan, open the <code className="ph codeph">Build-Info.txt</code> file and compare the <code className="ph codeph">IMAGE ID</code> against the Docker image list above with this command:<pre className="pre codeblock"><code>cat Build-Info.txt</code></pre></div><div className="p">The file should contain the following:<pre className="pre codeblock"><code>KATALON_OP_VERSION: 3.0.0{"\n"}June 3, 2024{"\n"} {"\n"}### IMAGES TAG ###{"\n"}ENVOY: op-a55958afbcab500990aaf6bbaf58dd7ff5b56f97{"\n"}LICENSE_SERVER: op-a3fb4c2d0076902d84abba053e240b6bae6a503b{"\n"}AUTHORIZER: op-9f21f7c53b075ce222e1c2196288113327fa48e2{"\n"}KEYCLOAK: op-b89406c7794b8e30ec4906b8e9f55fd7566b2a5e{"\n"}KEYCLOAK_CONFIG_CLI: op-b11786b85dc318b2a12b612e5fc243e0533487f5{"\n"}REDIS: op-4786e459da28f99f4ade5700b467cc56baf734bd{"\n"}KAFKA: op-f96f1b540295dfbb9597e38837bef566ce2a4f70{"\n"}ZOOKEEPER: op-f3374d97e2245152cec93c0c8c9ad1d49eb5abd7{"\n"}TESTOPS: op-e4c2267e98cbdd770beeefbd6ffb3270d78c6495{"\n"}TESTOPS_ENGINE: op-ba1f17f9f5417ca001854b93b0b3e2fedee2418f{"\n"}ORGANIZING_BE: op-649a471d996ae61ab877abe3b29906aac6c5da75{"\n"}REPO_SCANNER: op-af0e9babeafec19c8309ed3e98469c1632504e65{"\n"} {"\n"}### IMAGES ID ###{"\n"}ENVOY_ID: 5c7ce86459f0{"\n"}LICENSE_SERVER_ID: 5d8fd0ce786e{"\n"}AUTHORIZER_ID: 2697d9fc45bd{"\n"}KEYCLOAK_ID: bae44d368348{"\n"}KEYCLOAK_CONFIG_CLI_ID: 08ea2d10abfd{"\n"}REDIS_ID: 92714677dba2{"\n"}KAFKA_ID: 577b760f3875{"\n"}ZOOKEEPER_ID: b191a95f8d52{"\n"}TESTOPS_ID: bc8505e7d8dd{"\n"}TESTOPS_ENGINE_ID: d06b7736e9f2{"\n"}ORGANIZING_BE_ID: fc3d1ddb9185{"\n"}REPO_SCANNER_ID: 52d01a25eaa4</code></pre></div></div></li></ol> 

### <a id="task-zann512y" class="anchor_top_offset"/>Set up TestOps storage

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To set up your TestOps, you need to create a folder for <code className="ph codeph">TESTOPS_FILE_STORAGE_PATH</code>. In this example, the preferred configuration is <code className="ph codeph">TESTOPS_FILE_STORAGE_PATH=/opt/testops-data</code>. If you choose a different path, replace <code className="ph codeph">/opt/testops-data</code> with your preferred directory.</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Run the following command to create the TestOps storage directory:</span><div className="itemgroup info"><pre className="pre codeblock"><code>mkdir -p /opt/testops-data</code></pre></div></li><li className="li step stepexpand"><span className="ph cmd">Set the correct permission for the directory by running the following command:</span><div className="itemgroup info"><pre className="pre codeblock"><code>chmod 755 /opt/testops-data</code></pre><p className="p">If your storage directory differs, substitute your own path in place of <code className="ph codeph">/opt/testops-data</code>.</p></div></li></ol> 

### Deploy the License Server and TestOps

To start the deployment process for Katalon On-Premises, follow these steps to configure the environment and set up the License Server and TestOps.

1. Navigate to the `katalon-op` directory.Use the following commands to go to the `katalon-op` directory and verify the files:You should see the following files in the directory:
    
    ```
    cd katalon-op
    ls -al
    ```
    You should see the following files in the directory:
    ```
    drwxrwxr-x 3 root root       4096 Jun  4 07:56 .
    drwxr-xr-x 3 root root       4096 Jun  4 03:43 ..
    -rw-rw-r-- 1 root root        960 Jun  4 07:56 .env
    -rw-rw-r-- 1 root root       1090 Jun  3 08:59 Build-Info.txt
    -rw-rw-r-- 1 root root       6105 Jun  3 08:44 docker-compose.yml
    -rw-rw-r-- 1 root root 5033163363 Jun  3 08:59 images_3.0.0.tar.gz
    -rw-rw-r-- 1 root root       1305 Jun  3 08:44 katalon-op.crt
    -rw-rw-r-- 1 root root       1703 Jun  3 08:44 katalon-op.key
    drwxr-xr-x 2 root root       4096 Jun  4 04:32 logs
    ```
    
2. Configure the `.env` file.
    Open the `.env` file and replace the placeholder values with your own information. Ensure you update the following:
    - Database information.
    - Email and password information.
    - TestOps storage path, URLs, domain certificate, and key.
        
        :::info notes
        - Ensure the admin password follows these guidelines:
            - Minimum of 8 characters.
            - Contains at least one uppercase letter, one lowercase letter, one special character, and one number.
            - The password must not start or end with a space.
        :::
    - The `env` file should contain basic and advanced settings for both HTTP and HTTPS scenarios, depending on your deployment. Refer to the following sample script guide to know which values to replace with your configuration:
    - HTTP scenario configuration
        ```
        ### Katalon-OP env

        ########### Basic Settings ###########

        # Database configs
        DB_HOST=host.docker.internal                  <= Replace your own
        DB_PORT=5432                                  <= Replace your own
        DB_USERNAME=postgres                          <= Replace your own
        DB_PASSWORD=admin                             <= Replace your own

        # Admin user configs
        ADMIN_EMAIL=admin@my.domain                   <= Replace your own
        ADMIN_PASSWORD=Admin@123                      <= Replace your own (see note)

        # Auth server configs
        AUTH_SERVER_URL=http://localhost:8082                         <= Replace your own

        # License Server configs
        LICENSE_SERVER_URL=http://localhost:8080                     <= Replace your own

        # TestOps configs (optional if testops profile is not used)
        TESTOPS_SERVER_URL=http://localhost:8081                        <= Replace your own
        TESTOPS_FILE_STORAGE_PATH=/opt/testops-data                     <= Replace your own

        ########### Advanced Settings ###########

        # HTTP config
        HTTP_PORT_1=8080              <= If apply HTTP, can adjust with your port or leave it by default
        HTTP_PORT_2=8081              <= If apply HTTP, can adjust with your port or leave it by default
        HTTP_PORT_3=8082              <= If apply HTTP, can adjust with your port or leave it by default

        # HTTPS configs
        HTTPS_PORT=                    <= Leave it empty by default
        CERT_PATH=                     <= Leave it empty by default
        KEY_PATH=                      <= Leave it empty by default
        KEY_PASSPHRASE=                <= Leave it empty by default

        # TestOps proxy configs (optional if testops profile is not used)
        PROXY_PROTO=http                      <= Leave it by default
        PROXY_HOST=                           <= If have Proxy, replace your own
        PROXY_PORT=                           <= If have Proxy, replace your own
        PROXY_USERNAME=                       <= If have Proxy, replace your own
        PROXY_PASSWORD=                       <= If have Proxy, replace your own
        PROXY_EXCLUDE_LIST=                   <= If have Proxy, replace your own
        TRUSTED_CA_CERT_PATH=                 <= If have an internal CA, replace your own
        ```
        - **HTTPS scenario configuration**
        ```
        ### Katalon-OP env

        ########### Basic Settings ###########

        # Database configs
        DB_HOST=host.docker.internal                  <= Replace your own
        DB_PORT=5432                                  <= Replace your own
        DB_USERNAME=postgres                          <= Replace your own
        DB_PASSWORD=admin                             <= Replace your own

        # Admin user configs
        ADMIN_EMAIL=admin@my.domain                   <= Replace your own
        ADMIN_PASSWORD=Admin@123                      <= Replace your own (see note)

        # Auth server configs
        AUTH_SERVER_URL=https://login.kata-op.com                     <= Replace your own

        # License Server configs
        LICENSE_SERVER_URL=https://admin.kata-op.com                <= Replace your own

        # TestOps configs (optional if testops profile is not used)
        TESTOPS_SERVER_URL=https://testops.kata-op.com                        <= Replace your own
        TESTOPS_FILE_STORAGE_PATH=/opt/testops-data                           <= Replace your own

        ########### Advanced Settings ###########

        # HTTP config
        HTTP_PORT_1=8080              <= Leave it by default
        HTTP_PORT_2=8081              <= Leave it by default
        HTTP_PORT_3=8082              <= Leave it by default

        # HTTPS configs
        HTTPS_PORT=443                    <= If apply HTTPS, input 443
        CERT_PATH=                        <= Replace your own
        KEY_PATH=                         <= Replace your own
        KEY_PASSPHRASE=                   <= Replace your own if have

        # TestOps proxy configs (optional if testops profile is not used)
        PROXY_PROTO=http                      <= Leave it by default
        PROXY_HOST=                           <= If have Proxy, replace your own
        PROXY_PORT=                           <= If have Proxy, replace your own
        PROXY_USERNAME=                       <= If have Proxy, replace your own
        PROXY_PASSWORD=                       <= If have Proxy, replace your own
        PROXY_EXCLUDE_LIST=                   <= If have Proxy, replace your own
        TRUSTED_CA_CERT_PATH=                 <= If have an internal CA, replace your own
        ```

### Configure SSL certificate FQDNs/URLs

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">If you are running the License Server with Katalon Platform, you must configure three sub-domains, known as Fully Qualified Domain Names (FQDNs). An FQDN is the complete domain name that specifies the exact location of a server or resource on the internet.</p><div className="p">The required sub-domains include:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">admin.kata-op.com</code> (for the License Server)</p></li><li className="li"><p className="p"><code className="ph codeph">testops.kata-op.com</code> (for TestOps)</p></li><li className="li"><p className="p"><code className="ph codeph">login.kata-op.com</code> (for the Authorizer)</p></li></ul></div><p className="p">Katalon recommends using a Wildcard SSL certificate to secure these sub-domains.</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Prepare the SSL certificate and key.</span><div className="itemgroup info"><ul className="ul"><li className="li">Ensure you have the SSL certificate and key files stored in a directory on your server. </li><li className="li"><p className="p">If your certificate and key files are stored in a different directory, replace the paths accordingly.</p></li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Update the <code className="ph codeph">.env</code> file.</span><div className="itemgroup info">The following is an example of how to configure the HTTPS settings in the <code className="ph codeph">.env</code> file, assuming the certificate and key files are located in <code className="ph codeph">/katalon/katalon-3.0.0/</code>:<pre className="pre codeblock"><code># HTTPS config{"\n"}HTTPS_PORT=443{"\n"}CERT_PATH=/katalon/katalon-3.0.0/your-domain.crt{"\n"}KEY_PATH=/katalon/katalon-3.0.0/your-domain.key{"\n"}KEY_PASSPHRASE=</code></pre><p className="p">If the certificate and key are stored elsewhere, substitute your directory path for <code className="ph codeph">/katalon/katalon-3.0.0/</code>.</p></div></li></ol> 

### Run the application with Docker Compose

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To start the Katalon On-Premises application, run the corresponding Docker Compose command depending on your deployment plan.</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Start Katalon On-Premises.</span><ol type="a" className="ol substeps"><li className="li substep substepexpand"><span className="ph cmd">If using only the License Server, enter the following command:</span><div className="itemgroup info"><pre className="pre codeblock"><code>docker compose up -d</code></pre></div></li><li className="li substep substepexpand"><span className="ph cmd">If using both the License Server and TestOps, run this command instead:</span><div className="itemgroup info"><pre className="pre codeblock"><code>docker compose --profile testops up -d</code></pre></div></li></ol></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Once the process starts, you can monitor the containers as they initialize. The startup process may take some time to complete. The application will be ready once all services have started, as shown in the image below:<p className="p"><img className="image" src={useBaseUrl("/d11fd3c2-439e-48f2-b46a-eb9e509d9453/On-Premises-Docker-compose-applying.png")} /></p></section> 
