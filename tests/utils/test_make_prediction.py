import joblib
import pytest
from pathlib import Path as p
import pandas as pd

from src.utils import user_input
from src.utils import load_artefact
from src.utils import preprocessor
from src.utils import feature_engineering

base_path = p(__file__).parent.parent.parent.absolute()
data_path = p.joinpath(base_path, "datasets","test.csv")
model,encoder = load_artefact.load_artefacts('lgbm_model.pkl','one_hot_encoder.pkl')

data = user_input.get_user_input(data_path)
data = preprocessor.map_text_to_number(data)
data = preprocessor.drop_features(data)
data = preprocessor.convert_features_type_to_int(data)
data = feature_engineering.one_hot_encode_data(data)
data = feature_engineering.generate_new_feature(data)


def test_pred():
    pred = model.predict(data)
    assert pred.size != 0  
    assert pd.Series(pred).value_counts()[0]==21181


