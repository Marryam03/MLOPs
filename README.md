# Requirements:

Python 3.x 
Docker 
Flask 
pandas 
scikit-learn==1.2.2 
joblib

# Installation 
1. Build the Docker image:
docker build -t mlopsassignment.
2. Run the Docker container:
docker run -p 5000:5000 -it --name c_mlopsassignment mlops assignment

# Usage 
1. Feature Selection
Feature selection is already integrated into the pipeline and will be executed as part of the classification process.
2. Classification
 To classify malware samples, you can make POST requests to the API endpoint

# API Endpoint
Endpoint URL: http://localhost:5000/classify
Method: POST
* Request Body:

--> JSON object with the following structure:

 {
 
     "file_path": "/path/to/malware/sample"
   
 }
 
 * Response:
   
 --> JSON object containing the predicted class:
 
 {
 
     "predicted_class": "class_label" 
   
 }


 
