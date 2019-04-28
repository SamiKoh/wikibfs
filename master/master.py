import json
import random
import time
import urllib
from functools import partial
#from japronto import Application
from multiprocessing import Manager
from multiprocessing.pool import Pool
import requests

N_WORKERS = 8
N_PROCESSES = 20

def getLinks(page, paths, end, lang):
    print("page = %s, n = %d"%(page, len(paths)))
    try:
        port = 3000 + random.randint(1,N_WORKERS)
        response = requests.get("http://127.0.0.1:" + str(port) + "/links?lang=" + lang + "&page=" + page)
        links = response.json()["links"]
    except TypeError as e:
        return [], []
    except json.decoder.JSONDecodeError:
        return [],[]

    new_links = []
    for link in links:
        if link == end.lower():
            paths[link] = paths[page] + [link]
            print("\n" + "->".join(paths[link]) + "\n")
            return [], paths[page] + [link]
        if (link not in paths) and (link != page):
            try:
                paths[link] = paths[page] + [link]
                new_links.append(link)
            except KeyError as e:
                print("key error")
                print(e)
    return new_links, []
 
def shortest_path(start, end, lang):
    end = urllib.parse.quote(end)
    paths = Manager().dict()
    paths[start] = [start]
    Q = [start]
    cont = True
    while cont:
        if len(Q) > N_PROCESSES:
            batch = Q[0:N_PROCESSES]
            p = Pool(processes=N_PROCESSES)
            Q = Q[N_PROCESSES:]
        else:
            p = Pool(processes=len(Q))
            batch = Q
            Q = []
        data = p.map(partial(getLinks, paths=paths, end=end, lang=lang), [link for link in batch])
        p.close()
        with open("data1.txt", "w") as f:
            f.write(str(data))
        results = [x[1] for x in data if len(x[1]) > 0]
        if len(results) > 0:
            print(results)
            cont = False
        tmp = [x[0] for x in data]
        Q += list(set([x for y in tmp for x in y]))
        s = set()
        Q = [x for x in Q if not (x in s or s.add(x))]
    with open("results.txt", "w") as f:
        f.write(str(results))
    return results


""" 

def main(request):
    try:
        lang = request.query["lang"]
        start = request.query["start"]
        end = request.query["end"]
        if lang not in ['fi', 'en', 'de']:
            lang = 'en'

        start = time.time()
        results = shortest_path(start, end, lang)
        print("\nIt took %d seconds."%(time.time() - start))
        obj = {"results": results}
        return request.Response(json=obj)
    except AttributeError:
        return request.Response(text="Attribute error")
 """
if __name__ == "__main__":
    start = time.time()
    results = shortest_path("cat", "australia", "en")
    print("\nIt took %d seconds."%(time.time() - start))
    
    #app = Application()
    #app.router.add_route('/main', main)
    #print("starting master...")
    #app.run(debug=True)
