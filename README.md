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
### Bar_Graphs_Visualization.ipynb
The Jupyter file is run to visualize the bar graphs. It imports functions from basic_functions.py.

## How to run the code
1.Clone the repository. <br>
2. Run Bar_Graphs_Visualization.ipynb to visualize the bar graphs.

## Required packages
numpy <br>
matplotlib <br>
squarify <br>
pandas <br>
collections <br>
sklearn <br>
