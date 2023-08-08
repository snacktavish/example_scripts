#!/usr/bin/env python
import csv 
from opentree import OT



masterfile = "subspecies_splits.csv"

with open(masterfile, 'r') as base:
    base = csv.reader(base)
    next(base)
    ## Generate line-by-line name search ##
    final_list = {}
    n = 0
    for line in base:
        n += 1
        ## Search for CLO & OTT Name
        for check in range(2):
            n += check
            name = line[check]
            value = name.strip()
            print("Species ", str(n), ":", value)
            pyot_resp = OT.find_trees(value=value, search_property='ot:ottTaxonName', verbose = True)
            data = pyot_resp.response_dict
            ## Test if Response is Valid
            for test in data:
                if test == 'message':
                    final_list[("No." + str(n))] = [value,0]
                    break
                else:
            ## Add all Ott_Ids to single list
                    Ott_list = []
                    for resp in data['matched_studies']:
                        for ott_id in resp:
                            ott_id = resp['ot:studyId']
                            if ott_id not in Ott_list:
                                Ott_list.append(ott_id)
                                
            ## Create Dictionary of Lists
                    short_list = [value, Ott_list]
                    final_list[("No." + str(n))] = short_list
                    # for i in range(0,len(Ott_list)):
                        # num = str(n+i)
                        
            print("Total Studies", str(len(Ott_list)))
        if n >= 16:
                break

    print(final_list)                                                   

