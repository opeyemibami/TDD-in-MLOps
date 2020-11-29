import pandas as pd
import numpy as np


DROP_FEATURES = ['id','Region_Code', 'Vintage', 'Driving_License']


Gender_mapper = {'Male':1,'Female':0}
Vehicle_Age_mapper = {'> 2 Years':2,'1-2 Year':1,'< 1 Year':0}
Vehicle_Damage_mapper = {'Yes':1,'No':0}

def map_text_to_number(data):
    data['Gender'] = data['Gender'].map(Gender_mapper)
    data['Vehicle_Age'] = data['Vehicle_Age'].map(Vehicle_Age_mapper)
    data['Vehicle_Damage'] = data['Vehicle_Damage'].map(Vehicle_Damage_mapper)
    return data

def drop_features(data):
    data.drop(columns=DROP_FEATURES,axis=1,inplace=True)
    return data

def convert_features_type_to_int(data):
    for col in data.columns:
        data[col] = data[col].astype(np.int32)
    return data
