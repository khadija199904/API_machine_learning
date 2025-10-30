# Prédiction du Risque de Maladie Cardiovasculaire
## Description du projet

Ce projet vise à prédire le risque de maladie cardiovasculaire à partir de données cliniques et biologiques collectées auprès de patients.
L’objectif est de construire, comparer et optimiser différents modèles de Machine Learning (Random Forest, XGBoost, etc.) pour classifier les patients en deux catégories :

- positive = sain
- negative = malade
---

## Structure du dataset
Le jeu de données contient des informations cliniques et biologiques permettant d’évaluer le risque cardiovasculaire.

| Colonne | Description | Type | Importance médicale |
|----------|-------------|------|----------------------|
| **age** | Âge du patient | Numérique | Facteur de risque important (le risque augmente avec l'âge) |
| **gender** | Sexe du patient (1 = Homme, 0 = Femme) | Binaire | Les hommes ont souvent un risque plus élevé avant 60 ans |
| **pressurehight** | Pression artérielle systolique | Numérique | Mesure la pression pendant la contraction du cœur |
| **pressurelow** | Pression artérielle diastolique | Numérique | Pression entre deux battements cardiaques |
| **glucose** | Taux de glucose sanguin | Numérique | Niveau élevé = risque de diabète et maladies cardiaques |
| **kcm** | CK-MB (enzyme cardiaque) | Numérique | Indicateur de lésions du muscle cardiaque |
| **troponin** | Troponine (protéine cardiaque) | Numérique | Marqueur clé d’infarctus du myocarde |
| **impluse** | Fréquence cardiaque | Numérique | Indique l’activité et l’état cardiaque général |
| **status** | Cible (positive = sain, negative = malade) | Catégorique | Variable à prédire |

---

## Étapes du partie machine learning 
- Exploration et analyse des données (EDA)
- Prétraitement et pipeline d'entraînement avec Scikit-learn
- Comparaison de plusieurs modèles : Random Forest et XGBoost
- Optimisation des hyperparamètres avec GridSearchCV
- Sauvegarde du meilleur modèle entraîné

## Structure du featureML
```bash
 API_machine_learning
│
├── data/
│   └── cardiovascular.csv                # Notre dataset
│
├── pipeline.py                           # Pipeline  (RandomForest & XGBoost)
├── pipeline_with_gridsearch.py           # Pipeline avec GridSearchCV
│
├── best_pipeline_XGBoost.pkl               # Meilleur modèle sauvegardé
├── best_pipeline_with_GS_RandomForest.pkl   # Meilleur modèle avec gridsearch sauvegardé 
│
├── requirements.txt                      # Dépendances du featureML
└── README.md                             # Ce fichier
```
### Résultats du pipeline 
 1 - Pipeline 

| Modèle | Accuracy | F1-Score |
|---------|-----------|-----------|
| Random Forest | 0.980 | 0.983 |
| XGBoost | 0.982 | 0.986 |

 2 - Pipeline avec GridSearchCV

| Modèle | Accuracy | F1-Score |
|---------|-----------|-----------|
| RandomForest | 0.980 | 0.983 |
| XGBoost  | 0.980 | 0.983 |

```bash
# Cloner le dépôt
git clone https://github.com/username/Cardiovascular_Prediction.git
cd Cardiovascular_Prediction

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement pour Windows

venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

```

