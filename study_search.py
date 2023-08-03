#!/usr/bin/env python

# curl -X POST https://api.opentreeoflife.org/v3/studies/find_trees -H "content-type:application/json" -d '{"property":"ot:ottTaxonName","value":"Apteryx australis","verbose":true}' > Apyterx.json

import json

correct_answer = json.load(open("Apyterx.json"))

print("There should be {x} studies in the response".format(x=len(correct_answer['matched_studies'])))