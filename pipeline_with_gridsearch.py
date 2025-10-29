from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score ,f1_score
from xgboost import XGBClassifier
from Functions import Charge_data, clean_data, Encode_df, split_data
from sklearn.model_selection import GridSearchCV
import joblib





#  Charger et préparer les données 
df = Charge_data(r"C:\Users\khadija\Desktop\API_machine_learning-1\Cardiovasculaires_Data.csv")
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
'XGBoost': XGBClassifier(random_state=42)
}

def get_param_grid(name):
    if name == 'RandomForest':
        return { 
            
            'classifier__n_estimators' : [50 , 100, 200],
            'classifier__max_depth' : [None , 10,15]
        }
    if name == 'XGBoost' :
        return { 
            
            'classifier__n_estimators' : [50 , 100, 200],
            'classifier__max_depth' : [5, 10, 15],
            'classifier__objective': ['binary:logistic', 'binary:hinge']
            
        }
    


best_model = None
best_score = 0
best_name = ""

for name, model in models.items():
    print(f"\n**** {name} ****")

    # get paramet with fonction get param_grid 
    param_grid_model= get_param_grid(name)
    # pipline pour classification
    clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
      ])
    
    #  GridSearchCV pour pipeline
    grid_search = GridSearchCV(
    estimator=clf,
    param_grid=param_grid_model,
    cv=5,
    scoring='accuracy',
    n_jobs=1,
    )

    # Entraînement et évaluation 
    grid_search.fit(X_train, y_train)
    print(f"Best {name} Params:", grid_search.best_params_)
    y_pred = grid_search.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print( 'Accuracy: %.3f' % accuracy )
    F1 = f1_score(y_test, y_pred, average='binary')
    print('F1_Score: %.3f' % F1)

    # Sauvegarder le meilleur modèle selon F1
    if F1 > best_score:
        best_score = F1
        best_model = clf
        best_name = name



print(f"\nMeilleur modèle : {best_name} avec F1 = {best_score:.3f} et accuracy = {accuracy:.3f}")
# sauvgarder le best model avecgrid search avec joblib 
joblib.dump(best_model, f"best_pipeline_with_GS_{best_name}.pkl")
print(f"Modele sauvegardé '")


