# ECE143_NFD_Prediction

## File Structure
### opensea_api.py
The file is used for extracting id, current highest price offered by others and features id.
### opensea_traits.py
The file is used for extracting feature name, feature type and feature id. The file is saved in json and csv.
### basic_functions.py
The file has the necessary functions for plotting the bar graphs.
### floor_tracker.py
The file reads sales_traits.csv and trait_data.csv and outputs the floor prices for each trait into json file trait_floors.json
### apes_on_sale.py
This file calls the OpenSea API and returns a JSON with the sale price for every ape currently on sale
It might be a good idea to run this code in batches, ranges from 0 - 9999
### csv_trans.py
this file loads JSON data and converts into CSV
### listed_traits.py
this file takes traits_data_file.csv which contains the trait data for each ape and listing_data.csv which contains data on which apes
are currently on sale and exports a csv with the trait data for each ape on sale (CSV)
### Bar_Graphs_Visualization.ipynb
The Jupyter file is run to visualize the bar graphs. It imports functions from basic_functions.py.
### NFT_Prediction.ipynb
The Jupyter file is run to split the data into training, testing and targeting sets, train a random forest regressor using the datasets and visualize the performance on testing set as well as the feature importance of each trait category. It load the date from trait_data_file_with_name.csv and trait_data_file_with_offer_name.csv.   
### trait_data_file_with_name.csv
The file contain the trait information of all the Bored Apes with the first row presenting the names of trait categories. 
### trait_data_file_with_offer_name
The file contain the offered price and transaction history of all the Bored Apes with the first row indicating what is the column present.   

## How to run the code
1.Clone the repository. <br>
2. Run Bar_Graphs_Visualization.ipynb to visualize the bar graphs.
3. Run NFT_Prediction.ipynb to see the performance of regressior and the feature importance graph.  

## Required packages
numpy <br>
matplotlib <br>
squarify <br>
pandas <br>
collections <br>
sklearn <br>
