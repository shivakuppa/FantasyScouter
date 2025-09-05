import os
from dotenv import load_dotenv

from espn_api.football import League, Player

load_dotenv()
league_id = int(os.getenv("LEAGUE_ID"))
year = int(os.getenv("YEAR"))
espn_s2 = os.getenv("ESPN_S2")
swid = os.getenv("SWID")
league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

# print(league)

# print(league.box_scores(1))

box_scores = league.box_scores(1)

# print(box_scores[0].home_team.roster)

players = box_scores[0].home_team.roster

cdlamb = players[0]

# print(cdlamb.stats)

cdlambid = cdlamb.playerId

# print(cdlambid)

# print(len(league.free_agents(size=10000)))

for player in league.free_agents(size=10000):
    if "kyle pitts" in player.name.lower():
        # print("got kyle", player)
        
        # data = league.espn_request.get_player_card(player.playerId, league.finalScoringPeriod)
        print(player.stats)