import streamlit as st

st.set_page_config(
    page_title="補助金診断ツール",
    page_icon="💰",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "Thanks for using this app!"
    }
)

st.title("補助金診断ツール")

left, middle, right = st.columns(3)
if middle.button("クイック診断", type="primary"):
    st.switch_page("pages/candidates.py")