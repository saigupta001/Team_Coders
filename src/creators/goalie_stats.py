def create_goalie_stats(player_info,info,team_info,res_goalie_stats):
    new_goalie_stats = GoalieStats()
    new_goalie_stats.playerId = player_info["person"]["id"]
    new_goalie_stats.gamePk = info["gamePk"]
    new_goalie_stats.position = player_info["position"]["code"]
    new_goalie_stats.team = team_info["team"]["id"]

    new_goalie_stats.timeOnIce = convert_string_to_time(res_goalie_stats["timeOnIce"])
    new_goalie_stats.assists = res_goalie_stats["assists"]
    new_goalie_stats.goals = res_goalie_stats["goals"]
    new_goalie_stats.pim = res_goalie_stats["pim"]
    new_goalie_stats.shots = res_goalie_stats["shots"]
    new_goalie_stats.saves = res_goalie_stats["saves"]
    new_goalie_stats.powerPlaySaves = res_goalie_stats["powerPlaySaves"]
    new_goalie_stats.shortHandedSaves = res_goalie_stats["shortHandedSaves"]
    new_goalie_stats.evenSaves = res_goalie_stats["evenSaves"]
    new_goalie_stats.shortHandedShotsAgainst = res_goalie_stats["shortHandedShotsAgainst"]
    new_goalie_stats.evenShotsAgainst = res_goalie_stats["evenShotsAgainst"]
    new_goalie_stats.powerPlayShotsAgainst = res_goalie_stats["powerPlayShotsAgainst"]
    new_goalie_stats.decision = res_goalie_stats["decision"] if "decision" in res_goalie_stats else None
    new_goalie_stats.savePercentage = res_goalie_stats["savePercentage"] if "savePercentage" in res_goalie_stats else None
    new_goalie_stats.powerPlaySavePercentage = res_goalie_stats["powerPlaySavePercentage"] if "powerPlaySavePercentage" in res_goalie_stats else None
    new_goalie_stats.evenStrengthSavePercentage = res_goalie_stats["evenStrengthSavePercentage"] if "evenStrengthSavePercentage" in res_goalie_stats else None
    return new_goalie_stats 
