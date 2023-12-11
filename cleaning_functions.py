import pandas as pd

def clean_rows_columns(df):
    '''
    The function works to clean the rows and columns that are completely filled with null values
    '''
    df= df.drop(df.index[6920:])
    df= df.drop(['href formula','href', 'Case Number', 'Case Number.1',
       'original order', 'Unnamed: 21', 'Unnamed: 22'],axis=1)
    return df

def clean_column_names(df):
    '''
    The function formats the names of all the columns.
    '''
    df.columns = df.columns.str.lower()
    df = df.rename({'unnamed: 11':'killed'},axis =1)
    return df

def clean_invalid_values(df):
    '''
    The function creates dictionaries to replace invalid values (for example, misstyped or redundant)in the rows.  
    ''' 
    dict_killed = {' N':'N', 'n':'N','N ':'N','y':'Y','Y x 2':'Y',2017:'N','Nq':'N',"M":'N','F':'Y'}
    df['killed'] = df['killed'].map(dict_killed).fillna(df['killed'])
    
    dict_type = {'Under investigation':'Questionable',     'Unverified':'Questionable','Unconfirmed':'Questionable','?':'Questionable','Boat':'Watercraft',"Invalid":'Questionable'}
    df['type'] = df['type'].map(dict_type).fillna(df['type'])
    
    return df 

def replace_with_dict(cell,my_replace_dict):\
    '''
    This function will replace the cells in a column for the values in a dictionary.
    '''
    if isinstance(cell,str):
        for key,value in my_replace_dict.items():
            if key in cell.lower().strip():
                return value
        return cell
    return cell

def whole_pipeline(df):
    '''
    This function cleans the entire dataframe
    '''
    df = clean_rows_columns(df)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    return df
