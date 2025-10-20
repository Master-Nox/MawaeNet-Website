import streamlit as st
from streamlit_extras.row import row

st.markdown("<h1 style='text-align: center;'>MawaeNet</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Below you will find a list of tools and features available on MawaeNet.</h5>", unsafe_allow_html=True)

ButtonsRow1 = row(3, vertical_align="center", gap="medium")
if ButtonsRow1.button("Alyrian Cipher", type="secondary", use_container_width=True, help="Translate text to the fictional Alyrian language."):
    st.switch_page("2_Alyrian_Cipher.py")
ButtonsRow1.button("WIP", type="secondary", use_container_width=True, help="Work in progress.", key="wip1")
    # st.switch_page("2_Alyrian_Cipher.py")
ButtonsRow1.button("WIP", type="secondary", use_container_width=True, help="Work in progress.", key="wip2")
    # st.switch_page("2_Alyrian_Cipher.py")