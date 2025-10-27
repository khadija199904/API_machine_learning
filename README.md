#  Classification des Maladies Cardiaques
## 📘 Description générale

Ce jeu de données contient des **informations cliniques et biologiques** collectées auprès de patients afin de **déterminer le risque ou la présence d’une maladie cardiaque**.

Il est conçu pour des tâches de **classification supervisée** (positive = sain, negative = malade), et peut être utilisé pour entraîner, valider et comparer différents modèles de machine learning ou deep learning (Random Forest, Logistic Regression, Xgboost...).

---

## Structure du dataset

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

## Informations techniques

- **Nombre d’observations :** = 1319 patients  
- **Nombre de variables :** 9 colonnes  
- **Type de problème :** Classification binaire  

