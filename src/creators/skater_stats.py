def create_skater_stats(player_info,info,res_skater_stats,team_info):
    new_skater_stats = SkaterStats()
    new_skater_stats.playerId = player_info["person"]["id"]
    new_skater_stats.gamePk = info["gamePk"]
    new_skater_stats.position = player_info["position"]["code"]
    new_skater_stats.team = team_info["team"]["id"]

    new_skater_stats.timeOnIce = convert_string_to_time(res_skater_stats["timeOnIce"])
    new_skater_stats.assists = res_skater_stats["assists"]
    new_skater_stats.goals = res_skater_stats["goals"]
    new_skater_stats.shots = res_skater_stats["shots"]
    new_skater_stats.hits = res_skater_stats["hits"]
    new_skater_stats.powerPlayGoals = res_skater_stats["powerPlayGoals"]
    new_skater_stats.powerPlayAssists = res_skater_stats["powerPlayAssists"]
    new_skater_stats.penaltyMinutes = res_skater_stats["penaltyMinutes"]
    new_skater_stats.faceOffWins = res_skater_stats["faceOffWins"]
    new_skater_stats.faceoffTaken = res_skater_stats["faceoffTaken"]
    new_skater_stats.takeaways = res_skater_stats["takeaways"]
    new_skater_stats.giveaways = res_skater_stats["giveaways"]
    new_skater_stats.shortHandedGoals = res_skater_stats["shortHandedGoals"]
    new_skater_stats.shortHandedAssists = res_skater_stats["shortHandedAssists"]
    new_skater_stats.blocked = res_skater_stats["blocked"]
    new_skater_stats.plusMinus = res_skater_stats["plusMinus"]
    new_skater_stats.evenTimeOnIce = convert_string_to_time(res_skater_stats["evenTimeOnIce"])
    new_skater_stats.powerPlayTimeOnIce = convert_string_to_time(res_skater_stats["powerPlayTimeOnIce"])
    new_skater_stats.shortHandedTimeOnIce = convert_string_to_time(res_skater_stats["shortHandedTimeOnIce"])
    
    return new_skater_stats 
