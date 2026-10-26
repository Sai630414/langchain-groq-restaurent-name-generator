
import streamlit as st
from langchainhelper import generate_name_and_items

st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
)

st.title("Restaurant Name & Menu Generator")

cuisine = st.selectbox(
    "Choose a cuisine",
    [
        "Indian", "Italian", "Mexican", "Chinese",
        "Japanese", "Thai", "French",
        "Mediterranean", "American","Telugu"
    ],
)

if st.button("Generate"):
    try:
        with st.spinner("Creating your restaurant idea..."):
            result = generate_name_and_items(cuisine)

        st.subheader(result["restaurant_name"])
        st.write("### Menu Items")

        for item in result["menu_items"]:
            st.write(f"- {item}")

    except Exception as exc:
        st.error(f"Unable to generate results: {exc}")
