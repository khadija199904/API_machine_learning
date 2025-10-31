import pytest 
from Functions import Charge_data 
import pandas as pd


def test_load_data():
    filepath = r"C:\Users\khadija\Desktop\API_machine_learning-1\Cardiovasculaires_Data.csv"
    df = Charge_data(filepath)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    print("\n Le dataset est chargé avec succès !")
