
import streamlit as st
import requests

st.title("Application Front-end for Superkart") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=0.027) #Complete the code to define the UI element for Product_Allocated_Area
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=117.08) #Complete the code to define the UI element for Product_MRP
Store_Size = st.selectbox("Store Size", options=["Medium", "High", "Small"], index=0) #Complete the code to define the UI element for Store_Size
Store_Location_City_Type = st.selectbox("Store Location City Type", options=["Tier 2", "Tier 1", "Tier 3"], index=0) #Complete the code to define the UI element for Store_Location_City_Type
Store_Type = st.selectbox("Store Type", options=["Supermarket Type2", "Departmental Store", "Supermarket Type1", "Food Mart"], index=0) #Complete the code to define the UI element for Store_Type
Product_Id_char = st.selectbox("Product ID Character", options=["FD", "NC", "DR"], index=0) #Complete the code to define the UI element for Product_Id_char
Store_Age_Years = st.number_input("Store Age (Years)", min_value=16, max_value=38, value=24) #Complete the code to define the UI element for Store_Age_Years
Product_Type_Category = st.selectbox("Product Type Category", options=["Non Perishables", "Perishables"], index=0) #Complete the code to define the UI element for Store_Age_Years

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    # Placeholder URLs for demonstration. Replace with actual deployed API URL.
    model_root_url = "https://<user_name>-<space_name>.hf.space"
    api_endpoint = f"{model_root_url}/v1/predict" # Assuming the Flask API endpoint is /v1/predict

    response = requests.post(api_endpoint, json=product_data)    # Complete the code to enter user name and space name to correctly define the endpoint
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error(f"Error in API request: {response.status_code} - {response.text}")

# NEW CODE RRA
# import json  # To handle JSON formatting for API requests and responses
# import pandas as pd  # For data manipulation and analysis
# import numpy as np  # For numerical computations
