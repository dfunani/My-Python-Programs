import requests
import json
from decouple import config
from models import Club
import sys


def Main():
    apiKey = config('apikey')
    teamsApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/teams/'
    seasonApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/seasons'
    matchesApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/matches'
    jsonFilename = "matches"

    # Checking existing teams - standard is 20 teams
    current_clubs = Club().FetchAll()
    print(f"List of existing teams {current_clubs}")

    # Check what the current season is
    seasons = GetData_ByAPI(
        seasonApiEndpoint, apiKey, (("league_id", "237"),))
    current_season = list(
        filter(lambda x: x['is_current'] == 1, seasons['result']['data']))[0]
    print(f"New season start date: {current_season['start_date']}")

    # Get matches for given season id
    matches = GetData_ByAPI(matchesApiEndpoint, apiKey,
                            (("season_id", current_season['season_id']),))
    print(str(len(matches['result']['data'])) + " matches fetched")

    # Using the existing matches, create a list of the latest epl teams
    latest_clubs = Confirm_LatestTeams(matches['result']['data'])
    toBeDeleted = list(
        filter(lambda x: not x in latest_clubs['result'], current_clubs['result']))
    print(f"{len(toBeDeleted)} teams to be removed from the database {toBeDeleted}")
    toBeUpdated = list(
        filter(lambda x: not x in current_clubs['result'], latest_clubs['result']))
    print(f"{len(toBeUpdated)} teams to be added to the database {toBeUpdated}")

    if toBeUpdated:
        for item in toBeUpdated:
            res = GetData_ByAPI(teamsApiEndpoint + str(item), apiKey)
            if res['result']['data']:
                StoreData_DB(res['result']['data'])

    if toBeDeleted:
        Delete_Teams(toBeDeleted)

    Update_Matches(matches)
    exit(
        f"Completed updating the database with Sports Api Data for the {current_season['name']} season")


def Confirm_LatestTeams(obj: list):
    result = set()
    for item in obj:
        result.add(item['home_team']['team_id'])
        result.add(item['away_team']['team_id'])
    return {'status': 'success', 'code': "JSON_DUMP", 'result': result}


def StoreData_DB(objs: dict) -> dict:
    club = Club(
        team_id=objs['team_id'],
        name=objs['name'],
        short_code=objs['short_code'],
        common_name=objs['common_name'],
        logo=objs['logo'],
    )
    club.Add()
    return {'status': 'success', 'code': "JSON_DUMP", 'result': objs}


def GetData_ByAPI(endpoint: str, apikey: str, params: tuple = ()) -> dict:
    headers = {
        "apikey": apikey}

    response = requests.get(
        endpoint, headers=headers, params=params)

    return {'status': 'success', 'code': response.status_code, 'result': response.json()}


def StoreData_JSON(obj: dict, fileName: str) -> dict:
    with open(f'Static/{fileName}.json', 'w') as objFile:
        json.dump(obj, objFile, indent=4)
    return {'status': 'success', 'code': "JSON_DUMP", 'result': obj}


def GetData_ByJSON(filename: str) -> str:
    with open(f'Static/{filename}.json', 'r') as jsonObjFile:
        obj = json.load(jsonObjFile)
    return {'status': 'success', 'code': "JSON_DUMP", 'result': obj}


if __name__ == "__main__":
    Main()
