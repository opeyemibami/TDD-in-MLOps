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

def convert_features_type_to_int(data):
    for col in data.columns:
        data[col] = data[col].astype(np.int32)
    return data

def drop_features(data):
    data.drop(columns=DROP_FEATURES,axis=1,inplace=True)
    return data



# def preprocess_data(dataframe,encoder):

#     data = get_input()

#     data = ft.feature_eng(dataframe=dataframe)

#     #One hot encoding
#     hot_encoded_data = one_hot_enc.transform(data[multi_cols])
#     d = pd.DataFrame(data=hot_encoded_data,columns=['cholesterol_normal','cholesterol_above_normal','cholesterol_well_above_normal','glucose_normal','glucose_above_normal','glucose_well_above_normal'],dtype=int ).reset_index(drop=True)
#     data.drop(columns=multi_cols,axis=1,inplace=True)
#     data = pd.concat(objs=[data,d],axis=1)

#     #scale numerical columns
#     scaler = scaler
#     scaled = scaler.transform(data[num_cols])
#     data[num_cols] = scaled
#     return data

