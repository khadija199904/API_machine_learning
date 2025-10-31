import pytest 
from Functions import Charge_data 
from pipeline import df
import pandas as pd


def test_load_data(df):
    
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    print("\n Le dataset est chargé avec succès !")
