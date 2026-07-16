# 🐍 Cours Python & Intelligence Artificielle

Parcours complet **des bases de Python jusqu'au Deep Learning** : notebooks d'exercices,
cours détaillés en français et supports de présentation.

> Chaque notebook existe en **deux versions** : l'exercice tel que je l'ai fait, et une
> version **annotée** où chaque cellule est expliquée (théorie, formules, lecture des résultats).

---

## 📑 Sommaire

| Section | Contenu |
|---|---|
| 🐍 **[Bases_de_Python](Bases_de_Python/)** | Les fondamentaux : types, listes, fonctions, POO, pandas *(day1 → day5)* |
| 🤖 **[Cours_IA](Cours_IA/)** | Machine Learning *(S1 → S9)* + Deep Learning *(PyTorch)* |
| 📦 **[Archives](Archives/)** | Anciennes versions et doublons — conservés, non maintenus |
| 🎓 **[Summer Course 2026](Summer%20Course%202026/)** | Support de cours d'été (Python, ML, Java) |

---

## 🗂️ Architecture

```
Cours_Python/
│
├── Bases_de_Python/              🐍 Les fondamentaux Python
│   ├── 01_Exercices_originaux/      day1 → day5 (mes exercices)
│   ├── 02_Cours_detaille/           les mêmes, annotés en français
│   └── PowerPoints/                 le support de présentation
│
├── Cours_IA/                     🤖 Intelligence Artificielle
│   ├── PowerPoints/                 le deck général (Python + ML + DL)
│   │
│   ├── Machine_learning/            S1 → S9 : régression, classification, clustering
│   │   ├── 01_Exercices_originaux/     mes notebooks
│   │   ├── 02_Corrections/             les corrections du cours
│   │   ├── 03_Cours_detaille/          version annotée (théorie + explications)
│   │   ├── 04_Notebooks_solutions_perso/  mes propres corrections
│   │   ├── 05_Brouillons/              essais non aboutis
│   │   ├── 06_Ressources_externes/     tutoriels tiers
│   │   ├── Data/                       tous les datasets
│   │   └── PowerPoints/                un deck par séance
│   │
│   └── Deep_learning/               PyTorch, GPU, Google Colab
│       ├── 01_Exercices_originaux/
│       ├── 03_Cours_detaille/
│       ├── Google_Colab/               démo Colab + données servies par URL
│       ├── Archives/
│       └── PowerPoints/
│
├── Archives/                     📦 anciennes versions, doublons
└── Summer Course 2026/           🎓 cours d'été
```

---

## 🔢 La convention des dossiers numérotés

Le **numéro indique le statut**, pas l'ordre du cours :

| Dossier | Signification |
|---|---|
| `01_Exercices_originaux/` | Le notebook **tel que je l'ai écrit** en cours — jamais modifié après coup |
| `02_Corrections/` | Les corrections **fournies avec le cours** |
| `03_Cours_detaille/` | Le **même notebook, annoté** : théorie, formules, lecture des résultats, pièges |
| `04_Notebooks_solutions_perso/` | Mes propres versions corrigées / améliorées |

👉 **Pour apprendre une notion** : ouvre `03_Cours_detaille/`.
👉 **Pour voir le code brut** : ouvre `01_Exercices_originaux/`.

---

## 📚 La progression du cours

| Séance | Thème | Notions clés |
|---|---|---|
| **day1 → day5** | [Bases Python](Bases_de_Python/) | types, listes, fonctions, POO, décorateurs, matplotlib, pandas |
| **S1** | Régression linéaire | EDA, moindres carrés, train/test, MAE & RMSE |
| **S2** | Régression multiple & classification | coefficients, sigmoïde, matrice de confusion |
| **S3** | KNN & Naive Bayes | distances, classes déséquilibrées, `balanced_accuracy` |
| **S4** | Arbres de décision | Gini, profondeur, importance des variables |
| **S5** | Multiclasse | encodage `cat.codes`, matrice 4×4, sélection de features |
| **S6** | Forêts & boosting | Random Forest, GridSearchCV, élagage, SHAP |
| **S7** | Risque de crédit | Gradient Boosting, courbe **ROC & AUC**, SHAP |
| **S8** | Clustering | KMeans, DBSCAN, PCA, t-SNE, silhouette |
| **S9** | Non supervisé réel + **Deep Learning** | clustering sur vraies données, **PyTorch** |

---

## 🛠️ Technologies

`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `seaborn` · `plotly` · `SHAP` · `PyTorch`

## ▶️ Utilisation

Les notebooks lisent leurs données depuis le dossier `Data/` de leur section
(`pd.read_csv("../Data/fichier.csv")`) — ils s'exécutent directement après un clone.
