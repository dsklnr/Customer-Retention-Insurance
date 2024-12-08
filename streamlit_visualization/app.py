# install packages and libraries
import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
import googlemaps
from geopy.distance import geodesic
from googlemaps.convert import decode_polyline
import base64

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded_image

# Logo path
logo_path = "BMK2.png"

# Display logo at the top-left
st.markdown(
    f"""
    <style>
        .top-left-logo {{
            position: fixed;
            top: 70px;
            left: 70px;
            z-index: 1000;
        }}
    </style>
    <div class="top-left-logo">
        <img src="data:image/png;base64,{get_base64_image(logo_path)}" style="height: 200px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize Google Maps API Client
API_KEY = 'AIzaSyBwtfk9O2YwT-K3UMejRVDxMtGCNbVPNWM' 
gmaps = googlemaps.Client(key=API_KEY)

# Load Optimal Model
model_path = 'optimized_mlp_model.pkl'
optimized_mlp = joblib.load(model_path)

# Load training data feature names and default values
training_data_path = "pca_reduced_features.csv"
training_data = pd.read_csv(training_data_path)
feature_names = training_data.columns.tolist()
default_feature_values = training_data.mean().to_dict()

# Function to calculate distance using Google Maps API
def calculate_distance(zip1, zip2):
    try:
        directions = gmaps.directions(origin=zip1, destination=zip2, mode="driving")
        route = directions[0]
        polyline = route["overview_polyline"]["points"]
        distance_meters = sum(leg["distance"]["value"] for leg in route["legs"])
        distance_miles = distance_meters * 0.000621371
        return distance_miles, polyline
    except Exception as e:
        st.error(f"Error calculating distance: {e}")
        return None, None

# Function to decode and validate polyline
def decode_and_validate_polyline(polyline):
    try:
        decoded_polyline = decode_polyline(polyline)  # Decode polyline
        validated = [(point["lat"], point["lng"]) for point in decoded_polyline]
        return validated
    except Exception as e:
        st.error(f"Invalid polyline data: {e}")
        return []

# Persistent state
if "results" not in st.session_state:
    st.session_state["results"] = []
if "maps" not in st.session_state:
    st.session_state["maps"] = []
if "route_comparisons" not in st.session_state:
    st.session_state["route_comparisons"] = []

# App UI
st.title("Accident Severity Prediction App")
st.write("Enter the starting and ending zip codes to calculate the predicted accident severity score.")

# User inputs
zip_start = st.text_input("Enter Starting Zip Code:")
zip_end = st.text_input("Enter Ending Zip Code:")

if st.button("Predict Severity"):
    if not zip_start or not zip_end:
        st.error("Please provide both starting and ending zip codes.")
    else:
        # Calculate distance and get polyline
        distance_miles, polyline = calculate_distance(zip_start, zip_end)
        if distance_miles is not None and polyline:
            # Prepare input features
            input_features = {feature: default_feature_values[feature] for feature in feature_names}
            input_features["Distance(mi)_target_encoded"] = distance_miles
            input_df = pd.DataFrame([input_features])
            input_df = input_df[optimized_mlp.feature_names_in_]

            # Predict severity
            severity_score = optimized_mlp.predict(input_df)[0]

            # Safety tips
            safety_tips = []
            if severity_score > 1.0:  # Adjust threshold as appropriate
                safety_tips.append("High Severity Score! Consider the following tips:")
                safety_tips.append("- Avoid traveling during severe weather conditions.")
                safety_tips.append("- Reduce speed and maintain a safe distance from other vehicles.")
                safety_tips.append("- Ensure your vehicle is in good condition before traveling.")
            else:
                safety_tips.append("Low Severity Score. Have a safe trip!")

            # Store results
            result = {
                "zip_start": zip_start,
                "zip_end": zip_end,
                "distance_miles": distance_miles,
                "severity_score": severity_score,
                "safety_tips": safety_tips,
            }
            st.session_state["results"].append(result)

            # Display the route on a map
            geocode_start = gmaps.geocode(zip_start)
            geocode_end = gmaps.geocode(zip_end)
            start_location = geocode_start[0]["geometry"]["location"]
            end_location = geocode_end[0]["geometry"]["location"]

            # Create a folium map
            map_ = folium.Map(location=[start_location["lat"], start_location["lng"]], zoom_start=12)
            folium.Marker([start_location["lat"], start_location["lng"]],
                          popup="Start", icon=folium.Icon(color="green")).add_to(map_)
            folium.Marker([end_location["lat"], end_location["lng"]],
                          popup="End", icon=folium.Icon(color="red")).add_to(map_)

            # Decode and validate polyline
            validated_polyline = decode_and_validate_polyline(polyline)
            if validated_polyline:
                folium.PolyLine(locations=validated_polyline, color="blue").add_to(map_)
                st.session_state["maps"].append(map_)
            else:
                st.error("Could not visualize the route due to invalid polyline data.")
        else:
            st.error("Could not calculate distance or retrieve route information. Please check the zip codes and try again.")

# Display results
for idx, result in enumerate(st.session_state["results"]):
    st.write(f"**Route {idx + 1}:**")
    st.write(f"Starting Zip: {result['zip_start']}")
    st.write(f"Ending Zip: {result['zip_end']}")
    st.write(f"Distance: {result['distance_miles']:.2f} miles")
    st.write(f"Predicted Severity Score: {result['severity_score']:.2f}")
    st.subheader("Safety Tips")
    for tip in result["safety_tips"]:
        st.write(tip)
    if idx < len(st.session_state["maps"]):
        st_folium(st.session_state["maps"][idx], width=700, height=500)

# Route Comparisons
st.header("Compare Multiple Routes")

num_routes = st.number_input("How many routes would you like to compare?", min_value=1, max_value=5, value=1, step=1)
routes = []
for i in range(num_routes):
    st.write(f"Route {i + 1}")
    route_start = st.text_input(f"Start Zip Code for Route {i + 1}", key=f"start_{i}")
    route_end = st.text_input(f"End Zip Code for Route {i + 1}", key=f"end_{i}")
    routes.append((route_start, route_end))

if st.button("Compare Routes"):
    route_data = []
    for i, (route_start, route_end) in enumerate(routes):
        if route_start and route_end:
            distance_miles, polyline = calculate_distance(route_start, route_end)
            if distance_miles is not None and polyline:
                input_features = {feature: default_feature_values[feature] for feature in feature_names}
                input_features["Distance(mi)_target_encoded"] = distance_miles
                input_df = pd.DataFrame([input_features])[optimized_mlp.feature_names_in_]
                severity_score = optimized_mlp.predict(input_df)[0]
                route_data.append({
                    "Route": f"Route {i + 1}",
                    "Distance (mi)": distance_miles,
                    "Severity Score": severity_score
                })
    if route_data:
        st.session_state["route_comparisons"] = route_data
        st.write("Route Comparison:")
        st.dataframe(pd.DataFrame(route_data))
