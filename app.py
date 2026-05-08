import streamlit as st
from langchain_community.llms import Ollama
from pydantic import BaseModel
import json

# Load local LLM
llm = Ollama(model="llama3.1")

st.title("AI Incident Response Agent")

uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["txt", "log"]
)

if uploaded_file:

    logs = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Logs")
    st.code(logs)

    prompt = f"""
    You are an expert AI Site Reliability Engineer.

    Analyze the following logs.

    Return:
    - Severity Level
    - Incident Summary
    - Root Cause
    - Recommended Remediation

    Logs:
    {logs}
    """

    response = llm.invoke(prompt)

    st.subheader("AI Incident Analysis")
    st.write(response)

    # Simple severity tagging
    if "CRITICAL" in logs:
        st.error("Severity: CRITICAL")
    elif "ERROR" in logs:
        st.warning("Severity: HIGH")
    else:
        st.success("Severity: NORMAL")
        