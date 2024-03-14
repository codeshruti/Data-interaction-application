# Data-interaction-application

# Problem Statement:

To develop a command line interface which retrieves queries from the user and processes the query using a json database.

# Use Case:

This project uses a Hospital case study with patient and doctor data. Queries related to patients, doctors and problems routed to doctors can be addressed by the system by Intent Recognition and Query Handling.

# Example:

- “Patients”: [{“ID”:101, “Name”: “Daisy”, “Age”: 21, “Problem”: “Fever”}]
- “Doctors”: [{“ID”: 201, “Name”: “Danna”, “Specialization”: “Physician”}]

# Working:

- When a user enters a query, the query is converted into a set of tokens. Based on the tokens, the intent is recognized and the database is used to retrieve responses of the queries. It could be based on information directly present in the database or with keywords relevant to every specialization. For example, if a user has queries about "eye" problems, they can be directed to an "Opthalmologist" instead of showing details of all doctors.

- This system will be very effective in streamlining patients and can be extended to other aspects like "hospital scans", "nurses" etc.

- The setup can be modified to other usecases with changes in the database and keywords.

# Project File Structure:

- [app.py](app.py): The main Python script.
- [requirements.txt](requirements.txt): File listing project dependencies.
- [README.md](README.md): The project README file.

# Installation:

In terminal, “pip install -r requirements.txt” – downloads all necessary libraries with their versions for running the code

# Execution:

- On command line, execute script for “app.py”.
- Enter queries and to exit the system, type “quit”.
