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
toprow.link_button("Home", type="primary", use_container_width=True, url="https://mawae.net", help="Go to the Home page.")

with bottom():
    st.markdown("---")
    bottomrow = row(6, vertical_align="center", gap="medium")
    bottomrow.markdown("For questions, please reach out on Discord @masternox")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.link_button("Private Dashboard", type="secondary", use_container_width=True, url="https://home.mawae.net", help="Login to the private MawaeNet.") # When moved over to its own url, this will be substituted in.
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.markdown("")
    bottomrow.link_button("Forgot Password?", type="tertiary", use_container_width=True, url="https://account.mawae.net/reset-password/step1", help="Reset your password.")

pg = st.navigation(pages=[st.Page("1_MawaeNet.py"), st.Page("2_Alyrian_Cipher.py"), st.Page("3_NPC_Generator.py"), st.Page("4_Level_Distribution.py")], position="sidebar", expanded=False)
pg.run()