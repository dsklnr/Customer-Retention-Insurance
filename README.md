# Predictive Modeling for Risk-Based Premiums and Real-Time Safety Guidance in Auto Insurance Customer Retention

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
</br>
</br>

# Key Features:

Data Integration: The project involved the integration of various real-time data streams, including weather conditions, traffic congestion, and accident history, enabling a comprehensive risk assessment model that reflects real-world driving environments.

Machine Learning Models: The MLP model, chosen for its robust performance in handling non-linear relationships, was trained and validated using historical data to predict accident severity. CatBoost, an algorithm optimized for categorical data, showed slightly better performance but was ultimately surpassed by the MLP in terms of real-world applicability.

Feature Importance: Analysis revealed that factors like weather conditions, traffic density, and driver behaviors play a significant role in predicting accident severity, allowing BMK Insurance to optimize its risk assessment process.

Dynamic Insurance Pricing: Based on the predictions of accident severity and personalized risk scores, the model generates dynamic, real-time insurance premiums that are tailored to individual driving environments, ensuring fair pricing.

Real-Time Alerts and Route Suggestions: The system provides real-time alerts for adverse weather and high-risk traffic conditions, along with suggestions for safer, less congested routes to improve driver safety.

By leveraging machine learning and real-time data, BMK Insurance has developed a proactive approach to insurance pricing, offering personalized premiums based on real-time risk factors. This innovative system not only provides fairer pricing but also fosters customer loyalty through enhanced safety measures and personalized services. Future research could expand on these findings by exploring temporal factors and further refining the predictive models to improve accuracy.
</br>
</br>

# Using the Predictive Model

### Installation
To use this project, navigate to where you would like the repo cloned on your machine. Then clone the repo on your device using the commands below:

'git clone https://github.com/mmoran90/ADS-509-Text-Mining.git'

### Running the Streamlit Data Visualization
After the repo has been cloned, perform the following steps
   - Open a command prompt (windows) or terminal (Linux/MacOS) and navigate to where the repo was cloned
   - Ensure python3 is installed on your machine (python --version)
     - If python3 is not installed, please do so now  
   - Execute `python app.exe` from command prompt/terminal
     - `app.exe` utiliztes localhost (127.0.0.1)
   - Steamlit will automatically open

</br>
Now enter any or all fields in the webpage, where the application can predict a severity score based on a google maps route.
</br>
Additionally, the route will show on google maps based on provided zip codes and a severity score will be output to the webpage.
</br>
</br>

### Troubleshooting Streamlit
You might encounter issues where your interpreter cannot find libraries that are already installed on your machine. If that happens, create a local virtual environment. Below are steps to do so.
</br>
  - Windows
    - Create a new virtual environment
      - `python -m venv myenv`
    - Activate the virtual environment
      - `myenv\Scripts\activate`
  - MacOS/Linux
    - Create a new virtual environment
      - `python -m venv myenv`
    - Activate the virtual environment
      - `source myenv/bin/activate`
      
Now use `pip install <library>` for any missing libraries in your virtual environment. Below are all the libraries required:
  - streamlit
  - streamlit_folium
  - pandas
  - joblib
  - folium
  - geopy
  - googlemaps
  - base64
</br>
</br>

### Contributor(s)
* [Marvin Moran](https://github.com/mmoran90)
* [Katie Mears](https://github.com/KatieMears628)
* [Ben Ogle](https://github.com/dsklnr)
</br>
