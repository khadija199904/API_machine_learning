import pytest 

from pipeline import df



def test_load_data(df):
    
    assert not df.empty
    print("\n Le dataset est chargé avec succès !")
