'''
Problem Statement: To create a simple python application which simulates database interaction, processes user queries and returns the relevant data. Demonstrates NLP, database manipulation and user input handling

Example Considered: Hospital usecase , can be extended to any usecase

Approach: Create a mock database--> Preprocess the input(lemmatization, stopword elimination)--> Recognize user intents(atleast 3 different types)-> Prepare response from database--> Simple Command line interface for simulating the process.

Input : Textual input from user
Output: Information retrieved from the database

'''

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Mock database simulating a hospital usecase with objects: Doctors and Patients
mock_database = {
    "Patients": [
        {"ID": 1, "Name": "David", "Age": 32, "Problem": "Eye"},
        {"ID": 2, "Name": "Hansal", "Age": 19, "Problem": "Fracture"},
        {"ID": 3, "Name": "Katy", "Age": 21, "Problem": "Pregnancy"}
    ],
    "Doctors": [
        {"ID": 1, "Name": "Divya", "Specialization": "Opthalmology"},
        {"ID": 2, "Name": "Saarang", "Specialization": "Paediatrician"},
        {"ID": 3, "Name": "Philip", "Specialization": "Orthopedic Surgeon"},
        {"ID": 4, "Name": "Nritya", "Specialization": "Gynaecologist"},
        {"ID": 5, "Name": "Chaitanya", "Specialization": "Physician"}
    ]
}

# Keyword Definition: Defining keywords related to every specialization(here 5 cases are considered)
specialization_keywords = {
    "Opthalmology": ['eye', 'vision', 'ophthalmic', 'cataract'],
    "Paediatrician": ['child', 'pediatric'],
    "Orthopedic Surgeon": ['bone', 'fracture', 'orthopedic'],
    "Gynaecologist": ['childbirth', 'pregnancy', 'period', 'gynaecology', 'menopause'],
    "Physician": ['general', 'consultation', 'illness','fever']
}
'''
Objective: To preprocess input given by user by removing stopwords and performing lemmatization

Input: user_input (textual data) - Textual data given by user
Output: tokens (list) - Processed tokens after lemmatization and stopwords elimination

'''
def preprocess_input(user_input):
    # Defining a lemmatizer and stopwords collector
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    # Collecting tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    # print(tokens)
    return tokens

'''
Objective: To recognize the intent of user queries from the processed tokens

Input: tokens (list) - Processed tokens after lemmatization and stopword elimination
Output: intent (str) - Recognized intent based on user query

'''
def recognize_intent(tokens):
    # Categorizing intents based on keywords
    if 'patient' in tokens or 'problem' in tokens:
        return 'patient'
    elif 'doctor' in tokens or 'specialization' in tokens:
        return 'doctor'
    else:
        return 'unknown'

'''
Objective: To query the database using the recognized intent

Input: intent (str) - Recognized intent based on user query, tokens(list) - Processed tokens
Output: result (dict) - Retrieved data from the mock database corresponding to the intent

'''
def query_database(intent, tokens):
    # Categorizing queries based on keywords
    # When intent is "patient"
    if intent == 'patient':     
        patients = mock_database['Patients']
        # If name is mentioned, check for problem and display accordingly
        if 'name' in tokens:
            patient_info = []
            for patient in patients:
                if 'problem' in tokens or patient['Problem'].lower() in tokens:
                    patient_info.append({"Name": patient["Name"], "Problem": patient["Problem"]})
            return patient_info
        # Check for problem and display name of patient
        elif 'problem' in tokens:
            problem = [token for token in tokens if token.isalpha()]
            if problem:
                problem = ' '.join(problem)
                for patient in patients:
                    if patient['Problem'].lower() == problem.lower():
                        return [{"Name": patient["Name"]}]
            return None
        else:
            return None
    # When intent is "doctor"
    elif intent == 'doctor':
        doctors = mock_database['Doctors']
        relevant_doctors = []
        for doctor in doctors:
            # Based on keywords, categorize doctors
            if any(keyword in tokens for keyword in specialization_keywords[doctor['Specialization']]):
                relevant_doctors.append(doctor)
            elif doctor['Specialization'].lower() in tokens:
                relevant_doctors.append(doctor)
        return relevant_doctors
    else:
        return None


'''
Objective: To process user queries and execute other functions, display the response to the user relevant to the hospital database

Input: None
Output: None

'''
def main():
    print("XYZ Hospital Database Interaction")
    while True:
        user_input = input("Enter your query related to the hospital database(type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        # Preprocess data
        tokens = preprocess_input(user_input)
        intent = recognize_intent(tokens)
        if intent == 'Unknown':
            print("Please give another query")
        else:
            result = query_database(intent,tokens)
            # Display result
            if result:
                print("Response:")
                print(json.dumps(result, indent=4))
            else:
                print("No relevant data found")

if __name__ == "__main__":
    main()
