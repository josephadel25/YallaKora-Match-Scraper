# app.py
import streamlit as st
from scraper import scrape_matches
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="YallaKora Scraper", layout="centered")

st.title("⚽ YallaKora Match Scraper")
st.write("Scrape all football matches from YallaKora between two dates.")

# 📅 Date input
start_date = st.date_input("Start Date", value=datetime(2025, 1, 1))
end_date = st.date_input("End Date", value=datetime(2025, 1, 7))

# ⛔ Validation
if start_date > end_date:
    st.error("Start date must be before or equal to end date.")

# ▶️ Button to start scraping
elif st.button("🔍 Start Scraping"):
    with st.spinner(f"Scraping matches from {start_date} to {end_date}..."):
        csv_path = scrape_matches(start_date, end_date)
        df = pd.read_csv(csv_path)
        st.success("✅ Scraping completed!")
        st.dataframe(df)
        st.download_button("📥 Download CSV", data=df.to_csv(index=False).encode("utf-8-sig"),
                        file_name=os.path.basename(csv_path), mime="text/csv")
