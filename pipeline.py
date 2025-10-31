from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score ,f1_score
from xgboost import XGBClassifier
from Functions import Charge_data, clean_data, Encode_df, split_data


import joblib





#  Charger et préparer les données 
df = Charge_data("Cardiovasculaires_Data.csv")
df = clean_data(df)
df = Encode_df(df, col='status')
X_train, X_test, y_train, y_test = split_data(df, 'status')

#  Création un Pipeline Scikit-learn


numr_cols = ['age','gender','pressurehight','pressurelow','glucose','kcm','troponin','impluse']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numr_cols)]
    )  
# les modèles
models = {
'RandomForest': RandomForestClassifier(class_weight='balanced',random_state=42),
'XGBoost': XGBClassifier(random_state=42)
}

    
# --- Entraînement et évaluation pour chaque modèle ---
best_model = None
best_score = 0
best_name = ""

for name, model in models.items():
    print(f"\n**** {name} ****")
    clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
      ])
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print( 'Accuracy: %.3f' % accuracy )
    F1 = f1_score(y_test, y_pred, average='binary')
    print('F1_Score: %.3f' % F1)

    # Sauvegarder le meilleur modèle selon F1
    if F1 > best_score:
        best_score = F1
        best_model = clf
        best_name = name


print(f"\n Meilleur modèle : {best_name} avec F1 = {best_score:.3f}")

# sauvgarder le best model avec joblib 
joblib.dump(best_model, f"best_pipeline_{best_name}.pkl")
print(f"Modele sauvegardé '")

