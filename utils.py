import bs4


def composeName(input):
    search_name = str(input)
    search_name = search_name.replace(" ", "_")
    print(search_name)
    return search_name


def getDiv(page):
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    divs = soup.find_all("div", class_='mw-parser-output')

    div = divs[0]

    return div


def readTag(tag):
    string = ''
    for item in tag:
        if type(item) == bs4.NavigableString:
            string += item

        elif type(item) == bs4.Tag:
            string += readTag(item)
    return string


def getFullText(div):
    result = ''

    for i in div:
        if i.name == 'p':
            result += readTag(i)

        if i.name == 'div' and i.get('id') == 'toc':
            break

    return result
