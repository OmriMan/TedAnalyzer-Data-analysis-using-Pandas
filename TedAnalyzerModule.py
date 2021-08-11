# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:53:59 2019

@author: omrim
"""
import pandas as pd
import ast
class TedAnalyzer:
    '''
    a class that contains methods to explore dataset
    '''
    def __init__(self,file_path):
        '''
        constructor
        param file_path: receives a path to a .txt file that is located in the same directory of the TedAnalyzerModule.py file
        '''
        self.data = pd.read_csv(file_path)
    
    def get_data(self):
        '''
        return a copy of the data attribute
        '''
        copypy = pd.DataFrame.copy(self.data,deep=True)
        return copypy
    
    def get_data_shape(self):
        '''
        return a tuple holding the shape of the data attribute
        '''
        return self.data.shape
    
    def get_top_n_by_col(self,column_name,n):
        '''
         returns a Dataframe object that contains a copy of the top ​n ​ rows from the ​data ​ attribute, that has the highest values in the 
         column_name ​ column, if n is bigger than the number of rows in ​data ​ attribute, return all of the rows
        '''
        copydata = self.get_data()
        col = column_name
        datasort = copydata.sort_values(by=[col],ascending=False)#sort the dataframe by the input column_name
        if n>=len(datasort.index):#if n is bigger than the number of rows in ​data attribute
            return datasort#return all of the rows
        return datasort.head(n)
    
    def get_unique_values_as_list(self,column_name):
        '''
        returns a list of the unique values in the column ​column_name 
        '''
        copypy = self.get_data()
        col = column_name
        coldata = copypy[col]#new dataframe of one column
        uni = coldata.unique()#array of unique values
        return list(uni)
    
    def get_unique_values_as_dict(self,column_name):
        '''
        returns a dictionary of the unique value in column ​column_name as keys and the number of rows they appear in as values
        '''
        copypy = self.get_data()
        col = column_name
        coldata = copypy[col]#new dataframe of one column
        uniseries = coldata.value_counts()#series object that contain the unique values and the numbers of rows that each value show
        thedict = uniseries.to_dict()#convert from series object to dict
        return thedict
    
    def get_na_counts(self):
        '''
        return a series object with counts of the null values in each column
        '''
        nans = self.data.isna()
        return nans.sum()
        
    def get_all_na(self):
        '''
        returns a copy of the ​data ​attribute with all the rows that contain at least one null value
        '''
        copypy = self.get_data()
        all_na = copypy[pd.isnull(copypy).any(axis=1)]
        return all_na
        
    def drop_na(self):
        '''
        removes all rows that contain at least a single column with null value from the ​data ​ attribute and resets the index of the result dataFrame
        return None
        '''
        df = self.data.dropna()
        df.reset_index(inplace=True)
        self.data = df#update self.data to be the same dataframe without the null values and in reset index
        return None
        
    def get_unique_tags(self):
        '''
        returns a list of all the unique strings from the 'tags' column
        '''
        copypy = self.get_data()
        tags = copypy.loc[:,'tags']#new datagrame with 1 column-the tags column
        dictags = tags.to_dict()#dict of the tags column   
        lst = []
        for i in dictags:
            str_to_list = ast.literal_eval(dictags[i])#change str to list
            lst = lst[:]+str_to_list[:]
        lst2 = []
        #build a list of unique
        for j in lst:
            if j not in lst2:
                lst2.append(j)
        return lst2

    def add_duration_in_minutes(self,new_column_name):
        '''
        adds a new column called 'new_column_name' ​to the ​data attribute that shows the 'duration' value in minutes instead of seconds
        return None
        '''
        df = self.data
        df[new_column_name] = ((df['duration'])/60).astype("int64")
        self.data = df
        return None
        
    def filter_by_row(self,column_name,threshold):
        '''
        returns a subset of the data attribute with all the rows that their column_name values exceed the threshold
        '''
        copypy = self.get_data()
        filtered = copypy[copypy[column_name]>threshold ]
        return filtered
