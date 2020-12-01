from src.utils import preprocessor 
from src.utils.user_input import get_user_input
from src.utils.load_artefact  import load_artefacts
from src.utils import feature_engineering
from pathlib import Path as p
import os
import numpy as np


base_path = p(__file__).parent.parent.parent.absolute()
data_path = p.joinpath(base_path, "datasets","test.csv")

data = get_user_input(data_path)
data = preprocessor.map_text_to_number(data)
data = preprocessor.drop_features(data)
data = preprocessor.convert_features_type_to_int(data)

ENCODED_FEATURES = ['Vehicle_Age_group_0','Vehicle_Age_group_1','Vehicle_Age_group_2']
NEW_FEATURE = 'AP_to_PSC'


enc_data =  feature_engineering.one_hot_encode_data(data)
def test_one_hot_encode_data():
    
    assert 'Vehicle_Age' not in enc_data.columns
    for feat in ENCODED_FEATURES:
        assert feat in enc_data.columns
        
def test_generate_new_feature():
    new_data =  feature_engineering.generate_new_feature(enc_data)
    assert NEW_FEATURE in new_data.columns
