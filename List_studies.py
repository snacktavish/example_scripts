#!/usr/bin/env python
import csv 
from opentree import OT



masterfile = "subspecies_splits.csv"

with open(masterfile, 'r') as base:
    base = csv.reader(base)
    next(base)
    ## Generate line-by-line name search ##
    Mixed_OTT_list = {}
    request_num = 0
    tally = 0
    diff = 0
    for line in base:
        request_num += 1
        
        ## Search for CLO & OTT Name
        for check in range(2):
            request_num += check
            
            name = line[check]
            value = name.strip()
            print("Species ", str(request_num), ":", value)
            pyot_resp = OT.find_trees(value=value, search_property='ot:ottTaxonName', verbose = True)
            data = pyot_resp.response_dict
            ## Test if Response is Valid
            for test in data:
                if test == 'message':
                    tally += 1
                    Mixed_OTT_list[("No." + str(tally))] = [value, 'Search Manually for Tree']
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
                    for i in range(len(Ott_list)):
                        short_list = [value, Ott_list[i]]
                        tally += 1
                        Mixed_OTT_list[("No." + str(tally))] = short_list
            ## 
            print("Total Studies", str(len(Ott_list)))
        #if request_num >= 250:
                #break

    print(Mixed_OTT_list)                                                   


with open("Subspecies_Ott_Search.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([" ","OTT Name", "Study ID", "url"])
    for line in Mixed_OTT_list:
        writer.writerow([line, Mixed_OTT_list[line][0], Mixed_OTT_list[line][1], "https://tree.opentreeoflife.org/curator/study/view/" + Mixed_OTT_list[line][1]])
    file.close()