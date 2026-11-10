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
st.title("Welcome")
st.write("content appearing below.")

#################### ----------------TDS, Inv, Trasport, Loading, Unloading----------------------- #########################
st.markdown("---")
st.subheader("📄 Freight, Inv & Expenses Verification System")
st.markdown("[Freight, Inv & Expenses Verification System](https://girraj-packaging-payment-app-6ygwp4mpmog.streamlit.app)")

#################### ----------------Purchase Order & Verification System------------------------- #########################
st.markdown("---")
st.subheader("📄 Purchase Order & Verification System")
st.markdown("[Purchase Order & Verification System](https://shivam-girrag-po-app-sktjwrhte2s.streamlit.app)")

#################### ----------------Production Stock & Rill Stock Manager------------------------ #########################
st.markdown("---")
st.subheader("📄 Production Stock & Rill Stock Manager")
st.markdown("[Production Stock & Rill Stock Manager App](https://making-cost-rill-stock-app.streamlit.app)")

#################### ----------------Paper Sheet Stock Manager------------------------ #########################
st.markdown("---")
st.subheader("📄 Purchase Invoice Verification")
st.markdown("[Purchase Invoice Verification App](https://purchase-invoice-app-54o883fk8jv.streamlit.app)")
    
#################### ---------------- Quality Test Report Generator ------------------------ #########################
st.markdown("---")
st.subheader("Quality Test Report Generator")
st.markdown("[Quality Test Report Generator App](https://idyllic-unicorn-9a9402.netlify.app)")

#################### ---------------- Tax Invoice Generator (Tally Layout) ------------------------ #########################
st.markdown("---")
st.subheader("Tax Invoice Generator")
st.markdown("[Tax Invoice Generator App](https://lively-parfait-437225.netlify.app)")

#################### ---------------- Carton Box Cost Calculator ---------------------------#################
st.markdown("---")
st.subheader("Carton Box Cost Calculato")
st.markdown("[Carton Box Cost Calculato App](https://nimble-conkies-8f0b18.netlify.app)")

#################### ------------------- ⭐Paper Sheet Stock Manager Pro⭐-----------------######################
st.markdown("---")
st.subheader("⭐Paper Sheet Stock Manager Pro⭐")
st.markdown("[⭐Paper Sheet Stock Manager Pro⭐ App](https://paper-sheet-stock-manager-pro-app-nxpye3ifupi.streamlit.app/)")
