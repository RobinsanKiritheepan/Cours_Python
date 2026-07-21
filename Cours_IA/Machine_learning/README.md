# Machine Learning — S1 à S9

Le cœur du cours : construire, évaluer et comprendre des modèles de Machine Learning.

## Contenu

| Dossier | Description |
|---|---|
| **[01_Exercices_originaux](01_Exercices_originaux/)** | Les notebooks **tels que je les ai faits** en cours |
| **[02_Corrections](02_Corrections/)** | Les corrections **fournies avec le cours** |
| **[03_Cours_detaille](03_Cours_detaille/)** | Les mêmes notebooks, **annotés** : théorie, formules, lecture des résultats |
| **[04_Notebooks_solutions_perso](04_Notebooks_solutions_perso/)** | Mes propres versions corrigées |
| **[05_Brouillons](05_Brouillons/)** | Essais non aboutis |
| **[06_Ressources_externes](06_Ressources_externes/)** | Tutoriels tiers (pas mon travail) |
| **[Data](Data/)** | Tous les datasets |
| **[PowerPoints](PowerPoints/)** | Un deck par séance |

## Les séances

| Séance | Thème | Dataset | Notions clés |
|---|---|---|---|
| **S1** | Régression linéaire | Housing | EDA, moindres carrés, train/test, MAE & RMSE |
| **S2** | Régression multiple + 1ʳᵉ classification | Housing, Advertising, Titanic | coefficients, **sigmoïde**, matrice de confusion, baseline |
| **S3** | KNN & Naive Bayes | MBA, Spambase | distances, **classes déséquilibrées**, `balanced_accuracy` |
| **S4** | Arbres de décision | MBA, Titanic | **Gini**, profondeur, importance des variables, `class_weight` |
| **S5** | Multiclasse | FIFA 2026, EEG | `cat.codes`, matrice 4×4, sélection de features |
| **S6** | Forêts & boosting | Housing | **Random Forest**, GridSearchCV, élagage, **SHAP** |
| **S7** | Risque de crédit | Credit Risk | **Gradient Boosting**, courbe **ROC & AUC**, SHAP |
| **S8** | Clustering | Iris, moons | **KMeans**, **DBSCAN**, PCA, t-SNE, coude & silhouette |
| **S9** | Non supervisé réel | Credit Risk | clustering sur 28 638 vraies demandes de crédit |

## Les pièges rencontrés (et documentés)

| Piège | Séance |
|---|---|
| `fit(X_test, y_test)` — entraîné sur le test | S2 |
| `classification_report(y_pred, y_test)` — arguments **inversés** | S3 |
| Accuracy 84 % sur du 85/15 = **pire** que l'idiot | S3 |
| `idxmin()` renvoie l'**indice**, pas la valeur de k | S4 |
| Fuite temporelle : KNN à 98 % sur l'EEG | S5 |
| `max_depth=30` en boosting → 27 min de calcul | S7 |
| `silhouette_score` en O(n²) → `sample_size=2000` | S9 |

## Exécuter les notebooks

Les données sont dans [`Data/`](Data/) et lues via un chemin relatif :
```python
df = pd.read_csv("../Data/Housing_2.csv")
```
Aucune configuration nécessaire après un clone.
