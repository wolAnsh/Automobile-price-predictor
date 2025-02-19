# Automobile Price Predictor

This project is a web application that predicts automobile prices using a machine learning model deployed on Azure Machine Learning. The frontend is built with HTML and CSS, while the backend utilizes Flask, a Python web framework.

## Features

- **User Input Form:** Submit automobile features via a web form.
- **Prediction Display:** View the predicted price based on input features.

## Model Design

The machine learning model was designed and trained using Azure Machine Learning. Below is a visual representation of the model's architecture:

![Model Design](assets/Azure_ML_pipeline.png)

## Web Application Interface

Users can input vehicle details through the web interface:

![Web App Input](assets/Input_Azure_ML.png)

Upon submission, the application displays the predicted price:

![Web App Output](assets/Output_Azure_ML.png)

## Prerequisites

- Python 3.x
- Flask
- Requests library
- An active Azure Machine Learning endpoint

