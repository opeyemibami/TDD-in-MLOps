from utils.load_artefact  import load_artefacts

def test_load_artefacts():
    model,encoder = load_artefacts('lgbm_model.pkl','one_hot_encoder.pkl')
    assert model.random_state ==2020
    assert list(encoder.categories_[0])==[0, 1, 2]

