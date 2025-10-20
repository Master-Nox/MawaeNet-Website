import streamlit as st
from streamlit_extras.bottom_container import bottom
from streamlit_extras.row import row

st.set_page_config(
    page_title="MawaeNet",
    page_icon="🌐",
    layout="wide"
)

st.markdown(
    """
        <style>
                .stAppHeader {
                    background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                    visibility: visible;  /* Ensure the header is visible */
                }

               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

# st.logo(image=r"MawaeNet.png", size="large", link="https://mawae.net")

toprow = row(6, vertical_align="center", gap="medium")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
toprow.markdown("")
if toprow.button("Home", help="Go to the Home page.", type="primary", use_container_width=True):
    st.switch_page("1_MawaeNet.py")

with bottom():
    st.markdown("---")
    bottomrow = row(6, vertical_align="center", gap="medium")
    bottomrow.markdown("For questions, please reach out on Discord @masternox")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.link_button("Login", type="secondary", use_container_width=True, url="https://home.mawae.net", help="Login to the private MawaeNet.")

pg = st.navigation(pages=[st.Page("1_MawaeNet.py"), st.Page("2_Alyrian_Cipher.py"), st.Page("3_NPC_Generator.py")], position="sidebar", expanded=False)
pg.run()