# Cloud Computing: MiniProject - Modalysis

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

### Bert Summarization:
> Summarization strategies are typically categorized as extractive, abstractive or mixed. 
>  - Extractive strategies select the top N sentences that best represent the key points of the article. 
>  - Abstractive summaries seek to reproduce the key points of the article in new words.
>  Extractive summarization is a challenging NLP task that has only recently become practical by transformer models like BERT(Bidirectional Encoder Representations from Transformers) published by researchers at Google AI Language. BERT (Bidirectional transformer) is a transformer used to overcome the limitations of RNN and other neural networks as Long term dependencies. It is a pre-trained model that is naturally bidirectional.

## Setup: Local Deployment
```
git clone https://github.com/antra0497/Modalysis.git
cd Modalysis
pip install -r requirements.txt
```
Download pretrained Bert Model:
```
cd user
python model_download.py
```
Run the Flask server
```
python wsgi.py
```




## Home Page:
<img src="/static/img/HomePage_Screenshot.png" width="1000" />




