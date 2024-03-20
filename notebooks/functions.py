#!/usr/bin/env python
# coding: utf-8

# In[ ]:

### Import Modules
# from functions import * # Import Functions


# pandas library
import pandas as pd 

# numpy
import numpy as np

# import matplotlib library
from matplotlib import pyplot as plt

#import seaborn
import seaborn as sns


def drop_dub(df: pd.DataFrame):
    '''
    dropping dublicates, uniformating column_names, reseting the index.
    Parameters:
    - df (pd.DataFrame): Input DataFrame to be cleaned.
    Returns:
    - pd.DataFrame: Cleaned DataFrame duplicates removed, and index reset.
    '''
    df_2=df.copy()
    df_2.columns = df_2.columns.str.strip().str.lower()
    df_2.drop_duplicates(inplace=True)
    df_2.reset_index(drop=True,inplace=True)
    return df_2


def cleaning_gender(df: pd.DataFrame):
    '''
    cleaning the gender colmun using dic and map
    replaces the nan and errors with U (unknown)
    
    Parameters:
    - df (pd.DataFrame): Input DataFrame to be cleaned.
    Returns:
    - pd.DataFrame: Cleaned DataFrame.

    '''
    df2 = df.copy()

    gender_mapping = {'M':'M','F':'F','U':'U','x':'U'}
    df2['gendr']=df2.gendr.map(gender_mapping)
    
    df2['gendr'] = df2['gendr'].fillna('U')
    
    #df2['gendr'] = df2['gendr'].astype(str)
    
    return df2




def cleaning_Variation(df: pd.DataFrame):
    '''
    cleaning the Variation
    replaces the nan and errors with Unknown
    
    Parameters:
    - df (pd.DataFrame): Input DataFrame to be cleaned.
    Returns:
    - pd.DataFrame: Cleaned DataFrame.

    '''
    df2 = df.copy()

    df2['variation'] = df2['variation'].fillna('Unknown')
    
    
    return df2

def Null_Median(df: pd.DataFrame, column_name):
    '''
    Replaces the Nan in numeric columns with Median  
    Parameters:
    - df (pd.DataFrame) and column_name(as string) : Input DataFrame and the related column to be cleaned.
    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    '''
    df2 = df.copy()
    
    #median of the specified column
    Median = df2[column_name].median()
    
    # Replacing NaN in the specified column with  median
    df2[column_name] = df2[column_name].fillna(Median)
    
    return df2