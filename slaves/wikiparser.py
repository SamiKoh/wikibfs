import aiohttp
import asyncio
import json
import re
import urllib

from bs4 import BeautifulSoup
from japronto import Application


async def getPage(path):
    async with aiohttp.ClientSession() as session:
        async with session.get(path) as response:
            return await response.text()


async def getLinks(request):
    try:
        wiki = request.query["lang"]
        url = request.query["page"]
    except AttributeError:
        return request.Response(text="Attribute error")
    wikipath = 'https://' + wiki + '.wikipedia.org/wiki/'
    page = await getPage(wikipath + url)    
    soup = BeautifulSoup(page, features="html.parser")
    
    links = []
    
    for link in soup.find_all('a'):
        l = link.get('href')
        try:    
            if re.match(r'^\/wiki\/[A-z()%0-9.-]*$',l):
                links.append(l.replace('/wiki/', '').lower())
        except AttributeError:
            pass
        except TypeError:
            pass

    obj = {'links': list(set(links))}
    
    return request.Response(json=obj)


app = Application()
app.router.add_route('/links', getLinks)
print("starting server...")
app.run(debug=True)
