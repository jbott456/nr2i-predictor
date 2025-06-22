import requests
from datetime import date

today = date.today().strftime("%Y%m%d")
url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={today}"
resp = requests.get(url)
data = resp.json()

print("Status code:", resp.status_code)
print("Number of games found:", len(data.get("events", [])))

