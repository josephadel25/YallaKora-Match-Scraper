# ⚽ YallaKora Match Scraper

A simple and effective web scraping app to extract football match data from [YallaKora](https://www.yallakora.com/match-center) by date range — built with **Streamlit**, **Selenium**, and **Pandas**.

---

## 📸 Demo

![App Screenshot](screenshot.png) <!-- Replace with your actual screenshot if available -->

---

## 🚀 Features

- Select **start and end date** to scrape matches
- Extract team names, scores, penalty scores, winners, etc.
- Export the scraped data as a **CSV**
- Preview results directly in the web app
- No need to download `chromedriver` manually — handled automatically

---

## 🛠 Tech Stack

- `Python 3.10+`
- `Streamlit` – interactive frontend
- `Selenium` – for browser automation
- `webdriver-manager` – for auto-managing ChromeDriver
- `Pandas` – for table formatting and CSV export

---

## 📂 Project Structure

📁 yallakora-scraper/
│
├── app.py # Streamlit app UI
├── scraper.py # Scraping logic
├── requirements.txt # Dependencies
└── README.md # Project description

---

## ⚙️ Installation & Usage

### 🔧 1. Clone & Install

```bash
git clone https://github.com/yourusername/yallakora-scraper.git
cd yallakora-scraper
pip install -r requirements.txt


### ▶️ 2. Run the App

streamlit run app.py
```
## 📦 Output
The scraped data is saved as a CSV file, containing the following columns:

Date, Time, Champion, Round, Team A, Team B,
Team A Score, Team B Score, Team A Penalty Score,
Team B Penalty Score, Winner, Match Status, Match URL

## ✅ To-Do / Future Features

 Add team filtering

 Match statistics (e.g., goals, cards)

 Auto-run on schedule

 Arabic UI support

🤝 Contributing
Pull requests are welcome. If you'd like to suggest features or report bugs, please open an issue.

📄 License
MIT License — free for personal and commercial use.
