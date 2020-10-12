from __future__ import print_function
import json
from apiclient import discovery
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import app
import pandas as pd
import config


headers = {
    'Authorization': 'Bearer '+config.TOKEN,
    'Content-Type': 'application/json',
}
######################################################################
# IMPORT OF THE DOC
######################################################################

# Set doc ID, as found at `https://docs.google.com/document/d/YOUR_DOC_ID/edit`
DOCUMENT_ID = '1I2Rn08OSfqulqpiK_3fyqnsVJvLcDwRgLK3dEth4y0k'

# Set the scopes and discovery info
SCOPES = 'https://www.googleapis.com/auth/documents.readonly'
DISCOVERY_DOC = ('https://docs.googleapis.com/$discovery/rest?'
                 'version=v1')

# Initialize credentials and instantiate Docs API service
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = discovery.build('docs', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC)

# Do a document "get" request and print the results as formatted JSON
result = service.documents().get(documentId=DOCUMENT_ID).execute()
file = open("extract_text.json", "w")
file.write(json.dumps(result, indent=4, sort_keys=True))
file.close()

file = open("extract_text.json")
docpars=json.load(file)

#RESET OF URL input file
file_out= open("urltoshorten.csv", "w")
file_out.write("url\n")
file_out.close()
file_out= open("urltoshorten.csv", "a+")

######################################################################
# PARSING OF THE DOC and GET URL
######################################################################

k=-1
docsparslen=len(docpars["body"]["content"])-1
for i in range(0, len(docpars["body"]["content"])):
    if k == docsparslen :
        break
    k=k+1
    if "paragraph" not in docpars["body"]["content"][k] :
            k = k + 1
    if docpars["body"]["content"][k]["paragraph"] != None :
        if docpars["body"]["content"][k]["paragraph"]["elements"] != None :
            while len(docpars["body"]["content"][k]["paragraph"]["elements"])!=4 :
                if k == docsparslen :
                    break
                k = k +1
            if k == docsparslen :
                break
            if docpars["body"]["content"][k]["paragraph"]["elements"][2]["textRun"] != None:
                if docpars["body"]["content"][k]["paragraph"]["elements"][2]["textRun"]["textStyle"] != None :
                    if docpars["body"]["content"][k]["paragraph"]["elements"][2]["textRun"]["textStyle"]["link"] != None :
                        file_out.write(docpars["body"]["content"][k]["paragraph"]["elements"][2]["textRun"]["textStyle"]["link"]["url"]+"\n")


file_out.close()

######################################################################
# SHORTEN OF URL with BITLY API
######################################################################

de = pd.read_csv(r'urltoshorten.csv')
app.shorten(de)



