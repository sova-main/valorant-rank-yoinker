import json, time
from valclient.client import Client
from player import Player
from game import Game

running = True
seenMatches = []

print('Valorant Stream Yoinker by https://github.com/deadly')

with open('settings.json', 'r') as f:
    data = json.load(f)
    ranBefore = data['ran']
    region = data['region']
    stateInterval = data['stateInterval']
    twitchReqDelay = data['twitchReqDelay']
    skipTeamPlayers = data['skipTeamPlayers']
    skipPartyPlayers = data['skipPartyPlayers']

while True:
    try:
        if (ranBefore == False):
            region = input("Enter your region: ").lower()
            client = Client(region=region)
            client.activate()

            with open('settings.json', 'w') as f:
                    data['ran'] = True
                    data['region'] = region
                    json.dump(data, f, indent=4)
        else:
            client = Client(region=region)
            client.activate()
            break
    except Exception as e:
        print("Client Activation Error",e, "\nMaybe restart client...")
        time.sleep(10)

        
print("Waiting for a match to begin")
while (running):
    try:
        c_presence = client.fetch_presence(client.puuid)
        sessionState = c_presence['sessionLoopState']
        c_coregame = client.coregame_fetch_player()
        matchID = c_coregame['MatchID']

        if (sessionState == "PREGAME" or "INGAME" and matchID not in seenMatches):
            print('-'*55)
            seenMatches.append(matchID)
            matchInfo = client.coregame_fetch_match(matchID)
            print(f"Match detected: {matchInfo['MatchmakingData']['QueueID']}")
            players = []
            client.fetch_account_xp
            for player in matchInfo['Players']:
                if (client.puuid == player['Subject']):
                    localPlayer = Player(
                        client=client,
                        puuid=player['Subject'].lower(),
                        agentID=player['CharacterID'].lower(),
                        incognito=player['PlayerIdentity']['Incognito'],
                        team=player['TeamID'],
                        level=player['PlayerIdentity']['AccountLevel']
                    )
                else:
                    players.append(Player(
                        client=client,
                        puuid=player['Subject'].lower(),
                        agentID=player['CharacterID'].lower(),
                        incognito=player['PlayerIdentity']['Incognito'],
                        team=player['TeamID'],
                        level=player['PlayerIdentity']['AccountLevel']
                    ))
            local_player_team = localPlayer.team

            print("Teammates:")
            for player in players:
                if player.team == local_player_team:
                    print(f"{player.agent} - {player.full_name} - {player.account_level} - {player.rank}")

            
            print("\nEnemies:")
            for player in players:
                if player.team != local_player_team:
                    print(f"{player.agent} - {player.full_name} - {player.account_level} - {player.rank}")

    except Exception as e:
        if ("core" not in str(e)) and ("NoneType" not in str(e)):
            print("An error occurred:", e)

    time.sleep(stateInterval)
