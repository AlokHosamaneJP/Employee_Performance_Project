# Overview
The "Employee Performance Prediction App" is a sophisticated tool designed to help businesses forecast the performance scores of their employees using predictive analytics. Below is a detailed breakdown of the project's components, objectives, and the technology stack used to achieve its goals:

## Objectives
The primary objective of this project is to provide an accessible, user-friendly interface through which HR departments or managers can enter relevant employee data and receive predictive insights into employee performance. This assists in better human resource planning, potentially identifying high performers for promotion or detecting areas where employees might need additional support or training.

## Features and Functionalities
  - Interactive User Interface: Built with Streamlit, the application offers a clean, intuitive interface where users can input employee data such as tenure at the company, salary, overtime hours, promotional history, and satisfaction scores.
  - Real-Time Predictions: Upon entering the data and hitting the predict button, the system processes the inputs through a pre-trained machine learning model to output a performance score, providing immediate feedback on the potential performance level of the employee.
## Prerequisites
  - Python 3.7+
  - Streamlit
  - Joblib
  - Numpy
  - ScikitLearn
## Data Handling
  - Input Features: The model takes the following inputs to predict performance scores:
  - Years at the Company - Reflects the tenure of the employee.
  - Monthly Salary - Compensation details of the employee.
  - Overtime Hours - Additional hours worked beyond the regular schedule.
  - Promotions - The number of promotions received.
  - Employee Satisfaction Score - A quantified measure of employee contentment.
These features are crucial as they directly relate to an employee's engagement and productivity at work. The predictive model was likely trained on historical data to understand patterns and correlations between these features and the overall performance outcomes.

## Model and Predictions
  - Scaler (scaler.pkl): Before feeding into the model, the input features are scaled using this scaler, ensuring that the model receives data in the format it expects, which is crucial for accurate predictions.
  - Predictive Model (model.pkl): This file contains the serialized version of the machine learning model. The app uses this model to make predictions based on the input data. The model is pre-trained, likely on a dataset that includes historical employee performance data, allowing it to generalize and predict new unseen data accurately.
## Technology Stack
  - Python: The core programming language used for creating the application.
  - Streamlit: A Python library that enables the creation of web apps quickly and with fewer lines of code, ideal for machine learning and data science projects.
  - Joblib: Used for saving and loading the model and scaler objects, which is crucial for deploying machine learning models into production.
  - Numpy: A fundamental package for scientific computing with Python, used here for handling data arrays.
## Deployment and Usage
  The app is deployed locally via Streamlit, making it accessible via a web browser. This setup is ideal for demonstrations or small-scale deployment within an organization. Users simply run the application script and interact with it in their browser, entering data as required and receiving predictions instantly.

## Conclusion
  This project encapsulates the integration of data science and web development to create practical business solutions. It stands out by offering real-time, data-driven insights that can enhance decision-making processes regarding employee management and development.

![Screenshot 2025-01-19 at 7 55 13 PM](https://github.com/user-attachments/assets/494ddd24-89b5-484a-9543-e78913a7d8da)

