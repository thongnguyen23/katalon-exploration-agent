---
hide_title: true
title: Handling Databases in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Databases in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">With custom keywords, you can connect to a database as well as perform other data queries. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is a sample demonstrating how to create custom keywords for:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Establishing database connection</li><li className="li">Executing data query</li><li className="li">Closing the connection</li></ul> 

```jsx
private static Connection connection = null;

    /
     * Open and return a connection to database
     * @param dataFile absolute file path  
     * @return an instance of java.sql.Connection
     */
    @Keyword
    def connectDB(String dataFile){
        //Load driver class for your specific database type
        Class.forName("org.sqlite.JDBC")
        String connectionString = "jdbc:sqlite:" + dataFile
        if(connection != null && !connection.isClosed()){
            connection.close()
        }
        connection = DriverManager.getConnection(connectionString)
        return connection
    }

    /
     * execute a SQL query on database
     * @param queryString SQL query string
     * @return a reference to returned data collection, an instance of java.sql.ResultSet
     /
    @Keyword
    def executeQuery(String queryString) {
        Statement stm = connection.createStatement()
        ResultSet rs = stm.executeQuery(queryString)                
        return rs
    }

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
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add the sample code above to your keyword file and modify the details as appropriated. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/handling-databases/image2017-2-24-113A383A14.png")} width={600} /><br /><br /></p> 
