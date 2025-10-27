from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier
from Functions import Charge_data, clean_data, Encode_df, split_data



#  Charger et préparer les données 
df = Charge_data('heart_disease_dataset.csv')
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
'RandomForest': RandomForestClassifier(random_state=42),
'SVC': SVC(probability=True, random_state=42),
'LogisticRegression': LogisticRegression(max_iter=1000, random_state=42),
'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
}
# --- Entraînement et évaluation pour chaque modèle ---
for name, model in models.items():
    print(f"\n--- {name} ---")
    clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
      ])
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))