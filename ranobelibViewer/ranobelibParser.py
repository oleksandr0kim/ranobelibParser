import json
import requests
from bs4 import BeautifulSoup as bs


from constans import recomendationUrl
from classes.ranobeClass.searchIconClass import searchIconClass

def parseHomePage():

    src = requests.get(recomendationUrl)

    paragraphList = json.loads(src.text)


    recomendarionRanobeList = []

    for ranobe in paragraphList['resource']:

        rabobeData = {
            "name": ranobe['names']['rus'],
            "coverUrl": ranobe['poster']['medium'],
            "id": ranobe['id'],
            "vovule": ranobe['counts']['volumes'],
            "chapters": ranobe['counts']['chapters']
        }

        recomendarionRanobeList.append(rabobeData)


    return recomendarionRanobeList


def searchRanobe(ranobeName):
    res = requests.get('https://ranobehub.org/api/fulltext/global?query=' + ranobeName)
    result = json.loads(res.text)

    searchResult = []
    print(result)

    try:
        for ranobe in result[1]['data']:

            rabobeData = {
                "name": ranobe['names']['rus'],
                "id": ranobe['id'],
            }

            icon = searchIconClass()
            icon.name, icon.id = rabobeData['name'], rabobeData['id']

            searchResult.append(icon)
    except:

        icon = searchIconClass()
        icon.name, icon.id = 'Пусто...', 0

        searchResult.append(icon)


    return searchResult