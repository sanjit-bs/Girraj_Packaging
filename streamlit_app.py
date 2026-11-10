import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="App with Header Image",
    page_icon="🖼️",
    layout="wide"
)

# Option 1: Header Image from a Web URL
header_image_url = "https://github.com/sanjit-bs/Girraj_Packaging/blob/main/New%20Project%20(2).jpg?raw=true"  # Replace with your image URL

# Display header image
st.image(header_image_url, use_column_width=True)

# App Content below the header
st.title("Welcome to My Streamlit App")
st.write("This content appears directly below the header image.")

# ---
# Option 2: Local Image File (Uncomment lines below if loading a local file)
# st.image("path/to/your/header_image.jpg", use_column_width=True)
