import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# --- Title --- #
st.set_page_config(page_title="Sovereign Risk Scoring App")
st.title("\U0001F4CA Sovereign Risk Analyzer")

# --- Static Scores for Demo --- #
COUNTRY_RISK_SCORES = {
    "India": 78,
    "Argentina": 42,
    "Germany": 90,
    "Pakistan": 35,
    "Nigeria": 40,
    "United States": 88,
    "Greece": 50,
    "Japan": 75,
    "Brazil": 60,
    "Myanmar": 30
}

# --- Load FLAN-T5 Model --- #
@st.cache_resource(show_spinner=False)
def load_model():
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# --- Country Selection --- #
country = st.selectbox("Select a country to evaluate:", list(COUNTRY_RISK_SCORES.keys()))

# --- Generate Prompt & Response --- #
if st.button("Generate Sovereign Risk Report"):
    with st.spinner("Analyzing with LLM..."):
        score = COUNTRY_RISK_SCORES[country]
        prompt = f"Give a brief sovereign risk analysis for {country} based on its risk score of {score}/100."

        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_new_tokens=100)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Display Results
        st.subheader(f"Risk Score for {country}: {score}/100")
        st.markdown("---")
        st.write(decoded)
        st.markdown("---")
        st.info("Note: Score is based on mock logic and should be replaced with ML predictions in production.")
