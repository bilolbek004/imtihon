from threading import Thread

import httpx, json


def func1():
    url1 = 'https://api.chucknorris.io/jokes/random'
    req1 = httpx.get(url1)
    data = req1.json()
    with open('first.json.json', 'w') as f:
        json.dump(data, f, indent=4)


def func2():
    url1 = 'https://api.chucknorris.io/jokes/categories'
    req2 = httpx.get(url1)
    data = req2.json()
    with open('second.json.json', 'w') as f:
        json.dump(data, f, indent=4)


def func3():
    url1 = 'https://api.chucknorris.io/jokes/search?query={query}'
    req3 = httpx.get(url1)
    data = req3.json()
    with open('third.json.json', 'w') as f:
        json.dump(data, f, indent=4)


def func4():
    url1 = 'https://api.chucknorris.io/jokes/random?category={category}'
    req4 = httpx.get(url1)
    data = req4.json()
    with open('fourth.json.json', 'w') as f:
        json.dump(data, f, indent=4)


def func5():
    url1 = 'https://api.chucknorris.io/jokes/random'
    req5 = httpx.get(url1)
    data = req5.json()
    with open('fifth.json.json', 'w') as f:
        json.dump(data, f, indent=4)


oqim1 = Thread(target=func1(), daemon=True)
oqim2 = Thread(target=func2(), daemon=True)
oqim3 = Thread(target=func3(), daemon=True)
oqim4 = Thread(target=func4(), daemon=True)
oqim5 = Thread(target=func5(), daemon=True)
