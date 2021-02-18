#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[7]:


def mother_of_tables(df,up = True):
    
    df.dropna(how='all',inplace=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True,inplace=True)
    
    new_columns = []
    types = list(df.dtypes)
    for i in range(len(df.columns)):
        if df.dtypes[str(df.columns[i])] != "object":
            df[str(df.columns[i])] = df[str(df.columns[i])].astype("str")
        if str(df.columns[i]).count("Unnamed") == 0:
            new_columns.append(df.columns[i])
        else:
            new_columns.append(new_columns[len(new_columns) - 1])
    
    new_values = []
    for row in range(len(df.values)):
        if list(df.values[row]).count("nan") == 0:
            new_values.append(df.values[row])
        else:
            new_row = []
            if row == 0:
                for val in range(len(df.values[row])):
                    if val == 0 or str(df.values[row][val]) != "nan":
                        new_row.append(df.values[row][val])
                    else:
                        new_row.append(new_row[len(new_row) - 1])
            else:
                for val in range(len(df.values[row])):
                    if val == 0:
                        if str(df.values[row][val]) != "nan":
                            new_row.append(str(df.values[row][val]))
                        else:
                            new_row.append(str(df.values[row-1][val]))
                    else:
                        if str(df.values[row][val]) != "nan":
                            new_row.append(str(df.values[row][val]))
                        else:
                            if up:
                                new_row.append(str(df.values[row-1][val]))
                            else:
                                new_row.append(new_row[len(new_row) - 1])
            new_values.append(new_row)
    
    end = pd.DataFrame(columns = df.columns,data = new_values)
    for i in range(len(end.columns)):
        if str(types[i]) != "object":
            end[end.columns[i]] = end[end.columns[i]].astype(str(types[i]))
    end.columns = new_columns
    
    return end

