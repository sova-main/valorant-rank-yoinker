import requests, time, random


Tiers =  {
    0: "UN", #UNRATED
    1: "UNK1", #UNKOWN
    2: "UNK2",
    3: "Iron 1",
    4: "Iron 2",
    5: "Iron 3",
    6: "B1",
    7: "B2",
    8: "B3",
    9: "S1",
    10: "S2",
    11: "S3",
    12: "G1",
    13: "G2",
    14: "G3",
    15: "P1",
    16: "P2",
    17: "P3",
    18: "D1",
    19: "D2",
    20: "D3",
    21: "A1",
    22: "A2",
    23: "A3",
    24: "Imm1",
    25: "Imm2",
    26: "Imm3",
    27: "Rad",
}

proxy_list = []
x = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&simplified=true', stream=True)
for y in x.iter_lines():
    if y: 
        proxy_list.append({'http': f"socks4://{y.decode().strip()}"})
        


agentMap = {}

try:
    reqAgents = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true")
    reqAgents = reqAgents.json()
    Agents = reqAgents['data']
    for agent in Agents:
        agentMap[agent['uuid']] = agent['displayName']
    print("Finished Updating Agents")
except Exception as e:
    print(e)
        
class Player:
    def __init__(self, client, puuid, agentID, incognito, team, level):
        self.client = client
        self.puuid = puuid
        self.agent = agentMap[agentID]
        self.incognito = incognito
        self.team = self.side(team)
        self.account_level = level
        self.name = self.filter_name(self.set_name(puuid).split('#')[0])

        self.full_name = self.set_name(puuid)
        self.rank = self.set_rank(puuid)
        self.tag = self.set_name(puuid).split('#')[1]
        self.possibleNames = self.find_possible_names()

    def side(self, color):
        if (color == "Blue"):
            return "Defending"
        else:
            return "Attacking"
    
    
    def set_rank(self, puuid):
        playerMMR = self.client.fetch_mmr(puuid)
        current_rank = playerMMR['LatestCompetitiveUpdate']['TierAfterUpdate']
        player_rank_latest = Tiers.get(current_rank)

        previous_ranks_str = player_rank_latest+""
        try:
            previous_ranks = playerMMR['QueueSkills']['competitive']['SeasonalInfoBySeasonID']
            skip_first = dict(list(previous_ranks.items())[1:])
            for prev in skip_first: #skip first
                prev_season_info = previous_ranks[prev]
                previous_ranks_str += "|"+Tiers.get(prev_season_info['Rank'])
        except:
            pass
        # 
        # rr remaining for next rank = playerMMR['LatestCompetitiveUpdate']['RankedRatingAfterUpdate']
        # prev game rr =  playerMMR['LatestCompetitiveUpdate']['RankedRatingEarned']
        return previous_ranks_str

    def set_name(self, puuid):
        playerData = self.client.put(
            endpoint="/name-service/v2/players", 
            endpoint_type="pd", 
            json_data=[puuid]
        )[0]
        return f"{playerData['GameName']}#{playerData['TagLine']}"

    def filter_name(self, name):
        if ('twitch' in name):
            return name.replace('twitch', '').strip()
        if ('ttv' in name):
            return name.replace('ttv', '').strip()
        return name
    
    def find_possible_names(self):
        self.name_u = self.name.replace(' ', '_')
        self.name = self.name.replace(' ', '')

        return list(set([
            self.name,
            self.name + self.tag,
            self.name_u,
            self.name_u + self.tag,
            self.tag + self.name,
            self.tag + self.name_u,
            f"{self.name}_{self.tag}",
            f"{self.tag}_{self.name}",
            f"{self.name_u}_{self.tag}",
            f"{self.tag}_{self.name_u}",
        ]))

    def is_live(self, delay):
        for name in self.possibleNames:
            time.sleep(delay)
            state = requests.get(f'https://twitch.tv/{name}', proxies=random.choice(proxy_list)).content.decode('utf-8')
            if ('isLiveBroadcast' in state):
                return name
        return False
            
        
