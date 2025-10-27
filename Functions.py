import pandas as pd 
from sklearn.model_selection import GridSearchCV, train_test_split



def Charge_data(filepath):
    df = pd.read_csv(filepath)
    return df 

def clean_data (df) :
     df_cleaned = df.copy()
    # Supprimer les doublons
     df_cleaned = df_cleaned.drop_duplicates()

     # Remplacer les valeurs manquantes
     for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:       # colonnes numériques
           df[col] = df[col].fillna(df[col].mean())
        else:                                           # colonnes catégorielles
           df[col] = df[col].fillna(df[col].mode()[0])

     return df_cleaned


def Encode_df(df,col = None ) : 
    df_encoded = df.copy()
    if df_encoded [col].dtype == 'object':
       df_encoded [col] = df_encoded [col].map({'positive': 1, 'negative': 0})  

       return df_encoded
    

    
def split_data (df,target) :
   
   X = df.drop(columns=[target]) 
   y = df[target]
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

   return X_train, X_test, y_train, y_test

