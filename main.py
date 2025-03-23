import streamlit as st
import requests
import pandas as pd
import numpy as np

def load_data():
    url = "https://x8ki-letl-twmt.n7.xano.io/api:rcbz2K5n/final_bid_data"
    data = requests.get(url)
    return data.json()

st.header = "Tender Information"

data = load_data()
st.dataframe(data)