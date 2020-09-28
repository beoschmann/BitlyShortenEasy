import requests
import pandas as pd
import config
df = pd.read_csv(r'C:\Users\boschman\PycharmProjects\pythonProject\testimport.csv')

TOKEN = '8772d81a91dceeca5799a8afe0571bf3ee14dd8b'
headers = {
    'Authorization': 'Bearer '+config.TOKEN,
    'Content-Type': 'application/json',
}
dflen = len(df)

for i in range(len(df)):
    payload = '{"long_url":"' + df.iloc[i][0] + '"}'
    #print(payload)
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=payload)
    #print(response)
    jsonResponse = response.json()
    print (jsonResponse["long_url"] , jsonResponse["id"])
    file = open("resp_text.txt", "a+")
    file.write(jsonResponse["long_url"]+jsonResponse["id"]+"\n")
    file.close()



