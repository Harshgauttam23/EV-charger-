import streamlit as st
from utils import load_product_data, load_controller_data, display_controller_info, display_product_specs,Display_table_info
from components import display_image

# Set the page config
st.set_page_config(page_title="EV Charger Product Info", layout="centered")

# Load the product and controller data
product_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTLanvCCFozKp0soA38-gu8zF1T7LK2J2ZfAIhZjI-ouUvRsL8KAJkenCwr5K5MMlubEYiDah5WO_zh/pub?output=csv"
controller_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSX3wjkV0P7OZwkJdkl8LF1PN7kszS31C30JfWCNUWJ3FMVYGGWcmlDSxNcNQrZ7ImwDSWBoJA5Y_Jr/pub?output=csv"
Settings_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTtzM1iSrqCeldghafRySWYZI8PQTg6uFyejiygROKFPxKaeOYySBosNhToJYk4sFvMRqFNeVcCIeBv/pub?gid=0&single=true&output=csv"
Settings_url2 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTtzM1iSrqCeldghafRySWYZI8PQTg6uFyejiygROKFPxKaeOYySBosNhToJYk4sFvMRqFNeVcCIeBv/pub?gid=1645282227&single=true&output=csv"

settings_options = [
    ("CCU settings", "https://docs.google.com/spreadsheets/d/e/2PACX-1vTtzM1iSrqCeldghafRySWYZI8PQTg6uFyejiygROKFPxKaeOYySBosNhToJYk4sFvMRqFNeVcCIeBv/pub?gid=0&single=true&output=csv"),
    ("Charger Settings", "https://docs.google.com/spreadsheets/d/e/2PACX-1vTtzM1iSrqCeldghafRySWYZI8PQTg6uFyejiygROKFPxKaeOYySBosNhToJYk4sFvMRqFNeVcCIeBv/pub?gid=1645282227&single=true&output=csv"),
]



product_data = load_product_data(product_url)
controller_data = load_controller_data(controller_url)
Settings_data = load_controller_data(Settings_url)

# Streamlit UI
st.title("🚗 EV Charger Product Information")
st.markdown("---")

# Dropdown for selecting a product
product = st.selectbox("🔍 Select a Product", product_data['Product Name'].unique())

# Fetch and display product-specific information
if product:
    selected_product_data = product_data[product_data['Product Name'] == product].iloc[0]

    display_image(selected_product_data['Image URL'])
    # st.subheader(f"🖼️ {product} Image")
    # st.image(selected_product_data['Image URL'], use_column_width=True)

    # Display product specifications
    display_product_specs(selected_product_data)

    # Display controller information
    # display_controller_info(selected_product_data, controller_data)
   
    Display_table_info(Settings_data,"Configurations",settings_options)



    st.subheader(f"📄 {product} PDF Manual")
    st.markdown(f"[Click here to view the PDF]({selected_product_data['Troubleshooting']})", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2024 EV Charger Company. All rights reserved.")
