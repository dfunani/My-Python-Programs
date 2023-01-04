import requests
import json
from decouple import config
from models import Club
import sys


def Main():
    apiKey = config('apikey')
    apiParams = (("country_id", "42"), )
    teamsApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/teams'
    seasonApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/seasons'
    matchesApiEndpoint = 'https://app.sportdataapi.com/api/v1/soccer/teams'
    jsonFilename = "matches"

    # Checking existing teams - standard is 20 teams
    current_clubs = Club().FetchAll()
    print(f"List of existing teams {current_clubs}")

    # Check what the current season is
    seasons = GetData_ByAPI(
        seasonApiEndpoint, apiKey, (("league_id", "237"),))
    current_season = list(
        filter(lambda x: x['is_current'] == 1, seasons['result']['data']))[0]

    exit(
        f"Completed updating the database with Sports Api Data for {current_season['name']}")


def StoreData_DB(objs: list) -> dict:
    for obj in objs:
        club = Club(
            team_id=obj['team_id'],
            name=obj['name'],
            short_code=obj['short_code'],
            common_name=obj['common_name'],
            logo=obj['logo'],
            country_id=obj['country']['country_id'],
            country_name=obj['country']['name'],
            country_code=obj['country']['country_code'],
            continent=obj['country']['continent']
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
