import requests
from bs4 import BeautifulSoup
import json

from app.model import db, Player, User


def setUp():
    html = requests.get("https://www.nhl.com/capitals/roster").text

    soup = BeautifulSoup(html, 'html.parser')

    playerData = getData(soup)

    return playerData

def getData(soup):

    playerData = []

    forwardsName = soup.select("table.data-table__forwards.data-table__pinned tbody tr")

    forwardsInfo = soup.select("table.data-table__forwards.data-table__scrollable tbody tr")


    defensemenName = soup.select("table.data-table__defensemen.data-table__pinned tbody tr")

    defensemenInfo = soup.select("table.data-table__defensemen.data-table__scrollable tbody tr")


    goaliesName = soup.select("table.data-table__goalies.data-table__pinned tbody tr")

    goaliesInfo = soup.select("table.data-table__goalies.data-table__scrollable tbody tr")




    for i in range(len(forwardsName)):
        firstName = forwardsName[i].select("span.name-col__firstName")[0].text
        lastName = forwardsName[i].select("span.name-col__lastName")[0].text
        special = forwardsName[i].select("span.name-col__special")[0].text
        special = special.strip()

        number = forwardsInfo[i].select("td.number-col")[0].text
        position = forwardsInfo[i].select("td.position-col")[0].text
        shoots = forwardsInfo[i].select("td.shoots-col")[0].text
        height = forwardsInfo[i].select("span.xs-sm-md-only")[0].text
        weight = forwardsInfo[i].select("td.weight-col")[0].text
        player = {"firstname": firstName,
                  "lastname": lastName,
                  "special": special,
                  "number": number,
                  "position": position,
                  "shoots": shoots,
                  "height": height,
                  "weight": weight
                  }
        playerData.append(player)



    for j in range(len(defensemenName)):
        firstName = defensemenName[j].select("span.name-col__firstName")[0].text
        lastName = defensemenName[j].select("span.name-col__lastName")[0].text
        special = defensemenName[j].select("span.name-col__special")[0].text
        special = special.strip()

        number = defensemenInfo[j].select("td.number-col")[0].text
        position = defensemenInfo[j].select("td.position-col")[0].text
        shoots = defensemenInfo[j].select("td.shoots-col")[0].text
        height = defensemenInfo[j].select("span.xs-sm-md-only")[0].text
        weight = defensemenInfo[j].select("td.weight-col")[0].text
        player = {"firstname": firstName,
                  "lastname": lastName,
                  "special": special,
                  "number": number,
                  "position": position,
                  "shoots": shoots,
                  "height": height,
                  "weight": weight
                  }
        playerData.append(player)



    for k in range(len(goaliesName)):
        firstName = goaliesName[k].select("span.name-col__firstName")[0].text
        lastName = goaliesName[k].select("span.name-col__lastName")[0].text
        special = goaliesName[k].select("span.name-col__special")[0].text
        special = special.strip()

        number = goaliesInfo[k].select("td.number-col")[0].text
        position = goaliesInfo[k].select("td.position-col")[0].text
        shoots = goaliesInfo[k].select("td.shoots-col")[0].text
        height = goaliesInfo[k].select("span.xs-sm-md-only")[0].text
        weight = goaliesInfo[k].select("td.weight-col")[0].text
        player = {"firstname": firstName,
                  "lastname": lastName,
                  "special": special,
                  "number": number,
                  "position": position,
                  "shoots": shoots,
                  "height": height,
                  "weight": weight
                  }
        playerData.append(player)

    return playerData



if __name__ == "__main__":

    playerData = setUp()

    for item in playerData:
        db.session.add(Player(
            firstname=item.get("firstname"),
            lastname=item.get("lastname"),
            special=item.get("special"),
            number=item.get("number"),
            position=item.get("position"),
            shoots=item.get("shoots"),
            height=item.get("height"),
            weight=item.get("weight")
        ))

    db.session.add(User(username="Ben", email="ben.johnson@umbc.edu"))
    db.session.commit()

''''
    print(json.dumps(playerData, indent=4))

    with open('playerData.json', 'w') as fout:
        json.dump(playerData, fout,indent=4,)
'''''
