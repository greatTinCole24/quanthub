import streamlit as st
from data import fetch_flow_data
from llm import analyze_flow
from auth import require_login

st.set_page_config(
    page_title="Flow Chat",
    layout="wide"
)

require_login()

st.title("📈 Flow Chat Assistant")

with st.spinner("Fetching market data..."):
    flow_data = fetch_flow_data()

st.subheader("Ask about today's market")
user_prompt = st.text_input(
    "Example: What unusual options activity stands out today?"
)

if st.button("Analyze") and user_prompt:
    with st.spinner("Analyzing..."):
        answer = analyze_flow(flow_data, user_prompt)

    st.markdown("### 🧠 Analysis")
    st.write(answer)
