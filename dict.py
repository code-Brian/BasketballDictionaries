# Why, hello there! Let's go exploring! ㋡

# Pretend this list of dictionaries is pulled from an API.
# We need to put each team into a lost of Player object instancs 
# so that we can use methods related to players. 

# players imaginary API info
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
    # ! Class Attribute created an empty list to store our intances of Player objects.
    player_instances = []

    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    @classmethod
    def get_team(cls,team_list):
        new_team = []
        for cls.team in team_list:
            new_team.append(Player(cls.team))
        return new_team
kd = Player(players[0])
jasonT = Player(players[1])
kyrieI = Player(players[2])

players_iterated = []
for dict in players:
    players_iterated.append(Player(dict))

# print(players_iterated)

# for i in players_iterated:
#     print(i.name)

team = Player.get_team(players)
for i in range(0,len(team)):
    print(team[i].name)