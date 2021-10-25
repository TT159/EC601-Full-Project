# 601-Project2-phase1(b): Google NLP

This is a NLP test trail. In this project, we try to use the google natural language API to analyize some entities.

## Deploy Google Cloud Platform (GCP)
First we need a account for GCP. We can easily get a google cloud platform account with our google account. Then you can create your first project on GCP.

## Create the first NLP test project
- In the management background interface, select or create a new project. Then you can see the generated project in the project list.

## Enable billing
- Allow bills for the project and set up an account. Click the drop-down menu on the left and click "Billing" (if you don't bind the bank card, you need to bind it first). In this section, we can choose a billing account for our project. And make it at a 'active' status.</br>
After these, we sussessfully create a project.

## Enable API
Here, we need to use the google natural language API so we need to activate this API in our project.

- First, we go back to our project list and click the project you just created, and click "Manage Project". 
- Click "ENABLE APIS AND SERVICES". Enter "Google Cloud Natural Language API" in the search box to search and find the required API. Then, we select the API and double-click, select "Enable" in the opened interface.

## Set up authentication / Create credentials
Any client application that uses the API must be authenticated and granted access to the requested resources. This section describes important authentication concepts and provides steps for setting it up.</br>
There are multiple options for authentication, but it is recommended that you use service accounts for authentication and access control. 
- In the cloud console, we go to the 'Create service account' page and select a project.
- In 'Service account name' field we enter a name. Then we can add a brief description of the account.
- After this, it will automatically generate a email address. You can find it in the Cloud Console. Click the email address for the service account that you created.
- Click 'Keys'. We choose create a new key, then the information of the key will be store in a JSON file and download to your computer.

## Configure local environment variables
Use the service account key file in your environment. This variable only applies to your current shell session, so if you open a new session, set the variable again.
- First method. Computer-->Right click "Properties"-->Advanced System Settings-->New-->GOOGLE_API_KEY:Key_Path
- Second method. For windows, we can use following command in command prompt.
> set GOOGLE_API_KEY=Key_Path.</br>

Replace KEY_PATH with the path of the JSON file that contains your service account key.

## Install and initialize the Cloud SDK
If you plan to use the Natural Language API, you need to install and initialize the Cloud SDK. Cloud SDK is a set of tools that you can use to manage resources and applications hosted on Google Cloud.
Here is the official document you can follow:
> https://cloud.google.com/sdk/docs/install</br>
- After installing the Cloud SDK, we can open the 'Google Cloud SDK Shell' and use the following command to login and test the authentication.
> gcloud auth application-default login </br>
> gcloud auth application-default print-access-token </br>

## Run the test script
Above all, we can download some NLP test python scripts and run them in our computer.
In my project, I test a script which analyzes entities in a string. I upload the code named 'ttstring.py'. Also I upload the result of my test.

# 601-Project2-phase2: Build my own social media analyzer
After learning how to use Twitter API and Google NLP API, I plan to use these two to create a software to analyze the mood of the poster and try to guess the emotion they want to convey in their tweets, whether they are happy, sad or angry. The follwing are some prerequisite questions.
- Define MVP.
- Who is your user?
- What are the basic user story?
- Translate user stories to a modular design.

## MVP
In my perspective, the MVP of social media analyzer is to collect data and analyze data. 
## User
And our user is developer or data scientist who are intreseted in anlaying the emotion of tweets. 
## Basic user story
In addition, I think the basic user story is to collect the tweets of uesers and analyze them. For example, a data scientist can use this software to collect a specific user's tweets and analyze each tweets he/she posted in order to deduce the emotion behind each tweets. In this case, we can track a person’s emotional changes and even draw a graph.
## Modular design 
For modular design, I think it can be composed with several models: input module, authorization and authentication module, storage module, analyse module and output module. First, we need to use Twitter API to collect tweets data as our input and in this step, we need an authorization and authentication module to check the credentials of our users in order to pretect the privacy. Then, we need to store this data. For instance, we can store it in a JSON file or in other forms. After this, it is time to analyze the data and we use Googel NLP API to try to find out the potential emotion conveyed by the tweets. Finally, we conclude a result of the emotion as our output to our users. 

# Completion
Now we try to complete this function with some simple codes. To analyze entity sentiment in a Cloud Storage file, we use Twiiter API and Google NLP API. 
- First, we use Twitter API to collect data and store data in JSON file. This part is completed by CollectData.py
- Then, we use Google NLP API to complete sentiment analysis. Read the data file and analyze it. This part is completed by NlpApi.py 
