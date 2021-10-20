import requests


if __name__ == "__main__":
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    pair = "en|it"
    a = 1
    if a == 1:
        pair = "en|es"


    querystring = {"langpair":pair,"q":"Hello World!","mt":"1","onlyprivate":"0","de":"a@b.c"}

    headers = {
        'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
        'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


if __name__ == "__main__":
    url = "https://127.0.0.1:5000/jokes"
    response = requests.request("GET", url)
    jokes = response.json()
    print(jokes)