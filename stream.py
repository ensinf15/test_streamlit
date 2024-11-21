# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:58:43 2024

@author: admin
"""

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Title for the app
st.title("Simple Streamlit App")

# Subheader
st.subheader("Exploring Streamlit Basics")

# Add text
st.write("This is a basic Streamlit app to demonstrate its capabilities.")

# Create a slider for user input
number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")

# Generate random data
data = np.random.randn(100, 2)
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])

# Display dataframe
st.write("Here is a random dataset:")
st.dataframe(df)

# Line chart
st.write("Line chart of the data:")
st.line_chart(df)

# Interactive input box
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar!")

# Checkbox
if st.checkbox("Show raw data"):
    st.write(df)

# Selectbox
option = st.selectbox("Choose a column to highlight", df.columns)
st.write(f"You selected {option}.")

