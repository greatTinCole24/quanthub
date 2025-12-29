from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_flow(flow_data, user_prompt):
    system_prompt = (
        "You are a professional market analyst. "
        "Summarize unusual options activity clearly and concisely. "
        "Focus on actionable signals, not hype."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"""
Market Data:
{flow_data}

User Question:
{user_prompt}
"""
            }
        ],
        temperature=0.2,
        max_tokens=400
    )

    return response.choices[0].message.content
