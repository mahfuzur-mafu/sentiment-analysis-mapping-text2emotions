import streamlit as st
from textblob import TextBlob
import time

# App title & settings
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")
st.title("💬 Sentiment Analysis App")
st.markdown("---")

# Instructions
st.write("👉 Enter a sentence below and I'll analyze its **sentiment** for you.")

# Input box
user_input = st.text_area("✍️ Write your sentence here:", height=120)

# Analyze button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip():
        # Sentiment analysis
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Show result header
        st.subheader("📊 Analysis Result:")

        # Animated sentiment progress bar
        st.write("Sentiment Polarity Scale (-1 = Negative, +1 = Positive)")
        sentiment_bar = st.progress(0)
        sentiment_value = int((sentiment + 1) * 50)  # scale from -1..1 → 0..100

        for i in range(sentiment_value + 1):
            time.sleep(0.01)
            sentiment_bar.progress(i)

        # Display sentiment result
        if sentiment > 0:
            st.success(f"😊 Positive Sentiment\n\n**Score:** {sentiment:.2f}")
        elif sentiment < 0:
            st.error(f"☹️ Negative Sentiment\n\n**Score:** {sentiment:.2f}")
        else:
            st.info(f"😐 Neutral Sentiment\n\n**Score:** {sentiment:.2f}")

        # Animated subjectivity bar
        st.write("Subjectivity (0 = Objective, 1 = Subjective)")
        subj_bar = st.progress(0)
        subj_value = int(subjectivity * 100)

        for i in range(subj_value + 1):
            time.sleep(0.01)
            subj_bar.progress(i)

        # Explanation section
        st.markdown(
            """
            ### ℹ️ How it works:
            - **Positive (> 0):** Happy, optimistic, or favorable tone  
            - **Negative (< 0):** Sad, critical, or unfavorable tone  
            - **Neutral (= 0):** Objective or mixed tone  
            """
        )
    else:
        st.warning("⚠️ Please enter a sentence before analyzing.")
