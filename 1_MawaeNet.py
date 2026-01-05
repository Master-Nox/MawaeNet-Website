import streamlit as st
from streamlit_extras.row import row

st.markdown("<h1 style='text-align: center;'>MawaeNet</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Tools and features available on the public MawaeNet.</h5>", unsafe_allow_html=True)

ButtonsRow1 = row(3, vertical_align="center", gap="medium")
if ButtonsRow1.button("Alyrian Cipher", type="secondary", use_container_width=True, help="Translate text to the fictional Alyrian language."):
    st.switch_page("2_Alyrian_Cipher.py")
if ButtonsRow1.button("NPC Generator", type="secondary", use_container_width=True, help="Alyrian NPC Generator."):
    st.switch_page("3_NPC_Generator.py")
#ButtonsRow1.button("WIP", type="secondary", use_container_width=True, help="Work in progress.", key="wip2")
    # st.switch_page("2_Alyrian_Cipher.py")
#if ButtonsRow1.button("Home", type="secondary", use_container_width=True, help="Go to the Home page.", key="home"):
#    st.switch_page("100_Home.py")
if ButtonsRow1.button("Population Level Distribution", type="secondary", use_container_width=True, help="Alyrian Population Level Distribution."):
    st.switch_page("4_Level_Distribution.py")
