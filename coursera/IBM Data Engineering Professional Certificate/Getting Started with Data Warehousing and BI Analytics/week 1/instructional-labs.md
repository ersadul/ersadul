<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/SN_web_lightmode.png" width="300">
    <h1>Hands-on Lab: Create Db2 service instance and Get started with the Db2 console</h1>
    <p><strong>Estimated time needed:</strong> 15 minutes</p>
    <p>From now on, the hands-on labs for this course require an environment for working with a relational database. To get you up and running quickly we will do so on the Cloud, so you don't have to worry about downloading or installing anything, rather, simply access your database from your web browser. IBM Cloud provides a large number of Data and Analytics services, including IBM Db2, a next generation SQL database.</p>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/ibmcloud.png" width="140" height="100">
    <h1>Objectives</h1>
    <p>After completing this lab, you will be able to:</p>
    <ul>
      <li>Use IBM cloud account to create and use resources</li>
      <li>Create an instance of a Db2 service</li>
      <li>Locate and explore the Db2 console</li>
    </ul>
    <h2>Pre-requisites</h2>
    <p>You will need an IBM Cloud account to do this lab. If you have not created one already, click on this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CC0100EN-SkillsNetwork/labs/IBMCloud_accountCreation/CreateIBMCloudAccount.md.html" target="_blank" rel="external">link</a> and follow the instructions to create an IBM Cloud account.</p>
    <h1>Task 1: Create an instance of IBM Db2 Lite plan</h1>
    <p>Now let us introduce you to Db2 on IBM Cloud. IBM Db2 is a next generation SQL database provisioned for you in the cloud. You can use Db2 on IBM Cloud just as you would use any database software (RDBMS), but without the overhead and expense of hardware setup or software installation and maintenance. Among the service plans offered for Db2 on IBM Cloud is the Lite plan, which is free to use. You can use your database instance to store relational data, analyze data using a built-in SQL editor, or by connecting your own apps.</p>
    <p>Note that IBM Cloud also provides other variants of Db2 such as Db2 Hosted and Db2 Warehouse on Cloud, which is also referred to in this course. However, for the labs in this course, we will utilize the Db2 service since it comes with a Lite plan which is free to use.</p>
    <p>Please follow the steps given below to provision an instance of Db2 on IBM Cloud.</p>
    <ol>
      <li>
        <p>Login to <a href="https://cloud.ibm.com/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">IBM Cloud</a></p>
      </li>
      <li>
        <p>Go to <a href="https://cloud.ibm.com/catalog/services/db2?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">the DB2 Services page on IBM Catalog</a>.</p>
      </li>
      <li>
        <p>Select a location where you want the service to be hosted.</p>
      </li>
    </ol>
    <blockquote>
      <p><strong>Note</strong>: Depending on the Country of your IBM Cloud account, a location to deploy will be pre-selected. For example, if you are in the US, the default region will be Dallas. Users from the UK will see London and so on. Select either <strong>DALLAS</strong> or <strong>LONDON</strong> as the location. Make sure a <strong>Region</strong> is selected as the location, not a <strong>Data center.</strong></p>
    </blockquote>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Db2Details.jpg" alt="Datacenter location for IBM Cloud accounts.">
    </p>
    <ol start="4">
      <li>
        <p>Scroll down to the Pricing Plans section and select the <strong>Lite plan</strong> (it’s a free plan, and available only in <strong>DALLAS</strong> and <strong>LONDON</strong> at this point of time) or any other plans as required.</p>
      </li>
      <li>
        <p>Then click on the <strong>Create</strong> button towards the lower-right of the page. It will spin for a few seconds (typically less than 30s) and then you should see a Service Created message indicating that your instance of Db2 was created successfully.</p>
      </li>
    </ol>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Instance.jpg" alt="Choose a plan to create an instance.">
    </p>
    <h1>Task 2: Locate and Explore the Db2 console</h1>
    <p>Now that you have created your database instance, you need to know how to get to it, explore the console and start working with it.</p>
    <ul>
      <li><strong>NOTE:</strong> You are not required to compose and run any SQL query on this exercise.</li>
    </ul>
    <ol>
      <li>
        <p>To access your database instance, go to your IBM Cloud Resource List (you may need to log into IBM Cloud in the process) directly at: <a href="https://cloud.ibm.com/resources?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">cloud.ibm.com/resources</a></p>
        <ul>
          <li>
            <p><strong>Alternative</strong>: Go to your IBM Cloud dashboard (you may need to login to IBM Cloud in the process) at: <a href="https://cloud.ibm.com/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">cloud.ibm.com</a> and click <strong>Services</strong>.</p>
            <p>
              <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Services.jpg" alt="Services include the new database instance.">
            </p>
          </li>
        </ul>
      </li>
      <li>
        <p>In the Resource list, expand the <strong>Services</strong> and locate and click on your instance of Db2 you provisioned in exercise 2 (the name typically starts with Db2-xx for example Db2-fk, Db2-50, etc.)</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/ServicesDb2xx.png" alt="image">
        </p>
      </li>
      <li>
        <p>Click on the <strong>Go to UI</strong> button.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Go_to_UI.png" alt="image">
        </p>
      </li>
      <li>
        <p>The Db2 console will open in a new tab in your web browser. Click on the 3-bar menu icon in the top left corner and then click on <strong>RUN SQL</strong>.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Run_SQL.jpg" alt="image">
        </p>
      </li>
      <li>
        <p>On the next screen click on <strong>Create new</strong>.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/RunSQL-Create_new.png" alt="image">
        </p>
      </li>
      <li>
        <p>The SQL editor will open where you can start typing and running queries.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/SQLeditor.png" alt="image">
        </p>
      </li>
      <li>
        <p>The SQL editor has several areas for performing different tasks.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/SQLEditorZones.png" alt="image">
        </p>
      </li>
      <li>
        <p>Click on the <strong>Add New Script +</strong> icon if you want to add a new script for composing queries and then select <strong>Create new</strong>.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/Add_new_Script.PNG" alt="image">
        </p>
      </li>
      <li>
        <p>When you are asked in the upcoming labs, compose the appropriate SQL query for each problem and run by clicking <strong>Run all</strong> .</p>
      </li>
      <li>
        <p>When you will run the script, looking at the Result section of the executed queries you will know whether the SQL statements ran successfully or not.</p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/executed_queries.png" alt="image">
        </p>
      </li>
      <li>
        <p>By clicking the Result section of the executed queries, you can see the query error details or result set to check and ensure the output is what you expected.</p>
        <ul>
          <li><strong>NOTE:</strong> You may find that some results don't appear in the result set pane; in this case, click the highlighted <strong>diagonal arrow (View More)</strong> and it will open the full Result Set window containing the results.</li>
        </ul>
        <p></p>
        <p>
          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/images/executed_queries_resultset.png" alt="image">
        </p>
      </li>
    </ol>
    <h1>Summary</h1>
    <p>You can now find your way into and around the database instance, and you will use these skills in later labs.</p>
    <h3>Congratulations! You have completed this lab, and you are ready for the next topic.</h3>
    <h3></h3>
    <h1>Author(s)</h1>
    <ul>
      <li><a href="https://www.linkedin.com/in/ravahuja/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">Rav Ahuja</a></li>
      <li><a href="https://www.linkedin.com/in/sandipsahajoy/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">Sandip Saha Joy</a></li>
    </ul>
    <h1>Other Contributor(s)</h1>
    <ul>
      <li></li>
    </ul>
    <h1>Changelog</h1>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Version</th>
          <th>Changed by</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>23-08-2022</td>
          <td>2.5</td>
          <td>Appalabhaktula Hema</td>
          <td>Updated instructions</td>
        </tr>
        <tr>
          <td>11-05-2022</td>
          <td>2.4</td>
          <td>Hema</td>
          <td>Updated instruction</td>
        </tr>
        <tr>
          <td>28-04-2022</td>
          <td>2.3</td>
          <td>Hema</td>
          <td>Updated screenshots</td>
        </tr>
        <tr>
          <td>08-07-2021</td>
          <td>2.2</td>
          <td>Malika</td>
          <td>Updated screenshots</td>
        </tr>
        <tr>
          <td>23-12-2020</td>
          <td>2.1</td>
          <td>Steve Ryan</td>
          <td>ID Review</td>
        </tr>
        <tr>
          <td>07-12-2020</td>
          <td>2.0</td>
          <td>Sandip Saha Joy</td>
          <td>Created revised version from DB0201EN</td>
        </tr>
        <tr>
          <td>06-03-2020</td>
          <td>1.0</td>
          <td>Rav Ahuja</td>
          <td>Created initial version</td>
        </tr>
      </tbody>
    </table>
    <h2></h2>
    <h3 align="center">© IBM Corporation 2020. All rights reserved.</h3>
    <h3></h3>
    <script>window.addEventListener('load', function() {
snFaculty.inject();
});</script>
    <script src="https://skills-network-assets.s3.us.cloud-object-storage.appdomain.cloud/scripts/inject.43989f87.js"></script>
    <script src="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/highlight.min.js"></script>
    <script src="https://unpkg.com/highlightjs-badge@0.1.9/highlightjs-badge.min.js"></script>
  </body>
</html>
