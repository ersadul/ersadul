<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <h1>Final Assignment (Part 2) - Creating Streaming Data Pipelines using Kafka</h1>
    <center>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
    </center>
    <p>Estimated time needed: <strong>45</strong> minutes.</p>
    <h1>About This SN Labs Cloud IDE</h1>
    <p>This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Kafka and MySQL database running in a Docker container. You will also need an instance of DB2 running in IBM Cloud.</p>
    <h2>Important Notice about this lab environment</h2>
    <p>Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in the earlier session will get lost. Please plan to complete these labs in a single session to avoid losing your data.</p>
    <h1>Scenario</h1>
    <p>You are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. As a vehicle passes a toll plaza, the vehicle's data like <code>vehicle_id</code>,<code>vehicle_type</code>,<code>toll_plaza_id</code> and timestamp are streamed to Kafka. Your job is to create a data pipe line that collects the streaming data and loads it into a database.</p>
    <h2>Objectives</h2>
    <p>In this assignment you will create a streaming data pipe by performing these steps:</p>
    <ul>
      <li>Start a MySQL Database server.</li>
      <li>Create a table to hold the toll data.</li>
      <li>Start the Kafka server.</li>
      <li>Install the Kafka python driver.</li>
      <li>Install the MySQL python driver.</li>
      <li>Create a topic named toll in kafka.</li>
      <li>Download streaming data generator program.</li>
      <li>Customize the generator program to steam to toll topic.</li>
      <li>Download and customise streaming data consumer.</li>
      <li>Customize the consumer program to write into a MySQL database table.</li>
      <li>Verify that streamed data is being collected in the database table.</li>
    </ul>
    <h1>Note - Screenshots</h1>
    <p>Throughout this lab you will be prompted to take screenshots and save them on your own device. These screenshots will need to be uploaded for peer review in the next section of the course. You can use various free screengrabbing tools or your operating system's shortcut keys (Alt + PrintScreen in Windows, for example) to capture the required screenshots.</p>
    <h1>Exercise 1 - Prepare the lab environment</h1>
    <p>Before you start the assignment, complete the following steps to set up the lab:</p>
    <ul>
      <li>Step 1: Download Kafka.</li>
    </ul>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">wget</span> https://archive.apache.org/dist/kafka/<span class="hljs-number">2</span>.<span class="hljs-number">8</span>.<span class="hljs-number">0</span>/kafka_<span class="hljs-number">2</span>.<span class="hljs-number">12</span>-<span class="hljs-number">2</span>.<span class="hljs-number">8</span>.<span class="hljs-number">0</span>.tgz

</code></pre>
    <p></p>
    <ul>
      <li>Step 2: Extract Kafka.</li>
    </ul>
    <pre><code class="hljs language-apache"><span class="hljs-attribute">tar</span> -xzf kafka_<span class="hljs-number">2</span>.<span class="hljs-number">12</span>-<span class="hljs-number">2</span>.<span class="hljs-number">8</span>.<span class="hljs-number">0</span>.tgz
</code></pre>
    <p></p>
    <ul>
      <li>Step 3: Start MySQL server.</li>
    </ul>
    <pre><code class="hljs language-ebnf"><span class="hljs-attribute">start_mysql</span>
</code></pre>
    <p></p>
    <ul>
      <li>Step 4: Connect to the mysql server, using the command below. Make sure you use the password given to you when the MySQL server starts. Please make a note or record of the password because you will need it later.</li>
    </ul>
    <pre><code class="hljs language-routeros">mysql <span class="hljs-attribute">--host</span>=127.0.0.1 <span class="hljs-attribute">--port</span>=3306 <span class="hljs-attribute">--user</span>=root <span class="hljs-attribute">--password</span>=Mjk0NDQtcnNhbm5h

</code></pre>
    <p></p>
    <ul>
      <li>Step 5: Create a database named <code>tolldata</code>.</li>
    </ul>
    <p>At the 'mysql>' prompt, run the command below to create the database.</p>
    <pre><code class="hljs language-n1ql"><span class="hljs-keyword">create</span> <span class="hljs-keyword">database</span> tolldata;
</code></pre>
    <p></p>
    <ul>
      <li>Step 6: Create a table named <code>livetolldata</code> with the schema to store the data generated by the traffic simulator.</li>
    </ul>
    <p>Run the following command to create the table:</p>
    <pre><code class="hljs language-sql_more"><span class="hljs-keyword">use</span> tolldata;

<span class="hljs-keyword">create</span> <span class="hljs-keyword">table</span> livetolldata(<span class="hljs-built_in">timestamp</span> datetime,vehicle_id <span class="hljs-built_in">int</span>,vehicle_type <span class="hljs-built_in">char</span>(<span class="hljs-number">15</span>),toll_plaza_id <span class="hljs-built_in">smallint</span>);

</code></pre>
    <p></p>
    <p>This is the table where you would store all the streamed data that comes from kafka. Each row is a record of when a vehicle has passed through a certain toll plaza along with its type and anonymized id.</p>
    <ul>
      <li>Step 7: Disconnect from MySQL server.</li>
    </ul>
    <pre><code class="hljs language-awk"><span class="hljs-keyword">exit</span>
</code></pre>
    <p></p>
    <ul>
      <li>Step 8: Install the python module <code>kafka-python</code> using the pip command.</li>
    </ul>
    <pre><code class="hljs language-vim"><span class="hljs-keyword">python3</span> -<span class="hljs-keyword">m</span> pip install kafka-<span class="hljs-keyword">python</span>
</code></pre>
    <p></p>
    <p>This python module will help you to communicate with kafka server. It can used to send and receive messages from kafka.</p>
    <ul>
      <li>Step 9: Install the python module <code>mysql-connector-python</code> using the pip command.</li>
    </ul>
    <pre><code class="hljs language-vim"><span class="hljs-keyword">python3</span> -<span class="hljs-keyword">m</span> pip install mysql-connector-<span class="hljs-keyword">python</span> 
</code></pre>
    <p></p>
    <p>This python module will help you to interact with mysql server.</p>
    <h1>Exercise 2 - Start Kafka</h1>
    <h3>Task 2.1 - Start Zookeeper</h3>
    <p>Start zookeeper server.</p>
    <p>Take a screenshot of the command you run.</p>
    <p>Name the screenshot <code>start_zookeeper.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.2 - Start Kafka server</h3>
    <p>Start Kafka server</p>
    <p>Take a screenshot of the command you run.</p>
    <p>Name the screenshot <code>start_kafka.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.3 - Create a topic named <code>toll</code></h3>
    <p>Create a Kakfa topic named <code>toll</code></p>
    <p>Take a screenshot of the command you run.</p>
    <p>Name the screenshot <code>create_toll_topic.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.4 - Download the Toll Traffic Simulator</h3>
    <p>Download the <code>toll_traffic_generator.py</code> from the url given below using 'wget'.</p>
    <p><code>https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/toll_traffic_generator.py</code></p>
    <p>Open the code using the theia editor using the "Menu --> File -->Open" option.</p>
    <p>Take a screenshot of the task code.</p>
    <p>Name the screenshot <code>download_simulator.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.5 - Configure the Toll Traffic Simulator</h3>
    <p>Open the <code>toll_traffic_generator.py</code> and set the topic to <code>toll</code>.</p>
    <p>Take a screenshot of the task code with the topic clearly visible.</p>
    <p>Name the screenshot <code>configure_simulator.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.6 - Run the Toll Traffic Simulator</h3>
    <p>Run the <code>toll_traffic_generator.py</code>.</p>
    <p>Hint : <code>python3 &#x3C;pythonfilename></code> runs a python program on the theia lab.</p>
    <p>Take a screenshot of the output of the simulator.</p>
    <p>Name the screenshot <code>simulator_output.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.7 - Configure <code>streaming_data_reader.py</code></h3>
    <p>Download the <code>streaming_data_reader.py</code> from the url below using 'wget'.</p>
    <p><code>https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/streaming_data_reader.py</code></p>
    <p>Open the <code>streaming_data_reader.py</code> and modify the following details so that the program can connect to your mysql server.</p>
    <p><code>TOPIC</code></p>
    <p><code>DATABASE</code></p>
    <p><code>USERNAME</code></p>
    <p><code>PASSWORD</code></p>
    <p>Take a screenshot of the code you modified.</p>
    <p>Name the screenshot <code>streaming_reader_code.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <h3>Task 2.8 - Run <code>streaming_data_reader.py</code></h3>
    <p>Run the <code>streaming_data_reader.py</code></p>
    <p>Take a screenshot of the output of the streaming_data_reader.py.</p>
    <p>Name the screenshot <code>data_reader_output.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <pre><code class="hljs language-vim"><span class="hljs-keyword">python3</span> streaming_data_reader.<span class="hljs-keyword">py</span>
</code></pre>
    <p></p>
    <h3>Task 2.9 - Health check of the streaming data pipeline.</h3>
    <p>If you have done all the steps till here correctly, the streaming toll data would get stored in the table <code>livetolldata</code>.</p>
    <p>List the top 10 rows in the table <code>livetolldata</code>.</p>
    <p>Take a screenshot of the command and the output.</p>
    <p>Name the screenshot <code>output_rows.jpg</code>. (Images can be saved with either the .jpg or .png extension.)</p>
    <p>This concludes the assignment.</p>
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
          <td>2021-08-16</td>
          <td>0.1</td>
          <td>Ramesh Sannareddy</td>
          <td>Created initial version</td>
        </tr>
        <tr>
          <td>2021-12-01</td>
          <td>0.2</td>
          <td>Jeff Grossman</td>
          <td>Added copy code blocks</td>
        </tr>
        <tr>
          <td>2022-09-21</td>
          <td>0.3</td>
          <td>Appalabhaktula Hema</td>
          <td>Updated code blocks</td>
        </tr>
        <tr>
          <td>2022-11-10</td>
          <td>0.4</td>
          <td>Appalabhaktula Hema</td>
          <td>Corrected instructions</td>
        </tr>
        <tr>
          <td>Copyright (c) 2021 IBM Corporation. All rights reserved.</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <script>window.addEventListener('load', function() {
snFaculty.inject();
});</script>
    <script src="https://skills-network-assets.s3.us.cloud-object-storage.appdomain.cloud/scripts/inject.43989f87.js"></script>
    <script src="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/highlight.min.js"></script>
    <script src="https://unpkg.com/highlightjs-badge@0.1.9/highlightjs-badge.min.js"></script>
  </body>
</html>
