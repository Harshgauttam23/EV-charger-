import streamlit as st
from PIL import Image
import requests
from io import BytesIO


# def display_product_specs(product_data):
#     st.markdown(f"""
#     - **Power**: {product_data['Power Rating']}
#     - **Voltage**: {product_data['Voltage']}
#     - **Dimensions**: {product_data['Dimensions']}
#     - **Part Code**: {product_data['Part No.']}
#     - **Charging Type**: {product_data['AC/DC']}


#     """)

def display_pdf_link(pdf_url):
    st.markdown(f"[Click here to view the PDF]({pdf_url})", unsafe_allow_html=True)


def display_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True)
    except Exception as e:
        st.error("Image could not be loaded. Please check the Image URL.")

