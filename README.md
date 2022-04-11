# Cloud Computing: MiniProject - Modalysis

![](https://img.shields.io/apm/l/vim-mode?color=blue&style=plastic)
![](https://img.shields.io/github/commit-activity/m/antra0497/Modalysis?color=green&style=plastic)
![](https://img.shields.io/github/languages/count/antra0497/Modalysis?color=orange&style=plastic)
![]()
![]()
![]()


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
![](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=antra0497&repo=Modalysis&langs_count=8)](https://github.com/antra0497/Modalysis)

### Bart Summarization:
> Summarization strategies are typically categorized as extractive, abstractive or mixed. 
>  - Extractive strategies select the top N sentences that best represent the key points of the article. 
>  - Abstractive summaries seek to reproduce the key points of the article in new words.
>  
> Extractive summarization is a challenging NLP task that has only recently become practical by transformer models like BART. It is a denoising autoencoder for pretraining sequence-to-sequence models. BART is trained by 
>  - (1) corrupting text with an arbitrary noising function, and 
>  - (2) learning a model to reconstruct the original text. 
>  
>  It uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and many other more recent pretraining schemes. Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT)

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
## Setup: GCP Deployment

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


## Home Page: 


<img src="/static/img/HomePage_Screenshot.png" width="1000" />

## Project Requirement CheckList:

:white_check_mark: REST-based service interface for CRUD operations 
> GET, POST, PUT, DELETE

:white_check_mark: Interaction with external REST services
> Used Discord Api to send the summarized results directly to discord
 
:white_check_mark: Use of an external Cloud database for persisting information
> MongoDb Cluster

:white_check_mark: Serving the application over https

:white_check_mark: Implementing hash-based authentication

:white_check_mark: Implementing user accounts and access management

:white_check_mark: Securing the database with role-based policies

#### Links:

![](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)

![](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
