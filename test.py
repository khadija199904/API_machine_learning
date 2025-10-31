import pytest 
from Functions import Charge_data 



def test_load_data():
    filepath = "Cardiovasculaires_Data.csv"
    df = Charge_data(filepath)
    assert not df.empty
    print("\n Le dataset est chargé avec succès !")
