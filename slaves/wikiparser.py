import asyncio
import json
import re
import urllib

import requests
from bs4 import BeautifulSoup
from japronto import Application

async def getLinks(request):
    try:
        wiki = request.query["lang"]
        url = request.query["page"]
    except AttributeError:
        return request.Response(text="Attribute error")
    wikipath = 'https://' + wiki + '.wikipedia.org/wiki/'
    page = requests.get(wikipath + url)    
    soup = BeautifulSoup(page.text, features="html.parser")
    
    links = []
    
    for link in soup.find_all('a'):
        l = link.get('href')
        try:    
            if re.match(r'^\/wiki\/[A-z()%0-9.-]*$',l):
                links.append(l.replace('/wiki/', ''))
        except AttributeError:
            pass
        except TypeError:
            pass

    obj = {'links': links}
    
    return request.Response(json=obj)


app = Application()
app.router.add_route('/links', getLinks)
print("starting server...")
app.run(debug=True)
