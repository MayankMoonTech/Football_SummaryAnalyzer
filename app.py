import streamlit as st

from analytics.load_data import load_match_data
from analytics.metrics import calculate_metrics
from analytics.xg_model import calculate_xg

from utils.prompt_builder import build_prompt
from llm.ollama_client import generate_analysis


st.title("AI Football Tactical Analyst")

df = load_match_data()

metrics = calculate_metrics(df)

st.subheader("Match Metrics")
st.write(metrics)

if st.button("Generate Tactical Analysis"):

    prompt = build_prompt(metrics)

    analysis = generate_analysis(prompt)

    st.subheader("AI Tactical Report")

    st.write(analysis)