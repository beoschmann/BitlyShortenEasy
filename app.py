import requests
import pandas as pd
import config

df = pd.read_csv(r'importurl.csv')
headers = {
    'Authorization': 'Bearer '+config.TOKEN,
    'Content-Type': 'application/json',
}

def shorten(fileimport) :
    headers = {
        'Authorization': 'Bearer '+config.TOKEN,
        'Content-Type': 'application/json',
    }
    for i in range(len(fileimport)):
        payload = '{"long_url":"' + fileimport.iloc[i][0] + '"}'
        #print(payload)
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=payload)
        #print(response)
        jsonResponse = response.json()
        print(jsonResponse)
        print (jsonResponse["long_url"]+" = \n"+jsonResponse["id"]+"\n")
        file = open("resp_text.txt", "a+")
        file.write(jsonResponse["long_url"]+" = \n"+jsonResponse["id"]+"\n")
        file.close()

#de = pd.read_csv(r'urltoshorten.csv')
#print(de)
#shorten(de)