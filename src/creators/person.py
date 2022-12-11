def create_person(player,details):
    new_person = Person()
    new_person.id = player["person"]["id"]
    new_person.fullName = player["person"]["fullName"]
    new_person.positionCode = player["position"]["code"]
    new_person.weight = details["people"][0]["weight"]
    new_person.height = convert_height_string_to_int(details["people"][0]["height"])
    new_person.shootsCatches = details["people"][0]["shootsCatches"]
    
    return new_person 
