import joblib
import pytest
from pathlib import Path as p


from src.utils.user_input import get_user_input

base_path = p(__file__).parent.parent.parent.absolute()
data_path = p.joinpath(base_path, "datasets","test.csv")

EXPECTED_FEATURES = ['id','Gender','Age','Driving_License','Region_Code','Previously_Insured',
            'Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage']

class TestGetUserInput(object):

    def test_data_dimension(self):
        """
        This function ensures that the type of data ingested into the sys
        is in the right dimension 
        """
        data = get_user_input(data_path) 
        assert data.ndim == 2

    def test_data_feature_names(self):
        """
        This function test if the ingetsed data have the features in the right order
        """
        data = get_user_input(data_path) 
        assert list(data.columns) == EXPECTED_FEATURES
