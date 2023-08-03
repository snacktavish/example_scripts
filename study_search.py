#!/usr/bin/env python

# curl -X POST https://api.opentreeoflife.org/v3/studies/find_trees -H "content-type:application/json" -d '{"property":"ot:ottTaxonName","value":"Apteryx australis","verbose":true}'
import json
import requests
import curlify

from opentree import OT


correct_answer = json.load(open("Apyterx.json"))

print("There should be {x} studies in the response".format(x=len(correct_answer['matched_studies'])))


payload = {'property':'ot:ottTaxonName', 'value':'Apteryx australis', 'verbose':'true'}
headers =  {"Content-Type":"application/json"}
r = requests.post('https://api.opentreeoflife.org/v3/studies/find_trees',
                   data=json.dumps(payload),
                   headers=headers)

print(curlify.to_curl(r.request)) 
data = r.json()
## Try with OS / BASH CURL?

#data = json.load(open("Aptyrex_trees.txt", r))
#print(data)

Ott_list = []
for i in data['matched_studies']:
    for x in i:
        x = i['ot:studyId']
        if x not in Ott_list:
            Ott_list.append(x)


        
#print(Ott_list)

print("There are  {x} studies in this list.".format(x = len(Ott_list)))


pyot_resp = OT.find_trees(value='Apteryx australis', search_property='ot:ottTaxonName', verbose = True)

print("There are  {x} studies using python opentree.".format(x = len(pyot_resp.response_dict['matched_studies'])))
