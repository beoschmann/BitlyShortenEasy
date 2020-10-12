# BitlyShortenEasy
Tool created to easily transform multiple Link into Bitly.

#### **extractjson.py**
File to execute.
Extract google doc data and parse them to shorten the link with bitly

#### **What you need :**

    -Config.py with token from bitly. with TOKEN=""
    -Replace the Doc ID from google doc to work in extractjson.py
    -credentials.json&token.json -> Created automatically by google
    

If not, check quickstart.py on google.

#### **App.py**
Can be used you as standalone to just shorten without extracting data from google doc.
You need to insert your token to make it work.


#### **urltoshorten.csv**

List of url to be shortened. Must include "https://"


#### **res_text.txt**

List of url shortened format :

Line 1 : LONG URL =

Line 2 : SHORT URL

Thanks for using the tool.
