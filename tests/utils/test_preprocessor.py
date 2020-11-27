# from . import feature_engineering as ft
# import pandas as pd

# num_cols = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'bmi']
# multi_cols = ['cholesterol', 'gluc']

# def preprocess_data(dataframe,scaler,one_hot_enc):

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

