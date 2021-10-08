import os
import math
import json


def get_main_item(comp_name, inp_mult):
	print([{comp_name : inp_mult}])
	pprint(main_brain(comp_name, inp_mult))



def main_brain(comp_name, mult):
	rec_tab = []
	with open("data.json") as raw_data:
		data_buff = json.load(raw_data)
		resources_list = data_buff["resources"]
	if "Desc_"+comp_name+"_C" not in resources_list:
		recipe = data_buff["recipes"]["Recipe_"+comp_name+"_C"]["ingredients"]
		product = data_buff["recipes"]["Recipe_"+comp_name+"_C"]["products"][0]["amount"]
		craft_time = data_buff["recipes"]["Recipe_"+comp_name+"_C"]["time"]
		for k in recipe:
			rec_tab.append([k["item"].replace("Desc_","").replace("_C", " rate is: ")+str(round((mult*(k["amount"]/product)*60)/craft_time, 1))+"min."])
			rec_tab[-1] += main_brain(k["item"].replace("Desc_","").replace("_C", ""), round(mult*(k["amount"]/product), 1))
	return rec_tab


def pprint(lst: list, padding: int=0):
    for head, *tail in lst:
        print(" "*4*padding, head, sep="")
        if tail:
            pprint(tail, padding+1)


get_main_item("SuperComputer", 1)
