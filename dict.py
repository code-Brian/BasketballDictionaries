# Why, hello there! Let's go exploring! ㋡

# Pretend this list of dictionaries is pulled from an API.
# We need to put each team into a lost of Player object instancs 
# so that we can use methods related to players. 

players = [
    {
        "position": "small forward", 
        "age":34, 
        "team": "Brooklyn Nets",
        "name": "Kevin Durant"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

# KD = Player(players[0])

# print(KD.name)
# print(KD.age)
# print(KD.position)
# print(KD.team)