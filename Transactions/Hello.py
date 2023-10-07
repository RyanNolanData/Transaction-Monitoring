import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

#image = Image.open('Final_Periodic_App/Stax_Banner.png')

#st.image(image)

st.write("# Welcome to Paypal Reviews")

st.markdown(
    """
    These 2 Apps Help us review transactions from a customer

    **👈 Select an app from the sidebar** to get started

    If an app isn't working correctly, reach out to Ryan Nolan Data

    ### Want to learn more?
    - Check out The [YouTube Video](#)
    - Check out his [Twitter](https://twitter.com/RyanNolanData)

"""
)