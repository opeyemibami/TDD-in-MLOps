import pandas as pd
from utils.load_artefact  import load_artefacts

_,encoder = load_artefacts('lgbm_model.pkl','one_hot_encoder.pkl')

MULTI_CATEGORICAL_FEATURES = ['Vehicle_Age']
ENCODED_FEATURES = ['Vehicle_Age_group_0','Vehicle_Age_group_1','Vehicle_Age_group_2']

def one_hot_encode_date(data):
    hot_encoded_data = encoder.transform(data[MULTI_CATEGORICAL_FEATURES])
    hot_encoded_data_df =pd.DataFrame(data=hot_encoded_data,columns=ENCODED_FEATURES,dtype=int).reset_index(drop=True)
    data.drop(columns=MULTI_CATEGORICAL_FEATURES,axis=1,inplace=True)
    data = pd.concat(objs=[data,hot_encoded_data_df],axis=1)
    return data 

def generate_new_feature(data):
    data['AP_to_PSC'] = round(data['Annual_Premium']/data['Policy_Sales_Channel'])
    return data
