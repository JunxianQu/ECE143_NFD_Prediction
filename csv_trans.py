import json
import csv
'''
Load the trait_floors JSON and convert that data into a CSV
'''

data = json.load(open('trait_floors.json'))                                        # load trait_floors JSON into data
trait_headers = ['Background','Fur','Mouth','Eyes','Earring','Clothes','Hat']      # List with each Trait Category
for trait_cats in trait_headers:                                                   # loop thru each trait category
  data_file = open(trait_cats+'_floors.csv', 'w')                                  # create a category specific csv files
  csv_writer = csv.writer(data_file)        
  for traits in data[trait_cats].keys():              
    msg = [traits,data[trait_cats][traits]]                                        # write into each row the trait and its listed price
    csv_writer.writerow(msg)
    print("csv",traits)
  data_file.close()                                                                