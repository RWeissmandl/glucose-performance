#Strava
import requests
from datetime import datetime

from strava_secrets import (
    CLIENT_ID,
    CLIENT_SECRET,
    REFRESH_TOKEN,
    SHORT_LIVED_ACCESS_TOKEN,
    SHORT_LIVED_ACCESS_TOKEN_EXPIRY
)

def get_access_token():
    """Access tokens last for six hours.
    Check if access token has yet expired. 
    If yes: Use refresh token to get a short lived access token.
    If no: return current access token
    """
    #TODO:
    # if SHORT_LIVED_ACCESS_TOKEN_EXPIRY < datetime.now():
    #     return SHORT_LIVED_ACCESS_TOKEN
    url_swap_refresh_for_access = "https://www.strava.com/oauth/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }
    response = requests.post(url_swap_refresh_for_access, data=data)
    tokens = response.json()
    compare_refresh_token(tokens["refresh_token"])
    return tokens["access_token"]

def compare_refresh_token(new_refresh_token):
    """To request an access token, refresh token is used. 
    Refresh token may be updated during this process.
    Update refresh token if this happened.
    """
    if new_refresh_token != REFRESH_TOKEN:
        strava_secrets.REFRESH_TOKEN = new_refresh_token
    return

def get_activity_by_id(activity_id: str):

    # Use refresh token to get access token
    access_token = get_access_token()

    # Strava call using refresh tokens
    url_get_activity_by_id = f"https://www.strava.com/api/v3/activities/{activity_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"{url_get_activity_by_id}", headers=headers)
    return response.json()

def list_recent_activities():
    access_token = get_access_token()
    url_get_recent_activities = "https://www.strava.com/api/v3/activities"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"{url_get_recent_activities}", headers=headers)
    activities = response.json()
    names_of_recent_activies = {}
    for activity in activities:
        names_of_recent_activies[activity["name"]] = activity["id"]
    return names_of_recent_activies.keys()

def get_activity_id_from_name(activity_name: str):
    return names_of_recent_activies[activity_name]
