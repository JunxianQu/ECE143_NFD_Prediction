# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 14:42:31 2021

@author: ITSloaner
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from collections import OrderedDict
def plot(df,feature,dict_trait):
    '''
    The function takes in
    a dataframe that consists
    of traits and a particular
    feature that we want
    to plot as a histogram.

    Parameters
    ----------
    df : pandas Dataframe
        Consists of traits of
        the NFTs.
    feature : String
        Name of the feature
        that we want to plot.
    dict_trait: Dictionary (Counter)
        Contains the number of
        type of traits.

    Returns
    -------
    None.

    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(feature,str)
    assert isinstance(dict_trait,Counter)
    
    traits = set(('Background','Fur','Mouth','Eyes','Earring','Clothes','Hat'))
    
    assert feature in traits
    
    values = Counter(df[feature].values.flatten())
    
    percentage = Counter({key: values[key]*100/dict_trait[key] for key in values})
    
    percentage_list = sorted(percentage.items(),key=lambda i:i[1],reverse=True)
    
    sorted_percentage = dict({k:v for k,v in percentage_list})
    
    plt.figure(figsize=(20,3))
    plt.bar(sorted_percentage.keys(),sorted_percentage.values(),width=0.5)
    plt.xticks(range(len(sorted_percentage)),sorted_percentage.keys(),rotation=75)
    plt.title(feature)

    

def types_of_traits(trait_pd):
    '''
    The function takes in 
    the trait Pandas Data Frame
    and returns a dictionary 
    of dictionaries that 
    has the keys as the traits
    and each key has a dictionary
    associated with it. These
    dictionaries contain the count
    of each type of trait.

    Parameters
    ----------
    trait : pd.DataFrame
        Data Frame that contains 
        different traits.

    Returns
    -------
    dict.

    '''
    assert isinstance(trait_pd,pd.DataFrame)
    
    dictt = {}
    
    traits = set(('Background','Fur','Mouth','Eyes','Earring','Clothes','Hat'))
    
    for trait in traits:
        
        df = trait_pd[trait]
        values = Counter(df.values.flatten())
        dictt[trait] = values
        
    return dictt
    

def grouping(value):
    '''
    Function returns the
    group number depending
    on range. If value is 0
    return 0. If value is in
    [1,4] return 1, [5,9] return
    2 and [10,14] return 3

    Parameters
    ----------
    value : int

    Returns
    -------
    Group by value.

    '''
    if value==0:
        return '0'
    if value in range(1,8):
        return '1'
    if value in range(8,15):
        return '2'
    # if value in range(10,15):
    #     return '3'
    
def no_sold_token(sales,traits):
    '''
    The function takes 
    in 2 dataframes sales
    and traits. Sales
    dataframe has NFT ids,
    and the price at which the
    tokens are sold.
    The traits dataframe 
    has set of traits
    for each token id.

    Parameters
    ----------
    sales : pandas Dataframe
        Contains the price at
        which the NFTs are sold.
    traits : pandas Dataframe.
        Contains the traits of
        the NFTs.

    Returns
    -------
    None.

    '''
    
    assert isinstance(sales,pd.DataFrame)
    assert isinstance(traits,pd.DataFrame)
    
    
    count = sales.count(axis='columns')
    
    groups = count.groupby(by=lambda i:grouping(count.loc[i]))
    
    dictt_traits = types_of_traits(traits)
    print(dictt_traits)
    
    idx = groups.get_group('2').index
    traits_0 = traits.loc[idx]
    
    plot(traits_0,'Background',dictt_traits['Background'])
    
    

sales = pd.read_csv('sales_data.csv')
trait = pd.read_csv('trait_data_file.csv')
sales = sales.set_index('TokenID') 
trait = trait.set_index('TokenID')
# print(sales)
# print(trait)
no_sold_token(sales, trait)



