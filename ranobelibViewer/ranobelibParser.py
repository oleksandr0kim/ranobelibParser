import json
import requests
from bs4 import BeautifulSoup as bs


from constans import recomendationUrl, searchUrl, ranobePageUrl

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
    searchResult = []

    try:

        res = requests.get(searchUrl + ranobeName)
        result = json.loads(res.text)
        print(result)


        for ranobe in result[1]['data']:

            rabobeData = {
                "name": ranobe['names']['rus'],
                "id": ranobe['id'],
            }


            searchResult.append(rabobeData)



    except:

        rabobeData = {
            "name": 'Пусто...',
            "id": 0,
        }

        searchResult.append(rabobeData)


    return searchResult

def parseRanobePage(id):

    src = requests.get(ranobePageUrl + str(id))
    manyVovumes = len(requests.get(f"https://ranobehub.org/api/ranobe/{id}/contents").json()['volumes'])

    soup = bs(src.content, 'html.parser')


    name = soup.find('h1', class_="ui huge header").get_text().strip()
    description = soup.find('p').get_text().strip()
    coverUrl = soup.find('img', class_="ui large bordered rounded image __posterbox").get_attribute_list('data-src')[0]

    ranobeData = {
        "name": name,
        "description": description,
        "coverUrl": coverUrl,
        "manyVovumes": manyVovumes
    }

    return ranobeData
