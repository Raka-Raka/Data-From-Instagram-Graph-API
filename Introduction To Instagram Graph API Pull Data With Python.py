#!/usr/bin/env python
# coding: utf-8
#You only have to do two things to test the function: replace the instagram id and the access_token

import requests
import json
import pprint

domain = "https://graph.facebook.com/v9.0/"

my_insta_id = "781290450923865" # make sure you repmace the instagram id with your own intagram id

part_A = "?fields=business_discovery.username("

part_B_List = ["justinbieber", "selenagomez", "nickiminaj", "willsmith"]

part_C = "){media{caption,media_url}}&"

acces_token = "access_token=TFCDKJNIomd0ZBZBFZCAP5BCkfzjxELZAKLQDAChhZCIZD" # make sure you dont delete: access_token=

box = []
i = 0

while i < len(part_B_List):

    try:           
            url = domain + my_insta_id + part_A + part_B_List[i] + part_C + acces_token
            
            data = requests.get( url )
            
            link = [json.loads( data.content )][0]['business_discovery']['media']['data'][0]['media_url']
            
            caption = [json.loads( data.content )][0]['business_discovery']['media']['data'][0]['caption']
            box.append ([link, caption]) 
            i+=1
            
    except KeyError:
        box.append([""])
        i+=1
print(box)
