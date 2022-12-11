def create_team(team):
    new_team = Team()
    new_team.id = team["id"]
    new_team.name = team["name"]
    new_team.teamName = team["teamName"]
    return new_team 
