import streamlit as st
import emailgenerator


def run_app():
    st.set_page_config(
        page_title="GiniEmail",
        page_icon="✉️",
        layout="centered"
    )
    
    # Run the Streamlit app
    emailgenerator.main()

if __name__ == "__main__":
    run_app()
