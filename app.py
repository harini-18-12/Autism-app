import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('autism_model.pkl')

# Streamlit app title
st.title('Autism Risk Prediction')

# Collect user inputs
gender = st.selectbox('Gender', ['Male', 'Female'])
ethnicity = st.selectbox('Ethnicity', ['Europeans', 'Latino', 'Africans','Asian','Others',])
jaundice = st.selectbox('Jaundice (Yellowing of Skin)', ['Yes', 'No'])
family_history = st.selectbox('Family history of Autism', ['Yes', 'No'])
A1_Score = st.selectbox('A1 Score (noticing small sounds)', ['Yes', 'No'])
A2_Score = st.selectbox('A2 Score (focusing on whole picture)', ['Yes', 'No'])
A3_Score = st.selectbox('A3 Score (handling multi-tasking)', ['Yes', 'No'])
A4_Score = st.selectbox('A4 Score (switching focus after interruption)', ['Yes', 'No'])
A5_Score = st.selectbox('A5 Score (reading between lines)', ['Yes', 'No'])
A6_Score = st.selectbox('A6 Score (knowing if listener is bored)', ['Yes', 'No'])
A7_Score = st.selectbox('A7 Score (understanding character intentions)', ['Yes', 'No'])
A8_Score = st.selectbox('A8 Score (collecting info about categories)', ['Yes', 'No'])
A9_Score = st.selectbox('A9 Score (understanding emotions by face)', ['Yes', 'No'])
A10_Score = st.selectbox('A10 Score (working out people’s intentions)', ['Yes', 'No'])
country_of_residence = st.text_input('Country of Residence')
used_app_before = st.selectbox('Have you used a screening app before?', ['Yes', 'No'])
result = st.selectbox('Result from screening app', ['Yes', 'No'])
relation = st.selectbox('Relation with Person', ['Parent', 'Self', 'Relative', 'Health Care Professional', 'Others'])

# Additional inputs to match 23 features
dependency = st.selectbox('Does the person have a dependency?', ['Yes', 'No'])
who_completed_test = st.selectbox('Who completed the test?', ['Self', 'Parent', 'Caregiver', 'Other'])

# Convert 'Yes'/'No' to 1/0
def convert_yes_no(value):
    return 1 if value == 'Yes' else 0

# Prepare the features array
features = np.array([
    1 if gender == 'Male' else 0,
    1 if ethnicity == 'White-European' else (2 if ethnicity == 'Latino' else 3),
    convert_yes_no(jaundice),
    convert_yes_no(family_history),
    convert_yes_no(A1_Score),
    convert_yes_no(A2_Score),
    convert_yes_no(A3_Score),
    convert_yes_no(A4_Score),
    convert_yes_no(A5_Score),
    convert_yes_no(A6_Score),
    convert_yes_no(A7_Score),
    convert_yes_no(A8_Score),
    convert_yes_no(A9_Score),
    convert_yes_no(A10_Score),
    hash(country_of_residence) % 100 if country_of_residence else 0,
    convert_yes_no(used_app_before),
    convert_yes_no(result),
    1 if relation == 'Parent' else 2 if relation == 'Self' else 3 if relation == 'Relative' else 4 if relation == 'Health Care Professional' else 5,
    convert_yes_no(dependency),
    1 if who_completed_test == 'Self' else 2 if who_completed_test == 'Parent' else 3 if who_completed_test == 'Caregiver' else 4,
    1, 1, 1  # Placeholder features to ensure 23 features
]).reshape(1, -1)

# Debugging output to check feature count
st.text(f'Feature array shape: {features.shape}')

# Ensure 23 features are included
if features.shape[1] == 23:
    # Make prediction
    prediction = model.predict(features)[0]

    # Display result
    if prediction == 1:
        st.subheader('High Risk of Autism')
    else:
        st.subheader('Low Risk of Autism')
else:
    st.error(f'Incorrect number of features: {features.shape[1]} provided, but 23 expected. Please check your inputs.')
