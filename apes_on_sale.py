import requests
import json
import time
# url_specs hold the necessary specifiers to filter the right data being called
url_specs = '?&bundled=false&include_bundled=false&include_invalid=false&order_by=eth_price&order_direction=asc&asset_contract_address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D&side=1&sale_kind=0"'
listing_data = {}                                                                             # create a dictionary to hold the listing price for each ape on sale
'''
This for loops calls the below endpoint each time
and returns the listing data for each ape one at a time
10,000 calls in total need to be made
ranging from 
'''
for ids in range(1001,9999,1): # <-----------------------------------------------------------  when extracting from API it may be a good idea to do it in batches

    endpoint = "https://api.opensea.io/wyvern/v1/orders"                                     # end point for all listing events data
    url = endpoint + url_specs + '&token_id=' + str(ids)                                     # here we change the last specifier for each loop for the next ape  

    headers = {"Accept": "application/json", "X-API-KEY":'6cf71d3af4a94c1e982e2521203367be'} # just remember you need this API key to access the JSON responses

    response = requests.request("GET", url, headers=headers)
    
    response = response.json()
    time.sleep(1)                                                                            # sleep for 1 sec so as to not spam the API
    if response['orders'] != []:                                                             # if the ape is not on sale it will return an empty list when given this key
        print('id:',ids)                                                                     # print which ape's data is currently being called
        orders = response['orders']
        orders = orders[0]
        curr_price = float(orders['current_price']) / 1000000000000000000
        listing_data[ids] = {}                                                               # create inner dictionaries for each listed ape 
        listing_data[ids]['id'] = ids                                                        # store apes ID
        listing_data[ids]['current_price']=curr_price                                        # store it's listing price


with open('batch_data.json','w') as f:# <----------------------------------------------------  export the listing data into JSON file                                                                
    json.dump(listing_data,f,indent=1)                                                       # be weary of the what you name the file, no overrides plz
f.close()
            
    
