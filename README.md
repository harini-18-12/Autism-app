# Autism-app
AUTISM RISK PREDICTION

Project Overview

This project is a machine learning–powered web application designed to predict the risk of autism in individuals based on screening data and behavioral patterns. The aim is to provide a simple, accessible, and interactive platform that uses the AQ-10 questionnaire and other relevant personal details to assess whether a person is at high or low risk of Autism Spectrum Disorder (ASD).

The application is built using Streamlit, and the prediction is handled by a trained machine learning model loaded from a ".pkl" file.

 Input Features

The app collects the following inputs from users:

1. Gender – Male or Female  
2. Ethnicity – Europeans, Latino, Africans, Asian, Others  
3. Jaundice History– Whether the individual had jaundice as a child  
4. Family History – Whether there's a family history of autism  
5. AQ-10 Responses (A1 to A10) – Behavioral indicators (Yes/No)  
6. Country of Residence
7. Used Screening App Before – Yes/No  
8. Result from Screening App – Yes/No  
9. Relation with Person – Parent, Self, Relative, Health Care Professional, Others  
10.Dependency– Whether the person has any dependency  
11.Who Completed the Test – Self, Parent, Caregiver, Other  

Key Features of the Project

 1. User Interface:
- Developed using Streamlit for a fast, interactive web experience
- Clean form-based design for entering responses

2. Machine Learning Model:
- Trained using historical autism screening data
- Uses features derived from AQ-10 and demographic info
- Stored as `autism_model.pkl` and loaded with `joblib`

3. Prediction Output:
- Displays "High Risk of Autism" or "Low Risk of Autism"
- Uses 23 numerical features for accurate prediction

Technologies Used

1.Python – Programming language  
2.Streamlit – Web interface  
3.Scikit-learn– Model training and loading  
4.Joblib– Model serialization  
5. NumPy – Numerical array processing  

Visualizations (Planned or Possible Additions)

- AQ Score Distribution
- Risk Trends by Gender or Ethnicity
- User Risk Analysis Over Time (if database integration is added)


