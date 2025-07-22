# 🎬 IMDb Sentiment Classifier

This project is a simple and elegant machine learning app built with **scikit-learn** and **Streamlit**. It allows users to enter a movie review and get an instant prediction of whether the sentiment is **positive** or **negative**, along with a model-based rating estimate.

---

## 🚀 Demo

Enter a movie review like:

> “This movie was surprisingly powerful and emotional.”

Get an instant prediction like:

> ✅ **Prediction**: Positive  
> 🔢 **Confidence**: 0.93

---

## 🧠 Features

- ✅ Text classification using **TF-IDF + Logistic Regression**
- ✅ Interactive **Streamlit web app**
- ✅ Confidence score for each prediction
- ✅ Logging of all predictions with movie title + timestamp
- ✅ Summary rating based on all review predictions

---

## 📁 Project Structure

```
project/
├── aclImdb/               # Raw IMDb dataset (not pushed to Git)
├── app/
│   ├── streamlit_app.py   # Main web app
│   └── dashboard.py       # Optional model dashboard
├── data/
│   └── imdb_reviews.csv   # Final processed data (ignored in Git)
├── logs/
│   └── logs.csv           # Saved user inputs and predictions
├── model/
│   ├── model.joblib       # Trained Logistic Regression model
│   └── vectorizer.joblib  # TF-IDF vectorizer
├── notebook/
│   └── train_model.ipynb  # Jupyter notebook for model training
├── prepare_data.py        # Script to build dataset from raw .txt
├── requirements.txt
└── README.md
```

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/aibekgo/imdb-sentiment-classifier.git
cd imdb-sentiment-classifiers
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app/streamlit_app.py
```

Open in browser at: [http://localhost:8501](http://localhost:8501)

---

## 📊 Optional: View the model dashboard

```bash
streamlit run app/dashboard.py
```

It shows:
- Total number of reviews
- Positive/negative ratio
- Model rating (0–10)
- Top-reviewed movies
- Confidence distribution

---

## 📚 Dataset Info

The IMDb dataset used comes from [Stanford AI Lab](https://ai.stanford.edu/~amaas/data/sentiment/). It includes 50,000 movie reviews labeled as positive or negative, split into training and test sets.

---

## 🙌 Acknowledgements

- Dataset: IMDb Sentiment from Stanford
- Libraries: `pandas`, `scikit-learn`, `streamlit`, `joblib`, `matplotlib`, `seaborn`

---

## 📜 License

MIT License — use freely for learning or demo purposes.
