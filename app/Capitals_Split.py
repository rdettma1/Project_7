from app.model import db, Player, User

def get_players():

    players = Player.query.all()

    print(players)

    offense = players[0:13]

    defense = players[13:19]

    goalies = players[19:]

    print(offense)

    print(defense)

    print(goalies)

    myData = {"offense":offense,
              "defense":defense,
              "goalies":goalies
            }

    print(myData)

    print(myData.get("offense")[0].number)

    return myData;

if __name__ == "__main__":
    get_players()