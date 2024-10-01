import pandas as pd
import streamlit as st
from components import display_image

def load_product_data(url):
    """Load product data from the provided URL."""
    return pd.read_csv(url)

def load_controller_data(url):
    """Load controller data from the provided URL."""
    return pd.read_csv(url)

def display_product_specs(selected_product_data):
    """Display the specifications of the selected product."""
    st.markdown(f"""
    - **Power**: {selected_product_data['Power Rating']}
    - **Voltage**: {selected_product_data['Voltage']}
    - **Dimensions**: {selected_product_data['Dimensions']}
    - **Part Code**: {selected_product_data['Part No.']}
    - **Charging Type**: {selected_product_data['AC/DC']}
    - **Controllers Used**: {selected_product_data['Controllers']}

    """)
    controllers = selected_product_data['Controllers'].split(',')

    # st.subheader(f"📄 {controllers[0]} Upper COntroller S/W")
    st.markdown(f"[Click here to download the latest S/W of {controllers[0]}]({selected_product_data['First Controller S/W']})", unsafe_allow_html=True)

    st.markdown(f"[Click here to download the latest S/W of {controllers[1]}]({selected_product_data['Second Controller S/W']})", unsafe_allow_html=True)

# def display_controller_info(selected_product_data, controller_data):
#     """Display controller information based on the selected product."""
#     # Split the 'Controllers' field to get individual controller names
#     controllers = selected_product_data['Controllers'].split(',')
    
#     st.subheader("🛠️ Controller Information")
    
#     # Set to keep track of displayed controllers
#     displayed_controllers = set()
    
#     for controller in controllers:
#         controller = controller.strip()  # Clean whitespace
#         # Search for the controller in the controller data
#         controller_info = controller_data[controller_data['Controller Name'] == controller]
        
#         if not controller_info.empty:
#             if controller not in displayed_controllers:
#                 # Display the description(s) for the found controller
#                 descriptions = controller_info['Controller Description'].values
#                 st.markdown(f"**{controller}**:")
#                 for desc in descriptions:
#                     st.markdown(f"- {desc}")
#                 # Add controller to the displayed set
#                 displayed_controllers.add(controller)
#         else:
#             st.warning(f"No description found for **{controller}**.")



def display_controller_info(selected_product_data, controller_data):
    """Display controller information and images based on the selected product."""
    # Split the 'Controllers' field to get individual controller names
    controllers = selected_product_data['Controllers'].split(',')
    
    st.subheader("🛠️ Controller Information")
    
    # Set to keep track of displayed controllers
    displayed_controllers = set()
    
    for controller in controllers:
        controller = controller.strip()  # Clean whitespace
        # Search for the controller in the controller data
        controller_info = controller_data[controller_data['Controller Name'] == controller]
        
        if not controller_info.empty:
            if controller not in displayed_controllers:
                # Display the controller name
                st.markdown(f"**{controller}**:")
                
                # Display the controller image
                controller_image_url = controller_info['Image URL'].values[0]
                print(controller_image_url)
                display_image(controller_image_url)

                # st.image(controller_image_url, caption=controller, use_column_width=True)

                # Display the description(s) for the found controller
                descriptions = controller_info['Controller Description'].values
                for desc in descriptions:
                    st.markdown(f"- {desc}")
                
                # Add controller to the displayed set
                displayed_controllers.add(controller)
        else:
            st.warning(f"No description found for **{controller}**.")

def Display_table_info(df,title,settings_options):
    st.title(title)
    # Search box to filter the DataFrame

     
   
# Create a selectbox with display names
    st.markdown(
    """
    <style>
    .stSelectbox {
        font-size: 20px;  /* Change the font size here */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a selectbox with display names
    setting_chosen = st.selectbox("🔍 Select which settings you are looking for", [name for name, url in settings_options])


# Get the corresponding URL for the selected setting
    selected_url = dict(settings_options)[setting_chosen]
    Settings_data = load_product_data(selected_url)

    if 'Path' in df.columns and not df['Path'].empty:
      unique_path = df['Path'].unique()
    # Display the first unique path
      st.markdown(f"- **Path**: {unique_path[0]}")
    else:
      st.markdown("- **Path**: No path available.")
    
    df_first_three = df.iloc[:, 1:3]

# Display the DataFrame without the index
    st.dataframe(df_first_three.style.hide(axis= 'index'), use_container_width=True, height=1000)
    
    # st.dataframe(df_first_three.style.hide_index(), use_container_width=True)



    # styled_df = df.style.set_properties(**{
    #     'text-align': 'left',
    #     'white-space': 'pre-wrap'  # This can help with text wrapping in some cells
    # })
    
    # # Display the DataFrame with st.dataframe (interactive)
    # st.dataframe(styled_df, use_container_width=True)
   

    # Optionally, add a download button for the filtered data
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download filtered data as CSV", data=csv, file_name='filtered_data.csv', mime='text/csv')



