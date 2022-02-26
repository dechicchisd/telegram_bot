from email import utils
import requests
import utils

WIKI_PATH = 'https://it.wikipedia.org/wiki/'


def search_wiki(input_text):
    search_name = utils.composeName(input_text)
    url = WIKI_PATH + search_name

    page = requests.get(url)
    div = utils.getDiv(page)

    result = utils.getFullText(div)

    print(result)

    return result
