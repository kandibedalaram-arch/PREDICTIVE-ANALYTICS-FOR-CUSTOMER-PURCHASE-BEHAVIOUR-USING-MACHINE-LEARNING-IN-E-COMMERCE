Predictive Analytics for Customer Purchase Behaviour Using Machine Learning in E-Commerce

Project Overview

This project develops a machine learning solution to predict customer purchase behaviour in an e-commerce platform using behavioural and transactional data. The objective is to help businesses identify customers who are likely to make a purchase, improve marketing strategies, and increase conversion rates through data-driven decision-making.

The project covers the complete machine learning lifecycle, including data preprocessing, model development, model explainability, API development, containerization, and cloud deployment.

Business Objective

The objectives of this project are to:

* Predict customer purchase behaviour using machine learning.
* Identify the key behavioural and transactional factors influencing purchase decisions.
* Compare multiple machine learning algorithms to determine the best-performing model.
* Support personalised marketing strategies and improve customer conversion rates.

📊 Dataset Information

* Source: Kaggle – Customer Purchase Behaviour Dataset
* Dataset Type: Structured e-commerce behavioural and transactional data

Features

* Age
* Annual Income
* Time Spent on Website
* Visit Frequency
* Session Activity
* Loyalty Program Participation
* Purchase History
* Purchase Outcome (Target Variable)

Project Workflow

1. Data Preprocessing

* Cleaned and prepared the dataset.
* Handled missing values.
* Encoded categorical variables.
* Performed feature engineering.
* Split the dataset into 80% training and 20% testing.

2. Exploratory Data Analysis (EDA)

* Analyzed customer demographics and purchasing behaviour.
* Explored behavioural patterns influencing purchase decisions.
* Visualized relationships between important features and customer purchases.

3. Machine Learning Models

The following classification algorithms were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

4. Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix

XGBoost achieved the best performance with an accuracy of 95%, outperforming all other classification models.

Model Explainability

To improve model transparency and interpretability:

* Applied Feature Importance to identify the most influential predictors.
* Used SHAP (SHapley Additive Explanations) to explain individual predictions and understand feature contributions.

The most influential factors affecting customer purchases include:

* Discounts
* Time Spent on Website
* Loyalty Program Participation
* Annual Income
* Customer Age

Behavioural variables were found to have greater predictive power than demographic variables.

Key Insights

* Customers spending more time on the website are more likely to make purchases.
* Loyalty program participation significantly increases purchase probability.
* Discounts strongly influence customer buying decisions.
* Behavioural engagement is a stronger predictor than demographic characteristics.

Business Recommendations

* Implement predictive analytics to identify high-potential customers.
* Personalize marketing campaigns based on predicted purchase behaviour.
* Increase customer engagement through loyalty programs.
* Optimize promotional campaigns using model predictions.

Model Deployment

The trained machine learning model was deployed as a REST API for real-time customer purchase prediction.

Deployment Workflow

* Developed REST API endpoints using FastAPI.
* Implemented request validation using Pydantic.
* Tested the API using Postman.
* Containerized the application using Docker.
* Deployed the Docker container on AWS EC2.
* Managed source code using Git and GitHub.

The deployed API accepts customer information as input and returns a prediction indicating whether the customer is likely to purchase.

Tools & Technologies

Programming & Machine Learning

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* XGBoost

Model Explainability

* SHAP

API Development

* FastAPI
* Pydantic
* Postman

Deployment

* Docker
* AWS EC2

Version Control

* Git
* GitHub

Future Improvements

* Improve prediction performance using LightGBM and CatBoost.
* Automate deployment using CI/CD pipelines.
* Implement model monitoring and logging.
* Deploy using Kubernetes or AWS ECS for scalability.

Conclusion

This project demonstrates an end-to-end machine learning solution for predicting customer purchase behaviour in e-commerce. By combining predictive analytics, explainable AI, REST API development, Docker containerization, and AWS cloud deployment, the project provides a scalable solution that supports data-driven marketing and business decision-making.
