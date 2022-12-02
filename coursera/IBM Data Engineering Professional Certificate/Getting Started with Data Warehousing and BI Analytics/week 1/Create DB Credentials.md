<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/IDSNlogo.png">
    <h1>Create credentials to access your database instance</h1>
    <h2>Objective(s)</h2>
    <p>At the end of this lab you will be able to:</p>
    <ul>
      <li>Create your own instance of database on IBM Cloud using DB2 service</li>
    </ul>
    <h2>Exercise</h2>
    <p>Database credentials are required to connect from remote applications like Jupyter notebooks which are used in the labs and assignment in the last two weeks of the course.</p>
    <ol start="0">
      <li>Go to your IBM Cloud Resources dashboard (or click on IBM Cloud in the top left corner):</li>
    </ol>
    <p><a href="https://cloud.ibm.com/resources?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork22-2022-01-01" target="_blank" rel="external">https://cloud.ibm.com/resources</a></p>
    <p>Note: you may need to log into IBM Cloud in the process of loading the resources/dashboard.</p>
    <p>If your connection is slow it may take over 30 seconds for the dashboard to fully load.</p>
    <ol>
      <li>Locate and click on your Db2 service listed under Services.</li>
    </ol>
    <p>
      (<strong>NOTE:</strong> In the example below the service is called “Db2-xx” but your Db2 service may have a
      different letters/numbers in the suffix e.g. “Db2-f8”, “Db-50”, etc.)
    </p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/ServicesDb2xx.PNG" alt="image">
    </p>
    <ol start="2">
      <li>Click on Service Credentials in the left menu</li>
    </ol>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/Service_cred.PNG" alt="image">
    </p>
    <ol start="3">
      <li>Click on the button to create <strong>New credential</strong></li>
    </ol>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/New_Cred.PNG" alt="image">
    </p>
    <p>In the prompt that comes up click the “Add” button in the bottom right:</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/Add_Cred_1.PNG" alt="image">
    </p>
    <ol start="4">
      <li>Check the box to <strong>View credentials</strong></li>
      <li>Copy and save the credentials making a note of the following:</li>
    </ol>
    <ul>
      <li><strong>port</strong> is the database port</li>
      <li><strong>db</strong> is the database name</li>
      <li><strong>host</strong> is the hostname of the database instance</li>
      <li><strong>username</strong> is the username you'll use to connect</li>
      <li><strong>password</strong> is the password you'll use to connect</li>
    </ul>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/cred_details.PNG" alt="image">
    </p>
    <p>You need to scroll down to get the credentials details.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/images/details.png" alt="image">
    </p>
    <h2>Author(s)</h2>
    <h4>Rav Ahuja</h4>
    <h4></h4>
    <h3>Other Contributor(s)</h3>
    <p>Simran Garg</p>
    <h2>Changelog</h2>
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
          <td>2021-07-09</td>
          <td>2.1</td>
          <td>Malika</td>
          <td>Updated screenshots</td>
        </tr>
        <tr>
          <td>2020-08-27</td>
          <td>2.0</td>
          <td>Simran</td>
          <td>Migrated lab to course in GitLab</td>
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
