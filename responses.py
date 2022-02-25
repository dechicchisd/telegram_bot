from email import utils
import constants as cost
import requests
import utils


def search_wiki(input_text):
    search_name = utils.composeName(input_text)
    url = cost.WIKI_PATH + search_name

    page = requests.get(url)
    div = utils.getDiv(page)

    result = utils.getFullText(div)

    print(result)

    return result
