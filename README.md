# How does blood glucose impact performance?

Overlay activities with blood glucose data. I set this up so I can:

1. Select a recent activity, or choose activity by ID. GUI displays a list of 30 most recent activities by name. If older activity is needed, find ID manually and select activity by ID
2. Display activity on a map. This is just for convenience.

## Compare blood glucose and performance per lap. 

I do this by:

A. Displaying a bar chart of blood glucose per lap
B. Displaying a bar chart of speed per lap

Optionally: 
C. Displaying a bar chart of power per lap if activity has power (EG Cyling)
D. Displaying a bar chart of heart rate if activity has HR. 

This can be overlayed, or seen side by side. 

## APIs

- Activities are making a call to Strava 
- Blood glucose data is making a call to the Nightscout API. 

## Dependencies 

Dependencies are installed in requirements.txt. Run `pip install -r requirements.txt` to install. To run the app, run, ensure the venv has been activated with `source .venv/bin/activate` and then run `python3 app.py` in the `backend` folder.

For reference, to set up a venv: 
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install <dependencies>`
- `pip freeze > requirements.txt`

### To Do: Use UV instead

This project will use UV to manage dependencies. To run, ensure correct folder (/backend) and run `uv run python3 app.py`. If trouble, run `uv sync`.

For reference, uv was set up as follows:
- Install uv (can use curl as stated on their website)
- uv init
- uv add <dependencies>

## Strava Authorisation 

Strava uses OAuth2 for authorisation. [Strava Documentation](https://developers.strava.com/docs/getting-started/) sets out how to:
1. Set up a Strava developer account
2. Gain a valid refresh token with the correct scopes

Refresh tokens are used to acquire short-lived access tokens. Access tokens are used for each activity request. Note:
1. Short lived access tokens are reused for its six hour duration before expiry
2. Each time a request for access tokens is made, the refresh token may get updated. Only updated refresh tokens are valid. 

### Strava Secrets

Strava secrets are saved in a `strava_secrets.py` file containing:
```
CLIENT_ID=
STRAVA_CLIENT=
STRAVA_REFRESH_TOKEN=
SHORT_LIVED_ACCESS_TOKEN,
SHORT_LIVED_ACCESS_TOKEN_EXPIRY
```
