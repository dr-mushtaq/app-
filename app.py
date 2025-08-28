import streamlit as st
import pandas as pd
import numpy as np

# --- App Title ---
st.title("📊 Simple Streamlit Demo App")

# --- Sidebar for User Input ---
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name", "Guest")
number = st.sidebar.slider("Pick a number", 1, 100, 50)

# --- Display Welcome Message ---
st.write(f"Hello, **{name}** 👋! You picked the number {number}.")

# --- Generate Random Data ---
st.subheader("Random Data Table")
data = pd.DataFrame(
    np.random.randn(10, 3),  # 10 rows, 3 columns of random numbers
    columns=["Column A", "Column B", "Column C"]
)
st.dataframe(data)

# --- Plot the Data ---
st.subheader("Line Chart of Random Data")
st.line_chart(data)

# --- End Note ---
st.success("✅ App is running successfully!")
