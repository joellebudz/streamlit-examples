import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Diabetes Dataset Dashboard")
df = pd.read_csv("https://storage.googleapis.com/scsu-data-science/diabetes_nan.csv")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)

st.markdown('---')
st.subheader("Glucose Levels by Diabetes Outcome")

outcome = st.radio(
    "Select patient group:",
    ("Non-Diabetic (Outcome = 0)", "Diabetic (Outcome = 1)"))

if outcome == "Non-Diabetic (Outcome = 0)":
    filtered_df = df[df["Outcome"] == 0]
else:
    filtered_df = df[df["Outcome"] == 1]

filtered_df = filtered_df.dropna(subset=["Glucose"])

fig = plt.figure()
ax = fig.add_subplot()
ax.hist(filtered_df["Glucose"], bins=15)
ax.set_xlabel("Glucose Level")
ax.set_ylabel("Frequency")

if outcome == "Non-Diabetic (Outcome = 0)":
    ax.set_title("Distribution of Glucose Levels - Non-Diabetic")
else:
    ax.set_title("Distribution of Glucose Levels - Diabetic")

st.pyplot(fig)
