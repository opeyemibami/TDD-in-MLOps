import joblib
import pytest
from pathlib import Path as p
import os

import user_input
import load_artefact
import preprocessor
import feature_engineering


base_path = p(__file__).parent.parent.parent.absolute()
data_path = p.joinpath(base_path, "datasets","test.csv")
model,encoder = load_artefact.load_artefacts('lgbm_model.pkl','one_hot_encoder.pkl')
def pred():
    data = user_input.get_user_input(data_path)
    data = preprocessor.map_text_to_number(data)
    data = preprocessor.convert_features_type_to_int(data)
    data = preprocessor.drop_features(data)
    data = feature_engineering.one_hot_encode_date(data)
    data = feature_engineering.generate_new_feature(data)
    pred = model.predict(data)
    return pred




