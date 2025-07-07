import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("IMDB Movie Review Sentiment Dashboard")

df = pd.read_csv('data/reviews_with_sentiment.csv')
st.subheader("Sample Data")
st.write(df.head())

st.subheader("Sentiment Distribution")
counts = df['sentiment'].value_counts()
st.bar_chart(counts)

st.subheader("Ratings vs Sentiment")
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    st.write(df.groupby('sentiment')['rating'].mean())
