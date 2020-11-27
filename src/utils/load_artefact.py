import joblib
from pathlib import Path as p
import os


base_path = p(__file__).parent.parent.absolute()
artefact_path = p.joinpath(base_path, "artefacts")

def load_artefacts(model_name,encoder_name):
    """
    This func load saved artefacts during R&D such as model, encoder etc. 
    param: artefacts names 
    return: list of artefacts 
    """
    model = joblib.load(p.joinpath(artefact_path,model_name))
    encoder = joblib.load(p.joinpath(artefact_path,encoder_name))
    return [model,encoder]


