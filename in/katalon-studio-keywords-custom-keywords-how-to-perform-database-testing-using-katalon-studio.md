---
hide_title: true
title: How to perform Database Testing using Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to perform Database Testing using <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio allows users to create <a className="xref" href="/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio">custom keywords</a> to address specific needs. With custom keywords, you can connect to databases and perform database testing. This tutorial describes details on how to create custom keywords for database testing in Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is a code sample demonstrating how to</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">establish a database connection</li><li className="li">execute a query</li><li className="li">close the connection</li></ul> 

```jsx
package com.database
import java.sql.DriverManager
import java.sql.ResultSet
import java.sql.Statement
import com.kms.katalon.core.annotation.Keyword
import com.mysql.jdbc.Connection

public class DemoMySql {
private static Connection connection = null;
 
/ 
* Open and return a connection to database
* @param dataFile absolute file path
* @return an instance of java.sql.Connection
*/
    //Establishing a connection to the DataBase
    
    @Keyword
    def connectDB(String url, String dbname, String port, String username, String password){
        //Load driver class for your specific database type
        String conn = "jdbc:mysql://" + url + ":" + port + "/" + dbname
        
        //Class.forName("org.sqlite.JDBC")
        //String connectionString = "jdbc:sqlite:" + dataFile
        if(connection != null && !connection.isClosed()){
            connection.close()
        }
        connection = DriverManager.getConnection(conn, username, password)
        return connection
    }
    /
    * execute a SQL query on database
    * @param queryString SQL query string
    * @return a reference to returned data collection, an instance of java.sql.ResultSet
    /
    //Executing the constructed Query and Saving results in resultset
    
    @Keyword
    def executeQuery(String queryString) {
        Statement stm = connection.createStatement()
        ResultSet rs = stm.executeQuery(queryString)
        return rs
    }
    
    //Closing the connection
    @Keyword
    def closeDatabaseConnection() {
        if(connection != null && !connection.isClosed()){
            connection.close()
        }
        connection = null 
    }
    /**
    Execute non-query (usually INSERT/UPDATE/DELETE/COUNT/SUM...) on database 
    * @param queryString a SQL statement
    * @return single value result of SQL statement
    */
    
    @Keyword
    def execute(String queryString) {
        Statement stm = connection.createStatement()
        boolean result = stm.execute(queryString)
        return result
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><em className="ph i">Tips: Press "</em><strong className="ph b"><em className="ph i">Ctrl + Shift + o</em></strong><em className="ph i">" to automatically import missing libraries in test scripts.</em></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Custom Keywords file will look like the following:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/connect_db_gui_testing/Test-Explorer_Custom-Keywords.png")} alt="Katalon Custom Keywords" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add the sample code above to your keyword file and modify the details as appropriated. Refer to these links for the formats of database connection strings:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">For MSSQL: <a className="xref j-external-link" href="https://www.connectionstrings.com/sql-server/" target="_blank">https://www.connectionstrings.com/sql-server/</a> </li><li className="li">For Oracle: <a className="xref j-external-link" href="https://www.connectionstrings.com/oracle/" target="_blank">https://www.connectionstrings.com/oracle/</a> </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Use Defined Keywords in Test Cases for DB Testing</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">1. Create new custom keywords for database connection (see above).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">2. Copy the DB script provided above and paste it into the new keyword editor as illustrated below:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/connect_db_gui_testing/DB-Testing.png")} alt="Katalon Defined Keywords" /><br /><br /> </p> 
