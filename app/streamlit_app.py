import streamlit as st

# Set page config — must be first Streamlit call
st.set_page_config(page_title="IMDb Sentiment App", page_icon="🎬")

# Then all other imports
import joblib
import pandas as pd
import os
from datetime import datetime


# Load model and vectorizer
@st.cache_resource
def load_artifacts():
    model = joblib.load("../model/model.joblib")
    vectorizer = joblib.load("../model/vectorizer.joblib")
    return model, vectorizer

model, vectorizer = load_artifacts()

# -----------------------------
# ✍️ Section 1: Prediction form
# -----------------------------
st.header("💬 Review Sentiment Prediction")

movie_title = st.text_input("🎞 Movie title (optional):")
user_input = st.text_area("✍️ Write your review here:", height=200)

if st.button("🔍 Predict"):
    if user_input.strip():
        X = vectorizer.transform([user_input])
        pred = model.predict(X)[0]
        proba = model.predict_proba(X)[0][pred]

        if pred == 1:
            label = "🌟 Positive"
            emoji = "😄"
        else:
            label = "💔 Negative"
            emoji = "😡"

        st.subheader(f"Prediction: {label} {emoji}")
        st.write(f"Confidence: **{proba:.2f}**")

        # Save to logs
        log = pd.DataFrame([{
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'movie_title': movie_title.strip(),
            'review': user_input.strip(),
            'prediction': 'positive' if pred == 1 else 'negative',
            'confidence': round(proba, 3)
        }])
        os.makedirs("../logs", exist_ok=True)
        log_path = "../logs/logs.csv"
        if os.path.exists(log_path):
            log.to_csv(log_path, mode='a', header=False, index=False)
        else:
            log.to_csv(log_path, index=False)

        st.success("✅ Logged to logs.csv")
    else:
        st.warning("Please write a review first.")

if st.button("🧹 Clear"):
    st.experimental_rerun()

# -----------------------------
# 📊 Section 2: Dataset Summary
# -----------------------------
st.header("📊 Dataset-wide Sentiment Stats")

try:
    df = pd.read_csv("../data/imdb_reviews.csv")
    X_all = vectorizer.transform(df['review'])
    df['model_prediction'] = model.predict(X_all)

    total_reviews = len(df)
    pos_reviews = (df['model_prediction'] == 1).sum()
    neg_reviews = (df['model_prediction'] == 0).sum()
    model_rating = round(pos_reviews / total_reviews * 10, 1)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews", total_reviews)
    col2.metric("👍 Positive", pos_reviews)
    col3.metric("👎 Negative", neg_reviews)

    st.markdown(f"### 🎬 Estimated overall rating: **{model_rating} / 10**")

except Exception as e:
    st.warning("ℹ️ Cannot load full dataset. Model-wide stats unavailable.")
    st.exception(e)

