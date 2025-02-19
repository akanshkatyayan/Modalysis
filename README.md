# Cloud Computing: MiniProject - Modalysis


<img width="849" alt="image" src="https://user-images.githubusercontent.com/35501313/173912578-756fd220-09e1-47fa-85d3-86379b9ad27b.png">


![](https://img.shields.io/apm/l/vim-mode?color=blue&style=plastic)
![](https://img.shields.io/github/commit-activity/m/antra0497/Modalysis?color=green&style=plastic)
![](https://img.shields.io/github/languages/count/antra0497/Modalysis?color=orange&style=plastic)

Team: 
Akansh Katyayan
Antra Tripathi
Yash Desai
Yashowardhan Rungta
Soumi Chatterjee

## Project Aim:
Creating a Cloud based Flask application using state-of-the-art Machine Learning models to perform classification tasks and text summarisation with a user management system.

## Description:

### Tech Stack

![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)


### Bart Summarization:
> Summarization strategies are typically categorized as extractive, abstractive or mixed. 
>  - Extractive strategies select the top N sentences that best represent the key points of the article. 
>  - Abstractive summaries seek to reproduce the key points of the article in new words.
>  
> Extractive summarization is a challenging NLP task that has only recently become practical by transformer models like BART. It is a denoising autoencoder for pretraining sequence-to-sequence models. BART is trained by 
>  -  corrupting text with an arbitrary noising function, and 
>  -  learning a model to reconstruct the original text. 
>  
>  It uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT)

## Setup: Local Deployment
```
git clone https://github.com/antra0497/Modalysis.git
cd Modalysis
pip install -r requirements.txt
```
Run the Flask server
```
python wsgi.py
```
## Setup: GCP Deployment: https://modalysis-346819.nw.r.appspot.com/

Google App Engine (often referred to as GAE or simply App Engine) is a cloud computing platform as a service for developing and hosting web applications in Google-managed data centers. Applications are sandboxed and run across multiple servers. It offers automatic scaling for web applications—as the number of requests increases for an application and automatically allocates more resources for the web application to handle the additional demand.


**Steps:**
 - Created a VM instance on Google cloud Platfom
 - Created a Project named: Modalysis
 - Enable Cloud Engine API
 - App Engine:
    -  Create a new application
    -  Select location : europe-west2
 -  Source repository:
    -  Add repo: connect external repo
    -  Authenticate from github repo
    -  Changed the gcloud config for timeout :  ```gcloud config set app/cloud_build_timeout 5000```
    -  Deployed App: ```gcloud app deploy```

![image](https://user-images.githubusercontent.com/25953832/162655775-a92576cc-dbf0-4ba5-a82b-1fb6c45dd5a1.png)

## Setup: HerokuApp : https://modalysis.herokuapp.com/

Heroku is a container-based cloud Platform as a Service (PaaS) for several languages. Applications that are run on Heroku typically have a unique domain used to route HTTP requests to the correct application container or dyno. Each of the dynos are spread across a "dyno grid" which consists of several servers. Heroku's Git server handles application repository pushes from permitted users.

All Heroku services are hosted on Amazon's EC2 cloud-computing platform.

## Deployment Architecture:

![dia drawio](https://user-images.githubusercontent.com/25953832/162659447-d3edffc5-5c6b-4f94-8a54-3c4dd01c3b4a.png)


## Home Page: 


<img src="/static/img/HomePage_Screenshot.png" width="1000" />

## Project Requirement CheckList:

:white_check_mark: REST-based service interface for CRUD operations 
> GET, POST, PUT, DELETE 

:white_check_mark: Interaction with external REST services
> Using NLP Cloud Playground API to fetch the model
> Used Discord Api to send the summarized results directly to discord
 
:white_check_mark: Use of an external Cloud database for persisting information
> MongoDb Cluster

:white_check_mark: Serving the application over https

:white_check_mark: Implementing hash-based authentication

:white_check_mark: Implementing user accounts and access management

:white_check_mark: Securing the database with role-based policies

## REST URIs:-
- **Register User:** <POST/user/signup> Description: Method to create a new account, creates a user in our MongoDB database.
- **User Authentication:** <POST/user/login> Description: Hash based Authentication by verifying the password.
- **Update Password:** <PUT/user/updatepassword/> Description: Updates password of a registered user.
- **Invoke BART Summarizer:** (External API): <POST/dashboard/summarizer/> Description: Calls the Bart External API and generates the summary of a given text passage/article using API key.
- **External Api Discord:** <POST/dashboard/discord> Description: Sends the summary result to our discord server through the Discord Webhook.
- **GET Users:** <GET/user/getusers> Description: Admin can fetch a list of all the registered users.
- **UPDATE User Details:** <PUT/user/updateuser> Description: Admin can update the details of any specific user.
- **DELETE:** <DELETE/user/deleteuser>Description: Admin can delete a user from the database.
- **Create a User:** <POST/user/createuser>Admin can create a new user and assign a specific role. (Admin/User)


#### Links:

[![](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/ZMBqZXtKN08) 
![](https://img.shields.io/youtube/views/ZMBqZXtKN08?style=social)

[![](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)](https://docs.google.com/presentation/d/11n7AiZrcvdAyAV2WlSohrqdJGLh-v_od/edit?usp=sharing&ouid=109340109577034590549&rtpof=true&sd=true)



### Result and Feedback on the project:

<img width="946" alt="image" src="https://user-images.githubusercontent.com/35501313/178767175-2fe7c960-c4f4-4790-a5e5-9c3bd77e0990.png">
