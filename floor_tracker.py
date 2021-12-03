import csv
import pandas as pd
import json
import time
import numpy as np
trait_headers = ['Background','Fur','Mouth','Eyes','Earring','Clothes','Hat']               # headers for sales_traits dataframe
sales_traits = pd.read_csv('sales_traits.csv',names=trait_headers)# <-----------------------[Must have sale_traits.csv ported correctly here]
listing_headers = ['Price']                                                                 # header for listing_data dataframe
listing_data = pd.read_csv('listing_data.csv',names=listing_headers)# <---------------------[Must have sale_traits.csv ported correctly here]    

df = sales_traits.join(listing_data)                                                        # join the two dataframes
print(df)
                        
# outer dict holds inner dicts for each Trait Category
# inner dict - key is a trait, value is it's floor price

def trait_floors(mdf):
    '''
    This function takes in a the sale_listing dataframe
    and returns a dictionary filled with the minimum asks
    for each trait 
    :param: mdf
    :type: Dataframe
    :return: Outer/Inner dictionary
    '''
    tl = dict(zip(trait_headers,[{},{},{},{},{},{},{}]))
    # outer dict holds inner dicts for each Trait Category
    # inner dict - key is a trait, value is it's floor price     
    for trait_cat in trait_headers:                          # cycle thru each Trait Category
        trait_df = mdf[[trait_cat,'Price']]                  # create a subsect dataframe for each trait category
        trait_df = trait_df.pivot(columns=trait_cat)         # pivot dataframe such that it's columns are each trait in the trait category
        trait_df = trait_df['Price']                         # house_cleaning
        traits = trait_df.columns                            # grab each trait in the category and store into a list
        for trait in traits:                                 # cycle thru each trait in each trait category
            floor = trait_df[trait].min()                    # return trait's floor price
            tl[trait_cat][trait] = floor                     # store in the trait listing dictionary
    return tl                                           

trait_listing = trait_floors(df)


with open('trait_floors.json','w') as f:                    # store the trait_listing dictionary as a JSON file
    json.dump(trait_listing,f,indent=1)
f.close()
