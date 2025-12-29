import requests
import streamlit as st

@st.cache_data(ttl=10)  # refresh every 10 seconds
def fetch_flow_data():
    url = "https://api.unusualwhales.com/api/option-flow"
    headers = {
        "Authorization": f"Bearer {st.secrets['UW_API_KEY']}"
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()
