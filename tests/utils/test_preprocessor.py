from src.utils import preprocessor 
from src.utils.user_input import get_user_input
from pathlib import Path as p
import os
import numpy as np

import pytest

base_path = p(__file__).parent.parent.parent.absolute()
data_path = p.joinpath(base_path, "datasets","test.csv")


#use pytest fixture to load dependencies
data = get_user_input(data_path)
raw_data = data.copy()

prep_data = preprocessor.map_text_to_number(data)
def test_map_text_to_number():
    assert set(list(prep_data['Gender'].unique()))==set([1, 0])
    assert set(list(prep_data['Vehicle_Age'].unique()))==set([2, 1, 0])
    assert set(list(prep_data['Vehicle_Damage'].unique()))==set([1, 0])

prep_data = preprocessor.drop_features(prep_data)
def test_drop_features():
    assert prep_data.shape[1]<raw_data.shape[1]

prep_data = preprocessor.convert_features_type_to_int(prep_data)
def test_convert_features_type_to_int():
    assert prep_data.dtypes.unique()[0]==np.int32
