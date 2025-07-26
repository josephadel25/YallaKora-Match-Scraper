# scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import time, csv, os



def get_all_dates(start_date, end_date):
    """Generate all dates between start_date and end_date inclusive."""
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    return [(start_date + timedelta(days=i)).strftime("%#m/%#d/%Y")
            for i in range((end_date - start_date).days + 1)]


def scrape_matches(start_date, end_date, chromedriver_path="../chromedriver.exe"):
    output_file = f"yallakora_matches_from {start_date} to {end_date}.csv"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Time", "Champion", "Round", "Team A", "Team B",
                         "Team A Score", "Team B Score", "Team A Penalty Score",
                         "Team B Penalty Score", "Winner", "Match Status", "Match URL"])

    try:
        for day in get_all_dates(start_date , end_date):
            driver.get(f"https://www.yallakora.com/match-center?date={day}#days")
            time.sleep(2)
            matches = driver.find_elements(By.CLASS_NAME, "matchCard")
            results = []
            for match in matches:
                try:
                    round_ = match.find_element(By.CLASS_NAME, "date").text.strip()
                    champion = match.find_element(By.CSS_SELECTOR, ".title h2").text.strip()
                    teamA = match.find_element(By.CLASS_NAME, "teamA").text.strip()
                    teamB = match.find_element(By.CLASS_NAME, "teamB").text.strip()
                    resultq = match.find_element(By.CLASS_NAME, "MResult").text.strip().split()
                    scoreA, scoreB = resultq[0], resultq[2]
                    match_state = "Not Start" if scoreA == '-' or scoreB == '-'  else "Completed"
                    time_str = match.find_element(By.CLASS_NAME, "time").text.strip()
                    try:
                        peln_score = match.find_element(By.CLASS_NAME, "penaltyRes").text.strip().split()
                        peln_score = [x.replace("(", "").replace(")", "") for x in peln_score]
                        scoreA_peln, scoreB_peln = peln_score[0], peln_score[2]
                    except:
                        scoreA_peln = scoreB_peln = "N/A"

                    if scoreA != '-' and scoreB != '-':
                        if scoreA_peln == "N/A":
                            winner = teamA if scoreA > scoreB else (teamB if scoreB > scoreA else "تعادل")
                        else:
                            winner = teamA if scoreA_peln > scoreB_peln else teamB
                    else:
                        winner = "N/A"

                    match_link = match.find_element(By.TAG_NAME, "a").get_attribute("href")
                    results.append([day, time_str, champion, round_, teamA, teamB,
                                    scoreA, scoreB, scoreA_peln, scoreB_peln,
                                    winner, match_state, match_link])
                except Exception as e:
                    continue
            with open(output_file, "a", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerows(results)
    finally:
        driver.quit()

    return output_file
