# Risk-Based Premiums and Real-Time Safety Guidance for Car Insurance Customer Retention

# Overview 
### Problem Statement:
Auto insurance companies traditionally use demographic data and historical claims to set premiums, but this approach often fails to accurately assess the risk of individual drivers. This misalignment results in customers paying premiums that do not reflect their actual driving behavior or environmental conditions. BMK Insurance recognized this issue and developed a predictive modeling framework aimed at assessing individual accident risk. By incorporating real-time data, including weather, traffic patterns, and driving behaviors, the company seeks to create dynamic, personalized premiums that better align with each customer's unique risk exposure. This project addresses the need for a more precise, data-driven approach to insurance pricing, leading to fairer premiums, improved customer satisfaction, and better customer retention.

### Approach:
This study utilized machine learning techniques to predict accident severity, with the ultimate goal of developing a dynamic pricing model for auto insurance. The approach involved:

1.  Data Collection and Integration: 
A comprehensive dataset was created by integrating various data sources, including weather conditions, traffic patterns, and accident history. Real-time data was also used to capture current environmental conditions, ensuring that predictions reflect the latest driving environments.

2. Model Selection: 
Two primary models were evaluated for their predictive capabilities: the Multi-Layer Perceptron (MLP) and CatBoost. Both models demonstrated strong performance, but the MLP model was selected for deployment due to its ability to capture complex non-linear relationships and its scalability. The model showed an excellent fit with a low Root Mean Squared Error (RMSE) of 0.0436 and an R-squared value of 0.8830.

3. Risk Assessment and Personalized Pricing:
The MLP model was used to predict accident severity based on environmental and driving conditions. These predictions were then used to calculate personalized risk scores for individual drivers, which formed the basis for dynamic, risk-based insurance premiums.

4. Real-Time Safety Guidance: In addition to predictive modeling, BMK Insurance implemented a system that provides real-time safety alerts and route recommendations based on current weather and traffic conditions, aiming to reduce accident risk for drivers in real-time.

# Key Features:

Data Integration: The project involved the integration of various real-time data streams, including weather conditions, traffic congestion, and accident history, enabling a comprehensive risk assessment model that reflects real-world driving environments.

Machine Learning Models: The MLP model, chosen for its robust performance in handling non-linear relationships, was trained and validated using historical data to predict accident severity. CatBoost, an algorithm optimized for categorical data, showed slightly better performance but was ultimately surpassed by the MLP in terms of real-world applicability.

Feature Importance: Analysis revealed that factors like weather conditions, traffic density, and driver behaviors play a significant role in predicting accident severity, allowing BMK Insurance to optimize its risk assessment process.

Dynamic Insurance Pricing: Based on the predictions of accident severity and personalized risk scores, the model generates dynamic, real-time insurance premiums that are tailored to individual driving environments, ensuring fair pricing.

Real-Time Alerts and Route Suggestions: The system provides real-time alerts for adverse weather and high-risk traffic conditions, along with suggestions for safer, less congested routes to improve driver safety.

By leveraging machine learning and real-time data, BMK Insurance has developed a proactive approach to insurance pricing, offering personalized premiums based on real-time risk factors. This innovative system not only provides fairer pricing but also fosters customer loyalty through enhanced safety measures and personalized services. Future research could expand on these findings by exploring temporal factors and further refining the predictive models to improve accuracy.

### Contributor(s)
* [Marvin Moran](https://github.com/mmoran90)
* [Katie Mears](https://github.com/KatieMears628)
* [Ben Ogle](https://github.com/dsklnr)
</br>
