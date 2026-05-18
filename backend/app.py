#app.py
from flask import Flask
from nightscout import nightscout_data
from strava import get_strava_activity, list_recent_activities 

app = Flask(__name__)

@app.route("/nightscout")
def get_glucose():
    return nightscout_data("2026-03-08T08:30:00Z", "2026-03-08T12:00:00Z")

@app.route("/")
def get_activity():
    return get_activity_by_id("18533746143")

if __name__ == "__main__":
    app.run(debug=True)