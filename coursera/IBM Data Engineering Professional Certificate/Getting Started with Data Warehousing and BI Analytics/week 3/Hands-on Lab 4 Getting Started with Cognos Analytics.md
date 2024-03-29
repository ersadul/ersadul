<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/IDSNlogo.png" width="200">
    <h1>Hands-on Lab 4: Getting Started with Cognos Analytics</h1>
    <p><strong>Estimated time needed:</strong> 40 minutes</p>
    <p>IBM Cognos Analytics is an AI-fueled business intelligence platform that supports the entire data analytics cycle, from discovery to operationalization. It provides users with data discovery capabilities to visually explore and interact with their data to identify the key insights for improving data driven decisions. Users can perform data discovery and then quickly assemble that information into interactive, visually appealing dashboards; all without the need of formal training.</p>
    <p>In this lab, first you will learn how to sign up for IBM Cognos Analytics trial plan, and learn general navigation around the Cognos Analytics user interface (UI). Next, you will learn how to upload external data files to Cognos Analytics, and then learn how to start a new dashboard with templates. Lastly, you will learn how to create a simple dashboard.</p>
    <h1>Software Used in this Lab</h1>
    <p>Like the videos in the course, for the hands-on labs we will be using IBM Cognos Analytics trial version (currently limited to 90 days) as this is available at no charge.</p>
    <h1>Dataset Used in this Lab</h1>
    <p>The dataset used in this lab comes from the VM designed to showcase IBM Cognos Analytics. This dataset is published by IBM. You can download the dataset file directly from here: <a href="CustomerLoyaltyProgram.csv">CustomerLoyaltyProgram.csv</a></p>
    <h1>Objectives</h1>
    <p>After completing this lab, you will be able to:</p>
    <ul>
      <li>Sign up for a Cognos Analytics trial plan and navigate around the Cognos Analytics user interface.</li>
      <li>Upload external data files to the Cognos Analytics platform.</li>
      <li>Start a new dashboard with dashboard templates.</li>
      <li>Create a simple dashboard.</li>
    </ul>
    <h1>Exercise 1: Sign up for Cognos Analytics Trial Plan</h1>
    <p>In this exercise, you will learn how to sign up for an IBM Cognos Analytics trial plan.</p>
    <ol>
      <li>Go to <a href="https://www.ibm.com/account/reg/us-en/signup?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01&#x26;formid=urx-48178" target="_blank" rel="external">Try IBM Cognos Analytics</a>.</li>
    </ol>
    <blockquote>
      <p>Note- If you use your existing cloud account, you will get only 30 days trial for Cognos Analytics.</p>
    </blockquote>
    <ol start="2">
      <li>
        <p>Fill out section <strong>1. Account information</strong> with your information and click <strong>Next</strong>. The email address you are going to use here, will be called IBMid.<br><ins>If you already have an IBMid, click <strong>Log in</strong>. Enter your IBMid and password.</ins></p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.2.png" width="950">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Fill out section <strong>2. Additional information</strong> with your information. In the case of the Data Center, select one which is nearest to your location. Then click <strong>Next</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.3.png" width="815">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>Now enter the 7 digit code you received on your email address and click <strong>Create account</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.4.png" width="450">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>Click <strong>Proceed</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.5.png" width="450">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>You are now done with the sign up procedure. You will be redirected to <a href="https://myibm.ibm.com/dashboard/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01" target="_blank" rel="external">myibm.ibm.com/dashboard/</a> automatically. Wait for some moment until the Coursera on-line training - Data Visualizations trial offering becomes active.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.6.png" width="836">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>Click on the <strong>Launch</strong> button of this offering.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.7.png" width="400">
      </li>
    </ol><br>
    <p>If it has been more than 72 hours since you initiated your Cognos Trial activation, but its still showing Activation in Progress, please let us know on the forum so we can follow up with the Cognos team on your behalf.</p>
    <p>NOTE: The trial will not be activated for learners in countries under US sanctions.</p>
    <ol start="8">
      <li>
        <p>You have successfully launched the Cognos Analytics platform.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.8.png" width="865">
      </li>
    </ol><br>
    <ol start="9">
      <li>
        <p>From now on, if you want to sign in to the Cognos Analytics platform with your IBMid, go to <a href="https://myibm.ibm.com/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01" target="_blank" rel="external">myibm.ibm.com</a>. Enter your IBMid and password. Repeat step 7 and 8.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/1.9.png" width="512">
      </li>
    </ol><br>
    <h1>Exercise 2: Navigate around Cognos Analytics UI</h1>
    <p>In this exercise, you will learn general navigation around the Cognos Analytics user interface.</p>
    <ol>
      <li>
        <p>The goal of the Cognos Analytics user interface (UI) is to provide you with a streamlined way to get started using Cognos Analytics and view content and activities pertinent to them. You will begin your general navigation here.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/2.A.1.png">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>Click on the <strong>Navigation Bar</strong>, you can use the <strong>Content</strong> to work on different <strong>Samples</strong> The canvas now shows the Recently used files in the <strong>Recent</strong> section, if any, along with the <strong>File drop zone</strong> where you can easily upload your external data files.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/2.A.2.png">
      </li>
    </ol><br>
    <ol start="3">
      <li>Once you begin working with content, the canvas will update with your recently used items. In your Cognos Analytics instance, you may see recent content on the canvas.</li>
    </ol>
    <h1>Exercise 3: Create a Simple Dashboard with Cognos Analytics</h1>
    <p>In this exercise, you will learn how to upload external data files to Cognos Analytics, and then learn how to start a new dashboard with templates. Lastly, you will learn how to create a simple dashboard.</p>
    <h2>Task A: Upload External Data Files</h2>
    <p>In this task, you will learn how to upload external data files to Cognos Analytics.</p>
    <ol>
      <li>
        <p>Download the file <a href="CustomerLoyaltyProgram.csv">CustomerLoyaltyProgram.csv</a>.</p>
      </li>
      <li>
        <p>To sign in to the Cognos Analytics platform with your IBMid, go to <a href="https://myibm.ibm.com/dashboard/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01" target="_blank" rel="external">myibm.ibm.com/dashboard/</a>.</p>
      </li>
      <li>
        <p>Enter your IBMid and password.</p>
      </li>
      <li>
        <p>Scroll down and click <strong>Launch</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.A.1.png" width="400">
      </li>
    </ol><br>
    <ol start="5">
      <li>
        <p>To upload a file, you may either drag and drop this file into the File Drop Zone (highlighted in the image above), or you may click <strong>New > Upload files</strong> at the bottom left corner to navigate to where the file is saved. For this lab, we will use the second option. Click <strong>New > Upload files</strong>, then browse to the file download location, select the CSV file, and click <strong>Open</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.A.2.png">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>As the file uploads, notice that under the <strong>Switcher Menu</strong>, a series of status bars will be visible as the upload process reads and analyzes the data being brought in.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.A.3.png" width="787">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>Once it completes, the status bar will update to show the successful completion before closing.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.A.4.png" width="800">
      </li>
    </ol><br>
    <ol start="8">
      <li>
        <p>In the <strong>Recent</strong> section, you will see the new uploaded data file.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.A.5.png">
      </li>
    </ol><br>
    <h2>Task B: Start a New Dashboard with Templates</h2>
    <p>In this task, you will learn how to start a new dashboard with templates.</p>
    <ol>
      <li>
        <p>Click on the uploaded data file <strong>CustomerLoyaltyProgram.csv</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.B.1.png">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>The Template window will display allowing you to select the type of dashboard and the template style. Select the <strong>tabbed dashboard style</strong>. This will allow you to have multiple pages for your dashboards. Select the <strong>three-panel template</strong>. Click <strong>Create</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.B.2.png" width="916">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>Now you have created a new dashboard using the dashboard template.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.B.3.png" width="1248">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>To save the newly created dashboard, press <strong>CTRL+S</strong>. Select <strong>My content</strong> as <strong>Destination</strong>. On the <strong>Save as:</strong> text field, write "Simple dashboard", and click <strong>Save</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.B.4.png" width="580">
      </li>
    </ol><br>
    <h2>Task C: Create a Simple Dashboard</h2>
    <p>In this task, you will learn how to create a simple dashboard with Cognos Analytics.</p>
    <ol>
      <li>
        <p>As you build the dashboard, the location placement for Widgets in the dashboard template will be referenced using the following Panel numbers.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.1.png" width="533">
      </li>
    </ol><br>
    <ol start="2">
      <li>
        <p>From the <strong>Navigation</strong> panel, select <strong>Sources</strong> to open the data source panel, if it is not already open. The <strong>Data Source</strong> panel displays the uploaded file <strong>“CustomerLoyaltyProgram.csv”</strong> as the Selected Source.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.2.png" width="61">
      </li>
    </ol><br>
    <ol start="3">
      <li>
        <p>From the <strong>Data Source</strong> panel, press <strong>CTRL</strong> and select <strong>Order Year, Quantity Sold, Product Line</strong> and drag it to the center of <strong>Panel 1</strong>, releasing them once you see the <strong>drop zone turn blue</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.3.png" width="833">
      </li>
    </ol><br>
    <ol start="4">
      <li>
        <p>Click on the <strong>Line chart in panel 1</strong> to bring it into focus and render the <strong>on-demand toolbar</strong>.</p>
      </li>
      <li>
        <p>From the on-demand toolbar, select the title and enter the title "Product Line Performance by Year" to the visualization.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.5.png" width="545">
      </li>
    </ol><br>
    <ol start="6">
      <li>
        <p>Highlight the <strong>Title</strong> to open the <strong>Title on-demand toolbar</strong>. From here, you can change the various properties on the title.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.6.png" width="550">
      </li>
    </ol><br>
    <ol start="7">
      <li>
        <p>Click the <strong>Color picker</strong> icon, and change the color to <strong>Red</strong>, then click the font size drop-down and choose <strong>18</strong>.</p>
      </li>
      <li>
        <p>From the <strong>Data Source</strong> panel, select <strong>Quantity Sold</strong> and drag it to the center of <strong>Panel 2</strong>, releasing it once you see the <strong>drop zone turn blue</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.8.png" width="670">
      </li>
    </ol><br>
    <ol start="9">
      <li>
        <p>From the <strong>Data Source</strong> panel, select <strong>Revenue</strong> and drag it to the center of <strong>Panel 3</strong>, releasing it once you see the <strong>drop zone turn blue</strong>.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.9.png" width="931">
      </li>
    </ol><br>
    <ol start="10">
      <li>
        <p>Click on the tab name <strong>Tab 1</strong> to bring up the Tab’s on-demand toolbar. Select the <strong>Edit</strong> icon.</p>
        <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.C.10.png" width="236">
      </li>
    </ol><br>
    <ol start="11">
      <li><strong>Rename</strong> the tab to "A - Product Sales”.</li>
      <li>To save the current work of the dashboard, press <strong>CTRL+S</strong>.</li>
    </ol>
    <h3>Finally, your dashboard "A - Product Sales" should look like below:</h3>
    <h3>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0130EN-SkillsNetwork/Hands-on%20Labs/Lab%204%20-%20Getting%20Started%20with%20Cognos%20Analytics/images/3.png" width="1078">
    </h3><br>
    <h3>Congratulations! You have completed Lab 4, and you are ready for the next topic.</h3>
    <h3></h3>
    <h1>Author(s)</h1>
    <ul>
      <li><a href="https://www.linkedin.com/in/sandipsahajoy/?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01" target="_blank" rel="external">Sandip Saha Joy</a></li>
    </ul>
    <h2>Other Contributor(s)</h2>
    <ul>
      <li><a href="https://www.linkedin.com/in/stevelryan?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0130ENSkillsNetwork20531073-2022-01-01" target="_blank" rel="external">Steve Ryan</a></li>
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
          <td>2022-05-19</td>
          <td>2.4</td>
          <td>Malika Singla</td>
          <td>Updated dataset used</td>
        </tr>
        <tr>
          <td>2022-02-02</td>
          <td>2.3</td>
          <td>Malika Singla</td>
          <td>Updated the screenshots</td>
        </tr>
        <tr>
          <td>2021-07-14</td>
          <td>2.2</td>
          <td>Malika Singla</td>
          <td>Updated trial link</td>
        </tr>
        <tr>
          <td>2021-06-18</td>
          <td>2.1</td>
          <td>Malika Singla</td>
          <td>Updated the screenshot as per new UI</td>
        </tr>
        <tr>
          <td>2021-03-11</td>
          <td>2.0</td>
          <td>Steve Ryan</td>
          <td>Lab rearrangement</td>
        </tr>
        <tr>
          <td>2020-09-23</td>
          <td>1.2</td>
          <td>Steve Ryan</td>
          <td>Post review changes</td>
        </tr>
        <tr>
          <td>2020-09-16</td>
          <td>1.1</td>
          <td>Steve Ryan</td>
          <td>ID review</td>
        </tr>
        <tr>
          <td>2020-09-14</td>
          <td>1.0</td>
          <td>Sandip Saha Joy</td>
          <td>Initial version created</td>
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
