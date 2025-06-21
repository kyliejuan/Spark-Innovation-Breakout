import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Title
st.title("Patient Blood Pressure Tracker")

# Patient Info
st.sidebar.header("Patient Information")
name = st.sidebar.text_input("Name", "John Doe")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=45)
sex = st.sidebar.selectbox("Sex", ["Male", "Female", "Other"])

# Generate dummy blood pressure data
dates = [datetime.today() - timedelta(days=i) for i in range(10)][::-1]
systolic = np.random.randint(110, 140, size=10)
diastolic = np.random.randint(70, 90, size=10)

data = pd.DataFrame({
    "Date": dates,
    "Systolic": systolic,
    "Diastolic": diastolic
})

# Display data
st.subheader(f"Blood Pressure Readings for {name}")
st.dataframe(data)

# Plot
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Systolic"], label="Systolic", marker="o")
ax.plot(data["Date"], data["Diastolic"], label="Diastolic", marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Pressure (mmHg)")
ax.set_title("Blood Pressure Over Time")
ax.legend()
plt.xticks(rotation=45)

st.pyplot(fig)
