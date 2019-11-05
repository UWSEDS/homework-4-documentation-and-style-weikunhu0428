"""
This module perfomrs three tests for given data frame
Check that all columns have values of the corect type.
Check for nan values.
Verify that the dataframe has at least one row.
"""
import pandas as pd
import numpy as np

def test_data_type():
    """
    Return True if all data type is same.

    Argument: dataframe
    Output: True if all data types in dataframe are same

    Test:
    Dataframe: all columns have same data type
    Output:True
    """
    data = {'Name':['Mike', 'Evan', 'Anna'], 'Age':[20, 30, 50]}
    df_test1 = pd.DataFrame(data=data)
    type_list = []
    for i in range(len(df_test1.columns)):
        columns = df_test1.iloc[:, i]
        type0 = type(columns[0])
        type_list.append(all(isinstance(columns[j], type0) for j in range(len(df_test1))))

    value = all(type_list)
    #assert value == True
    assert value



def test_nan():
    """
    Return True if there is NAN.
    Argument: dataframe
    Output: True if there is at least one NA in data frame

    Test:
    Dataframe: contains one nan data
    Output:True
    """
    data = {'Name':[np.nan, 'Evan', 'Anna'], 'Age':[20, 30, 50]}
    df_test2 = pd.DataFrame(data=data)
    value = all(-df_test2.isna())
    assert value

def test_at_least_one_row():
    """
    Retrun True if datafarme has at least one row.
    Argument: dataframe
    Output: True if there is at least one row data frame

    Test:
    Dataframe: dataframe with three rows
    Output:True
    """
    data = {'Name':[np.nan, 'Evan', 'Anna'], 'Age':[20, 30, 50]}
    df_test3 = pd.DataFrame(data=data)
    value = len(df_test3) >= 1
    assert value
