from japronto import Application
import asyncio

first = urllib.parse.quote('Finland')
final = urllib.parse.quote('Orangutan')

path = {}
path[first] = [first]
Q = deque([first])

cont = True

while len(Q) != 0 and cont:
    page = Q.popleft()
    print("page " + page)
    links = getLinks(page, final)
    for link in links:
        if link.lower() == final.lower():
            print(" -> ".join(path[page]) + " -> " + link)
            cont = False
            break
        elif (link not in path) and (link != page):
            path[link] = path[page] + [link]
            Q.append(link)


app = Application()
# Add only route to root
app.router.add_route('/links', getLinks)
app.router.add_route('/basic', basic)
app.router.add_route('/', hello)
print("starting server...")
app.run(debug=True)
