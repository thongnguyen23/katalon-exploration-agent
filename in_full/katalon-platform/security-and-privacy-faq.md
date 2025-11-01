---
hide_title: true
title: Security and Privacy FAQ
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="reference-1295" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Security and Privacy FAQ

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">At <span className="ph">Katalon TestOps</span>, we prioritize providing strong security to ensure your information is safe and easily accessible when needed. We uphold a top-tier security program to safeguard your data by aligning with industry-leading practices and frameworks.</p> 

## Does Katalon hold any third-party compliance attestations?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon presently maintains SOC2 Type II certification and aligns with the ISO 27001 standard. Additionally, Katalon is also verified by <a className="xref j-external-link" href="https://gdprlocal.com/" target="_blank">GDPR Local</a> to ensure compliance with GDPR standards.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Moreover, Katalon is also Vendor Insights-certified on AWS Marketplace. For more information about our security profile, refer to the following link: <a className="xref j-external-link" href="https://aws.amazon.com/marketplace/pp/prodview-44cww3pup4ap6" target="_blank">Katalon Platform on AWS</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Our IT security team holds the following certifications:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Certified Information Systems Auditor® (CISA®)</p></li><li className="li"><p className="p">Certified Information Security Manager® (CISM®)</p></li><li className="li"><p className="p">Certified in Risk and Information Systems Control® (CRISC®)</p></li><li className="li"><p className="p">Certified Data Privacy Solutions Engineer™ (CDPSE®)</p></li><li className="li"><p className="p">Certified Information Privacy Professional (CIPP)</p></li><li className="li"><p className="p">Certified in the Governance of Enterprise IT® (CGEIT®)</p></li><li className="li"><p className="p">Certified Information Systems Security Professional® (CISSP®)</p></li><li className="li"><p className="p">Information Systems Security Architecture Professional® (ISSAP®)</p></li><li className="li"><p className="p">Project Management Professional® (PMP®)</p></li><li className="li"><p className="p">Offensive Security Certified Professional </p></li></ul> 

## How does the data flow within Katalon systems?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Customer data is exclusively used on <span className="ph">Katalon TestOps</span>, including <span className="ph">Katalon Runtime Engine (KRE)</span>, <span className="ph">Katalon Studio</span>, <span className="ph">Katalon TestCloud</span>, and <span className="ph">Katalon TestOps</span>, with no other purposes. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Customer data remains active as long as the account is active. Upon voluntary closure, the data enters an "expired" state, and is subsequently transferred to "cold storage" and retained for 365 days. After this duration, both the account and its associated data are permanently removed from our systems.</p> 

## What personally identification information (PII) does Katalon retain?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon retains personal identification information (PII) for user license verification, including name, email, and IP address. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We retain PII solely for the purpose of processing license payments; we do not process or manipulate the data in any other way or for any other purposes.</p> 

## How is user data stored? What encryption is used for data at rest and data in transit?

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Data is stored in approved data stores within AWS. Structured data is stored in databases while unstructured data is stored in securely configured AWS S3 buckets. </p></li><li className="li"><p className="p">Data at rest is encrypted with AES 256-bit encryption, while data transit is encrypted with TLS 1.2+ (RSA 2048-bit) encryption. Approved secure channels include SSH, HTTPS, and SFTP.</p></li><li className="li"><p className="p">Sensitive records are hashed SHA256 at the database table level.</p></li></ul> 

## How are users' passwords stored?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Users' passwords are stored in secure vault compliant with <a className="xref j-external-link" href="https://www.nist.gov/identity-access-management/nist-special-publication-800-63-digital-identity-guidelines" target="_blank">National Institute of Standards and Technology (NIST) Special Publication 800-63 Digital Identity Guidelines</a>.</p> 

## Do you have an enforced password policy for administrator accounts? Do you require MFA for administrator accounts?

All administrator accounts are enforced with company-defined length, complexity, and history requirements for passwords. All admin accounts require multi-factor authentication.

## Can unprotected user data be accessed by your staff? Is this access audited?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Our internal staff is prohibited from directly accessing user data. Only approved database administrators, upon request from the data owner, are granted access to assist them directly. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All access is meticulously logged and subject to regular audits for accountability and security.</p> 

## Is there a separation between publicly accessible parts of the application from the data storage?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Yes. Public-facing components are housed in separate logical networks behind load balancers.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Architecture design follows an n-tier pattern with all data decoupled from external-facing application components.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> There is no direct external access to data stores.</p> 

## Does <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon TestOps</span>  have cloud providers? Where are they hosted?

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> uses Amazon Web Services (AWS) for all production infrastructure and storage. Our AWS location is <code className="ph codeph">us-east-1 region</code> (Northern Virginia, USA). </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you need custom data storage location for your organization or project, <span className="ph">Katalon TestOps</span> offers on-premises and private Software-as-Service (SaaS) solutions. <a className="xref j-external-link" href="https://katalon.com/contact-us#contact-us" target="_blank">Contact us</a> for more information.</p> 

## Do you operate physical infrastructure? 

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> infrastructure is cloud-first and 100% virtualized. None of our infrastructure is physical.</p> 

## Does Katalon have an information security program?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon maintains an internal Information Security Management System based on the ISO 27001 and the <a className="xref j-external-link" href="https://www.nist.gov/itl/smallbusinesscyber/planning-guides/nist-cybersecurity-framework" target="_blank">NIST CyberSecurity Framework</a>. Specifically, it has been assessed and found to conform with ISO/IEC 27001:2022. This program is supervised internally by the Chief Information Security Officer.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All personnel are required to review and provide signed acknowledgement of the policies upon hiring and, at a minimum, annually.</p> 

## Does Katalon hold any third-party compliance attestations?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon currently holds and maintains SOC2 Type II certification. Katalon is also verified by <a className="xref j-external-link" href="https://gdprlocal.com/" target="_blank">GDPR Local</a> to ensure compliance with GDPR standards.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Our IT security team also holds the following certifications:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Certified Information Systems Auditor® (CISA®)</p></li><li className="li"><p className="p">Certified Information Security Manager® (CISM®)</p></li><li className="li"><p className="p">Certified in Risk and Information Systems Control® (CRISC®)</p></li><li className="li"><p className="p">Certified Data Privacy Solutions Engineer™ (CDPSE®)</p></li><li className="li"><p className="p">Certified Information Privacy Professional (CIPP)</p></li><li className="li"><p className="p">Certified in the Governance of Enterprise IT® (CGEIT®)</p></li><li className="li"><p className="p">Certified Information Systems Security Professional® (CISSP®)</p></li><li className="li"><p className="p">Information Systems Security Architecture Professional® (ISSAP®)</p></li><li className="li"><p className="p">Project Management Professional® (PMP®)</p></li><li className="li"><p className="p">Offensive Security Certified Professional </p></li></ul> 

## Do you have a disaster recovery plan (DRP) and business continuity plan (BCP)?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon systems are hosted in AWS, leveraging AWS services for both continuity and redundancy.</p> 
Regular backups and snapshots are taken and tested. Our backup and snapshots are taken daily.
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon systems are designed with high availability being a primary goal. </p> 

## How are backups managed? What encryption is used? How are they destroyed when they are no longer needed?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Automated snapshots and backups are captured and destroyed systematically according to policy. </p> 

## What happens to my data after I stop using Katalon?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Upon a user's request for account deletion or in accordance with our data retention policy, Katalon will delete or return to Customer any Personal Data stored upon request promptly subject to any legal retention obligations, subject to the <a className="xref j-external-link" href="https://katalon.com/terms#customer-terms-of-use" target="_blank">Customer Terms of Use</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This process is conducted using secure deletion methods that prevent data recovery, ensuring the user's information is permanently removed. Additionally, we regularly audit our data disposal practices to comply with global data protection regulations and industry standards, safeguarding our users' privacy rights.</p> 

## What is your system patching process/schedule?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon addresses vulnerabilities by prioritizing them according to their critical degree, aligning with our Vulnerability Management policies. Our focus is on making the best effort to address critical, exploitable vulnerabilities identified in externally accessible assets. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Overall, we adopt an immutable image approach for production patching, implementing patches at the "golden image" level to facilitate swift continuous deployment and remediation for production workloads. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Due to architectural design considerations, patch deployment may follow a rolling fashion.</p> 

## What are some controls you implement for your application security program?

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon adopts the latest practices to ensure secure delivery of <span className="ph">Katalon TestOps</span>: <ul className="ul"><li className="li"><p className="p">AWS Center for Internet Security (CIS) Benchmark for hardening and vulnerability remediation;</p></li><li className="li"><p className="p">Native Intrusion Detection System (IDS) services enabled at the operating system level;</p></li><li className="li"><p className="p">Vulnerability scanning, workload protection and cloud posture monitoring at the infrastructure level handled via Cloud-Native Application Protection Platform (CNAPP), Cloud Workload Protection Platform (CWPP), and Cloud Security Posture Management (CSPM).</p></li></ul> </div>

## Why do I get logged out of Katalon Studio every 7 days?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio uses a Single Sign-On (SSO) system for managing user authentication. The login token issued is valid for 7 days, and subsequent refresh tokens won't extend this period. To maintain continuous access, you'll need to log out and log back in every 7 days. Be mindful of your session duration to prevent interruptions to your testing activities.</p> 

## What port does <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  use to communicate with external resources?

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> is a desktop application and establishes connections with Application Lifecycle Management (ALM) integration servers like JIRA, qTest, Slack, and continuous integration (CI). The security protocols for these connections are configured by the users. Specifically, <span className="ph">Katalon Studio</span> utilizes port 443 for tasks such as updating, checking bugs, and reporting.</p> 

## How are configuration and credential data encrypted in Katalon Studio?

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> App configurations and credential data are encrypted by password-based encryption with Secure Hash Algorithm 1 (SHA1) and Data Encryption Standard in Encrypt-Decrypt-Encrypt multiple encryption mode (PBEWithSHA1AndDESede). </p> 

## What type of encryption does the 'Encrypt Text' tool in Katalon Studio use?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For <span className="ph">Katalon Studio</span>, we use <a className="xref j-external-link" href="https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html" target="_blank">PBEWithSHA1AndDESede</a> algorithm. <span className="ph">Katalon Studio</span> keeps a unique salt and secret key to encrypt and de-crypt values when performing the keyword action. We provide only the encryption feature without the decryption feature. Users can only see the encrypted value in the script file. The raw value will not be logged in our report. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can encrypt text manually by going to <span className="ph">Katalon Studio</span>, <span className="ph menucascade"><span className="ph uicontrol">Help</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Encrypt Text</span></span>:<img className="image" src={useBaseUrl("/95664570-f816-11ed-878a-0242c7a41fd4/KS-_encrypt_text.jpeg")} alt="Katalon Studio encrypt text" />The encrypted value can be used in the following method:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WebUI.setEncryptedText(findTestObject(null), '8SQVv/p9jVTHLrggi8kCzw=='){"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The method is to fill the encrypted text into a text box for the raw value to be decrypted when running the test.</p> 

## Do you have separate production and development environments?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Yes. Each of these environments is separated logically, in their Virtual Private Cloud (VPC) server, and has no dependencies with each other. </p> 

## Are these systems separate from your corporate network?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Yes. Corporate network and Katalon environments are not within the same logical networks.</p> 

## How do you manage access to production systems?

The principle of least privileged access is enforced to define role-based access to our production systems. All production access requires a secure VPN connection to a management network zone. 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">No production environments can be accessible publicly (i.e., all 0.0.0.0/0 subnets are shut down).</p> 
 Also, all production and privileged connections are logged.

## Describe your coding, testing, and deployment practices.

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon employs industry-standard tools and processes to ensure an efficient and secure software delivery lifecycle and CI/CD pipelines.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All development teams follow the Agile methodology with well-defined releases and support cadences.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Code security is reinforced with leading industry tools, enabling static and dynamic code scanning, secured shared secrets, software composition analysis, and vulnerability testing.</p> 

## Do you perform system vulnerability scans and penetration testing?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We employ AWS Inspector and Nessus for vulnerability scanning. Annual penetration testing is done internally and externally.</p> 

## Do you perform web application vulnerability testing or intrusion detection?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We perform the following web application vulnerability testing and intrusion detection:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Application vulnerability scans include static, dynamic, and open source dependencies.</p></li><li className="li"><p className="p">AWS CIS Benchmark is used for hardening and vulnerability remediation.</p></li><li className="li"><p className="p">Native IDS services are enabled at the OS level and vulnerability. </p></li><li className="li"><p className="p">Management and tracking are enabled with Amazon Inspector and Nessus.</p></li></ul> 

## What type of firewalls/DDOS defense do you use?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Native AWS Web Application Firewall (WAF) services are deployed for edge defense.</p> 

## How do you monitor your systems and networks?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">AWS Security Hub, CloudTrail, GuardDuty, Macie, Prowler, and Wazuh are some of the tools and services we deploy for our network and workload monitoring.</p> 

## What logging do systems perform? How are they protected?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">All cloud workload logs are shipped to a central log management platform where security, compliance, vulnerability logs are performed. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Protection is enabled by regular backups and architecture high availability design.</p> 

## How does Katalon manage the physical security setup of the system/service (including overview/architecture drawing)?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Katalon security framework complies with the <strong className="ph b">ISO/IEC 27001 standard</strong> for information security management system (ISMS) and covers physical and environmental security to prevent unauthorized physical access, damage, and interference to the organization's information and information processing facilities. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Refer to the following table regarding Katalon's physical and environmental security setup:<img className="image" src={useBaseUrl("/956d9870-f816-11ed-878a-0242c7a41fd4/ISO_standard__-_physical_and_environmental_securtiy.jpeg")} alt="ISO standard - physical and environmental security" /></p> 

## Log4Shell (CVE-2021-44228) - General update

<p xmlns="http://www.w3.org/1999/xhtml" className="p">On the 9th of December 2021, a Remote Code Execution exploit CVE-2021-44228 was discovered in a popular Java logging library called Log4j2. It became widespread and known to have been exploited in the wild. This incident was created for further investigation and response to fully understand and respond to the potential attacks on Katalon assets. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Based on our internal review, <span className="ph">Katalon TestOps</span> users are not affected by this vulnerability.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> is not affected by this vulnerability. <span className="ph">Katalon TestOps</span> uses the default implementation of Spring Boot (implemented Logback through SLF4J for logging). As <a className="xref j-external-link" href="https://spring.io/blog/2021/12/10/log4j2-vulnerability-and-spring-boot/" target="_blank">noted</a> by the Spring Boot team: "Spring Boot users are only affected by this vulnerability if they have switched the default logging system to Log4J2."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Any vulnerability that might exist in <span className="ph">Katalon TestOps</span> has been mitigated to some extent in its Web Application Firewall (WAF) controls, which have been updated to block requests embedding known attacks on this vulnerability.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As of 13 December 2021, <span className="ph">Katalon TestOps</span> has been upgraded to include Log4J v2.15.0 in its dependencies. In combination with the WAF controls noted above, these corrective actions should completely mitigate any exposure in TestOps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio Enterprise</span> uses Log4J v1.2.15. This version is not as vulnerable as the version identified in the CVE, particularly given that we are not using the JMSAppender. The similar conclusion is drawn for <span className="ph">Katalon Runtime Engine</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For version 8.3.0, you may download it from our GitHub Repo at <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/releases/tag/v8.3.0.beta" target="_blank">https://github.com/katalon-studio/katalon-studio/releases/tag/v8.3.0</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We encourage our users to download and use the suggested versions. During your usage, please do let us know of any feedback that you have with the product version.</p> 

## Does the GPT-powered Manual Test Generator engine employ closed-model AI or open source? Is the data shared or used by any other third party?

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">The GPT-powered <span className="ph">Katalon Manual Test Cases Generator</span> is based on the cloud API of OpenAI. We only send requests to OpenAI and receive responses from their server. No prompt or answer submitted through Katalon products is used by OpenAI to train models. </li><li className="li">Katalon has an agreement with OpenAI to ensure that data submitted for AI processing is not retained by OpenAI. Katalon also does not store prompts and answers submitted through the Manual Test Generator. </li></ul> 

## How does Katalon handle data privacy when using AI services?

Katalon products utilize AI services to improve various features. When AI services are used, we apply strict data privacy measures to protect user data. As per Katalon's contract with OpenAI, none of the submitted data is retained or stored for any purpose. OpenAI does not use customer data to train or improve its models.
