def create_team_stats(rev_team_info,info,team_info,home_or_away):
    new_team_stats = TeamStats()
    new_team_stats.gamePk = info["gamePk"]
    new_team_stats.teamId = team_info["team"]["id"]
    new_team_stats.isHome = (home_or_away == "home")
    if "teamSkaterStats" in team_info["teamStats"]:
        res_team_stats = team_info["teamStats"]["teamSkaterStats"]
        rev_res_team_stats = rev_team_info["teamStats"]["teamSkaterStats"]

        new_team_stats.goals = res_team_stats["goals"]
        new_team_stats.pim = res_team_stats["pim"]
        new_team_stats.shots = res_team_stats["shots"]
        new_team_stats.powerPlayPercentage = res_team_stats["powerPlayPercentage"]
        new_team_stats.powerPlayGoals = res_team_stats["powerPlayGoals"]
        new_team_stats.powerPlayOpportunities = res_team_stats["powerPlayOpportunities"]
        new_team_stats.faceOffWinPercentage = res_team_stats["faceOffWinPercentage"]
        new_team_stats.blocked = res_team_stats["blocked"]
        new_team_stats.takeaways = res_team_stats["takeaways"]
        new_team_stats.giveaways = res_team_stats["giveaways"]
        new_team_stats.hits = res_team_stats["hits"]

        new_team_stats.goalsAgainst = rev_res_team_stats["goals"]
        new_team_stats.pimAgainst = rev_res_team_stats["pim"]
        new_team_stats.shotsAgainst = rev_res_team_stats["shots"]
        new_team_stats.powerPlayPercentageAgainst = rev_res_team_stats["powerPlayPercentage"]
        new_team_stats.powerPlayGoalsAgainst = rev_res_team_stats["powerPlayGoals"]
        new_team_stats.powerPlayOpportunitiesAgainst = rev_res_team_stats["powerPlayOpportunities"]
        new_team_stats.faceOffWinPercentageAgainst = rev_res_team_stats["faceOffWinPercentage"]
        new_team_stats.blockedAgainst = rev_res_team_stats["blocked"]
        new_team_stats.takeawaysAgainst = rev_res_team_stats["takeaways"]
        new_team_stats.giveawaysAgainst = rev_res_team_stats["giveaways"]
        new_team_stats.hitsAgainst = rev_res_team_stats["hits"]

        new_team_stats.wins = info["stats"][team_info["team"]["id"]]["wins"]
        new_team_stats.losses = info["stats"][team_info["team"]["id"]]["losses"]
        new_team_stats.ot = info["stats"][team_info["team"]["id"]]["ot"]
        new_team_stats.leagueRecordType = info["stats"][team_info["team"]["id"]]["type"]
        new_team_stats.score = info["stats"][team_info["team"]["id"]]["score"]

    return new_team_stats 
