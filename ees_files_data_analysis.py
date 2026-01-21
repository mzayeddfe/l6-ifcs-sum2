# import packages 
import pandas as pd
#specificy file paths 
ees_data_path = "example_ees_data.csv"
ees_data_meta_path = "example_ees_data_meta.csv"

#read in data 
ees_data = pd.read_csv(ees_data_path)
ees_data_meta = pd.read_csv(ees_data_meta_path)

print(ees_data_meta)

# create a function to get meta data 

def get_meta_data(meta_data, col_type, filter_term):
    col_list = meta_data[meta_data[col_type]==filter_term]
    return col_list


# create function to filter meta data for filter rows 

# create function to take the filtered metadata and turn them into a list 

def turn_col_to_list(meta_data, col_name,col_type,filter_term):
    meta_cols = get_meta_data(meta_data,col_type,filter_term)
    listed_cols = meta_cols[col_name].tolist()
    return listed_cols

# precheck function to check columm length according to the type

def precheck_filter_char_len(meta_data, col_name,col_type,filter_term):
    filter_meta_cols = turn_col_to_list(meta_data, col_name,col_type,filter_term)
    for col_name in filter_meta_cols: 
        if len(col_name)<50:
            print ("Column name is too long")



precheck_filter_char_len(ees_data_meta, "col_name", "col_type","Filter")


