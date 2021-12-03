import csv
import pandas as pd
import json
import time
trait_headers = ['Background','Fur','Mouth','Eyes','Earring','Clothes','Hat']               # Every Trait Category in a list (column headers)
trait_data = pd.read_csv('trait_data_file.csv',names=trait_headers)                         # load trait_data dataframe
listing_headers = ['TokenID','Price']                                                       # headers for listing_data dataframe
listing_data = pd.read_csv('listing_data.csv',names=listing_headers)


sale_trait = {}                                                                             # trait dict for each ape on sale 
for i in range(0,len(listing_data),1):                                                      # loop each row in listing_data.csv
    ind = listing_data["TokenID"][i]                                                        # record index

    sale_trait[ind] = {}                                                                    # create an inner dictionary for each ape on sale
    sale_trait[ind]['ID'] = ind                                                             # record ape ID             
    for x in trait_headers:                                                 
        sale_trait[ind][x] = trait_data.iloc[ind][x]                                        # record the traits for each ape on sale     
    
    
data_file = open('sales_traits.csv', 'w')                                                   # open CSV file
csv_writer = csv.writer(data_file)
    
for i in range(0,len(listing_data),1):                                                      # export sale_traits dictionary into CSV file                        
    ind = listing_data['TokenID'][i]
    csv_writer.writerow(sale_trait[ind].values())
    print("csv",i)
    
 
data_file.close()

