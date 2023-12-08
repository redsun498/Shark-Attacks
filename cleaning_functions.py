import pandas as pd

def clean_rows_columns(df):
    df= df.drop(df.index[6920:])
    df= df.drop(['href formula','href', 'Case Number', 'Case Number.1',
       'original order', 'Unnamed: 21', 'Unnamed: 22'],axis=1)
    return df

def clean_column_names(df):
    df.columns = df.columns.str.lower()
    df = df.rename({'unnamed: 11':'killed'},axis =1)
    return df

def clean_invalid_values(df):
    dict_killed = {' N':'N', 'n':'N','N ':'N','y':'Y','Y x 2':'Y',2017:'N','Nq':'N',"M":'N','F':'Y'}
    df['killed'] = df['killed'].map(dict_killed).fillna(df['killed'])
    
    dict_type = {'Under investigation':'Questionable',     'Unverified':'Questionable','Unconfirmed':'Questionable','?':'Questionable','Boat':'Watercraft',"Invalid":'Questionable'}
    df['type'] = df['type'].map(dict_type).fillna(df['type'])
    
    return df 

def replace_with_dict(cell,my_replace_dict):
    if isinstance(cell,str):
        for key,value in my_replace_dict.items():
            if key in cell.lower().strip():
                return value
        return cell
    return cell

def whole_pipeline(df):
    df = clean_rows_columns(df)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    return df
