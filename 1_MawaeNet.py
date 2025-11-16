import streamlit as st
from streamlit_extras.row import row

st.markdown("<h1 style='text-align: center;'>MawaeNet</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Below you will find a list of tools and features available on MawaeNet.</h5>", unsafe_allow_html=True)

ButtonsRow1 = row(3, vertical_align="center", gap="medium")
if ButtonsRow1.button("Alyrian Cipher", type="secondary", use_container_width=True, help="Translate text to the fictional Alyrian language."):
    st.switch_page("2_Alyrian_Cipher.py")
if ButtonsRow1.button("NPC Generator", type="secondary", use_container_width=True, help="Alyrian NPC Generator."):
    st.switch_page("3_NPC_Generator.py")
if ButtonsRow1.button("Population Level Distribution", type="secondary", use_container_width=True, help="Alyrian Population Level Distribution."):
    st.switch_page("4_Level_Distribution.py")