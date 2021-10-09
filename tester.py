import requests

if __name__ == "__main__":
    countryCode = ['105391811', '105346827', '105384690', '105346646', '105339663']
    dictionaryMasterList = []
    for item in countryCode:
        url = "https://foreca-weather.p.rapidapi.com/observation/latest/" + item

        querystring = {"lang":"en"}

        headers = {
            'x-rapidapi-host': "foreca-weather.p.rapidapi.com",
            'x-rapidapi-key': "00a6319afcmshb59ecb31e0a9dbap1c6de4jsn4b86a9198483"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        list_of_dictionaries2 = response.json().get('observations')
        dictionaryMasterList = list_of_dictionaries2 + dictionaryMasterList
    print('WEATHER INFO')
    print(dictionaryMasterList)