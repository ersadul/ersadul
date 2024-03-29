<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png">
    </center>
    <h1>Hands-on Lab: Populating a Data Warehouse</h1>
    <p>Estimated time needed: <strong>15</strong> minutes</p>
    <h2>Objectives</h2>
    <p>In this lab you will:</p>
    <ul>
      <li>Create an instance of IBM DB2 on cloud</li>
      <li>Create credentials for external accessibility</li>
      <li>Create a db2cli dsn</li>
      <li>Verify a db2cli dsn</li>
      <li>Create the schema on production data warehouse</li>
      <li>Populate the production data warehouse</li>
      <li>Work with db2cli interactive command line</li>
    </ul>
    <h1>About Skills Network Cloud IDE</h1>
    <p>Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. to complete this lab, we will be using the Cloud IDE based on Theia running in a Docker container.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.</p>
    <h1>Exercise 1 - Create an instance of IBM DB2 on cloud</h1>
    <p>We will be using the cloud instance of IBM DB2 as a production data warehouse in this lab.</p>
    <p>If you do not have an instance of IBM DB2 on cloud, follow the instructions in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0260ENSkillsNetwork27338483-2022-01-01" target="_new">lab</a> to create one.</p>
    <h1>Exercise 2 - Create service credentials</h1>
    <p>To access your IBM DB2 cloud instance from external programs, you need service credentials.</p>
    <p>If you do not have service credentials, follow the instructions in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Lab%2008%20-%20Create%20Db2%20Service%20Credentials/instructions.md.html?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0260ENSkillsNetwork27338483-2022-01-01" target="_new">lab</a> to create your service credentials.</p>
    <p>Make a note of the following details:</p>
    <ul>
      <li>user</li>
      <li>password</li>
      <li>host</li>
      <li>port</li>
      <li>database name</li>
    </ul>
    <p>You will need them later in this lab.</p>
    <h1>Exercise 3 - Create a db2cli dsn</h1>
    <p>You can access the IBM DB2 cloud instance using the web browser user interface.</p>
    <p>Using the <code>db2cli</code> you can access your cloud IBM DB2 instance from the command line.</p>
    <p>db2cli can be very helpful in automating data load tasks.</p>
    <p>In this exercise we will be creating a dsn (data source name). A dsn in short is a simple name that refers to a data source.</p>
    <p>Creating a dsn is two step process.</p>
    <p>Step 1: We add the database, host, port and the security mode details. A sample commmand is given for your reference below:</p>
    <p><code>db2cli writecfg add -database dbname -host hostname -port 50001 -parameter "SecurityTransportMode=SSL"</code></p>
    <p>Step 2: We give a name to the data source we just created. This dsn name helps us to easily point to the IBM DB2 instance. A sample commmand is given for your reference below.</p>
    <p><code>db2cli writecfg add -dsn dsn_name -database dbname -host hostname -port 50001</code>​</p>
    <p>Run the commands below on the terminal to create a dsn named <code>production</code>. Make sure you use the database name, host and port details you noted in exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> writecfg add -database BLUDB -host <span class="hljs-number">0</span>c<span class="hljs-number">77</span>d<span class="hljs-number">6</span>f<span class="hljs-number">2</span>-<span class="hljs-number">5</span>da<span class="hljs-number">9</span>-<span class="hljs-number">48</span>a<span class="hljs-number">9</span>-<span class="hljs-number">81</span>f<span class="hljs-number">8</span>-<span class="hljs-number">86</span>b<span class="hljs-number">520</span>b<span class="hljs-number">87518</span>.bs<span class="hljs-number">2</span>io<span class="hljs-number">90</span>l<span class="hljs-number">08</span>kqb<span class="hljs-number">1</span>od<span class="hljs-number">8</span>lcg.databases.appdomain.cloud -port <span class="hljs-number">31198</span> -parameter <span class="hljs-string">"SecurityTransportMode=SSL"</span>

<span class="hljs-attribute">db2cli</span> writecfg add -dsn production -database BLUDB -host <span class="hljs-number">0</span>c<span class="hljs-number">77</span>d<span class="hljs-number">6</span>f<span class="hljs-number">2</span>-<span class="hljs-number">5</span>da<span class="hljs-number">9</span>-<span class="hljs-number">48</span>a<span class="hljs-number">9</span>-<span class="hljs-number">81</span>f<span class="hljs-number">8</span>-<span class="hljs-number">86</span>b<span class="hljs-number">520</span>b<span class="hljs-number">87518</span>.bs<span class="hljs-number">2</span>io<span class="hljs-number">90</span>l<span class="hljs-number">08</span>kqb<span class="hljs-number">1</span>od<span class="hljs-number">8</span>lcg.databases.appdomain.cloud -port <span class="hljs-number">31198</span>

</code></pre>
    <p></p>
    <p>You should see an output similar to the one below.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Populating%20a%20Data%20Warehouse/images/add-dsn.png" alt="Screenshot of codeblock">
    </p>
    <h1>Exercise 4 - Verify a db2cli dsn</h1>
    <p>Now that the dsn is created, we need to verify if it is working, before we go ahead and start using it.</p>
    <p>The generic syntax for the command to verify the dsn is given below:</p>
    <p><code>db2cli validate -dsn alias -connect -user userid -passwd password</code></p>
    <p>Run the command below to verify the <code>production</code> dsn. Make sure you use your username and password that you noted in Exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> validate -dsn production -connect -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span>
</code></pre>
    <p></p>
    <p>You should see an output similar to the one below.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Populating%20a%20Data%20Warehouse/images/dsn-validation.png" alt="Screenshot showing dsn validation">
    </p>
    <p>Your dsn is validated. You can now use it to access the IBM DB2 cloud instance.</p>
    <h1>Exercise 5 - Create the schema on production data warehouse</h1>
    <p>Step 1: Download the schema file.</p>
    <p>Run the command below to download the schema file.</p>
    <pre><code class="hljs language-awk">wget https:<span class="hljs-regexp">//</span>cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud<span class="hljs-regexp">/IBM-DB0260EN-SkillsNetwork/</span>labs<span class="hljs-regexp">/Populating%20a%20Data%20Warehouse/</span>star-schema.sql
</code></pre>
    <p></p>
    <p>Step 2: Create the schema.</p>
    <p>Run the command below to create the schema on the production data warehouse. Make sure you use your username and password that you noted down in Exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span> -inputsql star-schema.sql

</code></pre>
    <p></p>
    <p>The command above tells db2cli to run the commands in the file <code>star-schema.sql</code> on the production data warehouse.</p>
    <h1>Exercise 6 - Populate the production data warehouse</h1>
    <p>Step 1: Download the data files.</p>
    <p>Run the commands below to download the data files.</p>
    <pre><code class="hljs language-awk">wget https:<span class="hljs-regexp">//</span>cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud<span class="hljs-regexp">/IBM-DB0260EN-SkillsNetwork/</span>labs<span class="hljs-regexp">/Populating%20a%20Data%20Warehouse/</span>DimCustomer.sql

wget https:<span class="hljs-regexp">//</span>cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud<span class="hljs-regexp">/IBM-DB0260EN-SkillsNetwork/</span>labs<span class="hljs-regexp">/Populating%20a%20Data%20Warehouse/</span>DimMonth.sql

wget https:<span class="hljs-regexp">//</span>cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud<span class="hljs-regexp">/IBM-DB0260EN-SkillsNetwork/</span>labs<span class="hljs-regexp">/Populating%20a%20Data%20Warehouse/</span>FactBilling.sql

ls *.sql
</code></pre>
    <p></p>
    <p>Step 2: Load the data in the data warehouse.</p>
    <p>Run the commands below to load the data on to the production data warehouse. Make sure you use your username and password that you noted in Exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span> -inputsql DimCustomer.sql
<span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span> -inputsql DimMonth.sql
<span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span> -inputsql FactBilling.sql

</code></pre>
    <p></p>
    <h1>Exercise 7 - Verify the data on the production data warehouse</h1>
    <p>Step 1: Download the verification sql file.</p>
    <p>Run the command below to download the sql file to verify the data.</p>
    <pre><code class="hljs language-awk">wget https:<span class="hljs-regexp">//</span>cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud<span class="hljs-regexp">/IBM-DB0260EN-SkillsNetwork/</span>labs<span class="hljs-regexp">/Populating%20a%20Data%20Warehouse/</span>verify.sql

</code></pre>
    <p></p>
    <p>Step 2: Verify the data in the data warehouse.</p>
    <p>Run the command below to verify the data on the production data warehouse. Make sure you use your username and password that you noted down in Exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span> -inputsql verify.sql

</code></pre>
    <p></p>
    <p>You have successfully loaded the data, if you see an output similar to the one below.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Populating%20a%20Data%20Warehouse/images/verify.png" alt="Screenshot of output">
    </p>
    <h1>Exercise 8 - Work with db2cli interactive command line</h1>
    <p>db2cli can also be used interactively.</p>
    <p>Run the command below to open an interactive sql command shell to your production data warehouse. Make sure you use your username and password that you noted in Exercise 2.</p>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">db2cli</span> execsql -dsn production -user jrg<span class="hljs-number">38634</span> -passwd SuWySBe<span class="hljs-number">5</span>Y<span class="hljs-number">4</span>MsYnh<span class="hljs-number">9</span>

</code></pre>
    <p></p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Populating%20a%20Data%20Warehouse/images/db2-cli-interactive1.png" alt="Screenshot showing data successfully loaded">
    </p>
    <p>Run the command below on the db2cli.</p>
    <pre><code class="hljs language-sql"><span class="hljs-keyword">select</span> <span class="hljs-built_in">count</span>(<span class="hljs-operator">*</span>) <span class="hljs-keyword">from</span> DimMonth;

</code></pre>
    <p></p>
    <p>You should see an output as seen in the image below.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Populating%20a%20Data%20Warehouse/images/db2cli-interactive2.png" alt="Screenshot of output">
    </p>
    <p>You are encouraged to run more sql queries. When done type <code>quit</code> to exit db2cli.</p>
    <h1>Practice exercises</h1>
    <ol>
      <li>Problem:</li>
    </ol>
    <blockquote>
      <p><em>Using the db2cli interactive shell, find the count of rows in the table FactBilling</em></p>
    </blockquote>
    <details>
      <summary>Click here for Hint</summary>
      <blockquote>
        <p>Use the select statement along with count function on the table FactBilling_.</p>
      </blockquote>
    </details>
    <details>
      <summary>Click here for Solution</summary>
      <p>At the db2cli prompt, run the following sql statement:</p>
      <pre><code class="hljs language-sql"><span class="hljs-keyword">select</span> <span class="hljs-built_in">count</span>(<span class="hljs-operator">*</span>) <span class="hljs-keyword">from</span> FactBilling;

</code></pre>
    </details>
    <ol start="2">
      <li>Problem:</li>
    </ol>
    <blockquote>
      <p><em>Using the Cloud UI (not db2cli), create a simple MQT named avg_customer_bill with fields customerid and averagebillamount.</em></p>
    </blockquote>
    <details>
      <summary>Click here for Hint</summary>
      <blockquote>
        <p>use the <code>create table</code> command</p>
      </blockquote>
    </details>
    <details>
      <summary>Click here for Solution</summary>
      <p>Access the UI for DB2, go to the Run SQL screen, in the editor, copy the following command:</p>
      <pre><code class="hljs language-sql_more"><span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">TABLE</span> avg_customer_bill (customerid, averagebillamount) <span class="hljs-keyword">AS</span>
(<span class="hljs-keyword">select</span> customerid, <span class="hljs-keyword">avg</span>(billedamount)
<span class="hljs-keyword">from</span> factbilling
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> customerid
)
     <span class="hljs-keyword">DATA</span> <span class="hljs-keyword">INITIALLY</span> <span class="hljs-keyword">DEFERRED</span>
     <span class="hljs-keyword">REFRESH</span> <span class="hljs-keyword">DEFERRED</span>
     MAINTAINED <span class="hljs-keyword">BY</span> <span class="hljs-keyword">SYSTEM</span>;
</code></pre>
      <p>Clck the 'Run All' Button to run the statement. You should see status as 'Success' on the Result section.</p>
    </details>
    <ol start="3">
      <li>Problem:</li>
    </ol>
    <blockquote>
      <p><em>Refresh the newly created MQT</em></p>
    </blockquote>
    <details>
      <summary>Click here for Hint</summary>
      <blockquote>
        <p>use the <code>refresh table</code> command</p>
      </blockquote>
    </details>
    <details>
      <summary>Click here for Solution</summary>
      <p>At the db2cli prompt, run the following command:</p>
      <pre><code class="hljs language-pgsql"><span class="hljs-keyword">refresh</span> <span class="hljs-keyword">table</span> avg_customer_bill;
</code></pre>
    </details>
    <ol start="4">
      <li>Problem:</li>
    </ol>
    <blockquote>
      <p><em>Using the newly created MQT find the customers whose average billing is more than 11000.</em></p>
    </blockquote>
    <details>
      <summary>Click here for Hint</summary>
      <blockquote>
        <p>use the select statement on the MQT with a where clause on the column averagebillamount</p>
      </blockquote>
    </details>
    <details>
      <summary>Click here for Solution</summary>
      <p>At the db2cli prompt, run the following command:</p>
      <pre><code class="hljs language-axapta"><span class="hljs-keyword">select</span> * <span class="hljs-keyword">from</span> avg_customer_bill <span class="hljs-keyword">where</span> averagebillamount > <span class="hljs-number">11000</span>;
</code></pre>
    </details>
    <p>Congratulations! You have successfully finished the Populating a Data Warehouse lab.</p>
    <h2>Authors</h2>
    <p>Ramesh Sannareddy</p>
    <h3>Other Contributors</h3>
    <p>Rav Ahuja</p>
    <h2>Change Log</h2>
    <table>
      <thead>
        <tr>
          <th>Date (YYYY-MM-DD)</th>
          <th>Version</th>
          <th>Changed By</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2021-09-29</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version of the lab</td>
        </tr>
      </tbody>
    </table>
    <p>Copyright (c) 2021 IBM Corporation. All rights reserved.</p>
    <script>window.addEventListener('load', function() {
snFaculty.inject();
});</script>
    <script src="https://skills-network-assets.s3.us.cloud-object-storage.appdomain.cloud/scripts/inject.43989f87.js"></script>
    <script src="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/highlight.min.js"></script>
    <script src="https://unpkg.com/highlightjs-badge@0.1.9/highlightjs-badge.min.js"></script>
  </body>
</html>
