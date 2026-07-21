# Cours Python & Intelligence Artificielle

Parcours complet **des bases de Python jusqu'au Deep Learning** : notebooks d'exercices,
cours détaillés en français et supports de présentation.

> Chaque notebook existe en **deux versions** : l'exercice tel que je l'ai fait, et une
> version **annotée** où chaque cellule est expliquée (théorie, formules, lecture des résultats).

---

## Le contexte

Ce dépôt rassemble mon travail du **Barcelona Summer Course** (Northin), à Barcelone —
un programme d'été intensif *Computer science & IoT*, suivi du **15 juin au 7 août 2026**
(8 semaines) dans le cadre de ma formation d'ingénieur à l'**ENSEA**.

| Cours du programme | Durée | Où c'est dans ce dépôt |
|---|---|---|
| Introduction to Python & Python for AI | 1 sem. | [`Bases_de_Python/`](Bases_de_Python/) *(day1 → day5)* |
| Introduction to Machine Learning and Data Analysis | 1 sem. | [`Machine_learning/`](Cours_IA/Machine_learning/) *(S1 → S9, scikit-learn)* |
| AI and Deep Learning | 1 sem. | [`Deep_learning/`](Cours_IA/Deep_learning/) *(PyTorch, Lightning, CNN)* |
| Advanced Programming with Java | 2 sem. | [`Summer Course 2026/`](Summer%20Course%202026/) |

**Le rythme est intensif** : une notion par jour, du code écrit en direct pendant la
séance. C'est ce qui explique la forme de ce dépôt — mes fichiers de séance sont bruts
et parfois bancals, et j'ai pris le temps de les annoter **après coup** pour réviser.

### Pourquoi des annotations générées par IA

Pendant les séances, je code vite et je note peu. Plutôt que de relire du code nu des
mois plus tard, j'ai repris chaque notebook avec **Claude** pour y intercaler ce qui
manquait : la théorie derrière chaque cellule, les formules, comment lire les sorties,
et surtout **pourquoi mes erreurs étaient des erreurs**.

C'est un choix assumé : le code reste le mien, les explications viennent de l'IA. La
section **« Qui a écrit quoi »**, plus bas, détaille précisément ce qui relève de l'un
ou de l'autre — y compris les 4 notebooks où le code a réellement été corrigé.

---

## Sommaire

| Section | Contenu |
|---|---|
| **[Bases_de_Python](Bases_de_Python/)** | Les fondamentaux : types, listes, fonctions, POO, pandas *(day1 → day5)* |
| **[Cours_IA](Cours_IA/)** | Machine Learning *(S1 → S9)* + Deep Learning *(PyTorch)* |
| **[Archives](Archives/)** | Anciennes versions et doublons — conservés, non maintenus |
| **[Summer Course 2026](Summer%20Course%202026/)** | Support de cours d'été (Python, ML, Java) |

---

## Architecture

```
Cours_Python/
│
├── Bases_de_Python/               Les fondamentaux Python
│   ├── 01_Exercices_originaux/      day1 → day5 (mes exercices)
│   ├── 02_Cours_detaille/           les mêmes, annotés en français
│   └── PowerPoints/                 le support de présentation
│
├── Cours_IA/                      Intelligence Artificielle
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
├── Archives/                      anciennes versions, doublons
└── Summer Course 2026/            cours d'été
```

---

## La convention des dossiers numérotés

Le **numéro indique le statut**, pas l'ordre du cours :

| Dossier | Signification | Qui l'a écrit |
|---|---|---|
| `01_Exercices_originaux/` | Le notebook **tel que je l'ai écrit** en cours — jamais modifié après coup | **moi** |
| `02_Corrections/` | Les corrections **fournies avec le cours** | l'enseignant |
| `03_Cours_detaille/` · `Complet/` | Le **même code**, avec des explications intercalées : théorie, formules, lecture des résultats, pièges | **annotations générées avec Claude** |
| `04_Notebooks_solutions_perso/` | Versions corrigées / améliorées de mes exercices | moi, avec de l'aide |

## Par où commencer — lisez ceci

> ### Prenez la version `03_Cours_detaille/`
>
> C'est celle qui est **annotée** : chaque cellule y est expliquée (théorie, formules,
> lecture des résultats) et **les erreurs de mon code y sont identifiées et commentées**.
>
> ### ⚠️ Les `01_Exercices_originaux/` peuvent planter
>
> Ce sont **mes fichiers bruts, tapés en séance**. Je les laisse volontairement tels
> quels : ils contiennent mes fautes de frappe, mes contresens et parfois du code qui
> **ne s'exécute pas** (variable mal nommée, argument inversé, boucle trop lente…).
> Ne les prenez pas comme référence — prenez-les comme la trace de mon apprentissage.
>
> **Où trouver du code corrigé ?** Quelques notebooks seulement l'ont :
> `04_Notebooks_solutions_perso/` (2 fichiers) et les 4 exceptions listées plus bas.
> Partout ailleurs, l'erreur est **expliquée** dans la version annotée, mais le code
> reste tel que je l'ai écrit.

---

## Qui a écrit quoi

Ce dépôt mélange volontairement deux choses, et il vaut mieux le dire clairement :

- **Le code des exercices est le mien.** Tout ce qui est dans `01_Exercices_originaux/`
  a été tapé par moi pendant les séances, avec mes erreurs et mes tâtonnements. Ces
  fichiers ne sont **jamais** retouchés après coup — c'est la trace de mon apprentissage.

- **Les explications sont générées par IA.** Les dossiers `03_Cours_detaille/` et
  `Complet/` reprennent mon code et y ajoutent des cellules markdown rédigées avec
  **Claude** : théorie, formules, lecture des sorties, pièges rencontrés. C'est mon
  support de révision.

  ⚠️ **Important : annoté ne veut pas dire corrigé.** Sur 32 notebooks annotés,
  **28 gardent mon code à l'identique** — bugs compris. L'erreur y est **expliquée**
  dans le markdown, pas réparée dans le code. Les 4 restants contiennent en plus la
  correction appliquée :

  | Fichier | Ce qui a été modifié |
  |---|---|
  | `S9_P1_Unsupervised_learning` | `silhouette_score` avec `sample_size=2000` (sinon 11 s par itération), cellules réordonnées |
  | `S8_P2_KMeans_DBSCAN_Moons` | `noise=0.1` et DBSCAN réécrit — la version d'origine ne séparait pas les deux lunes |
  | `S9_P2_Deep_Learning` *(×2 : `03_` et `Complet/`)* | boucle d'entraînement allégée, `print` de débogage retiré, adaptation GPU |

  Dans tous les cas, **la version d'origine reste intacte** dans
  `01_Exercices_originaux/` — il suffit de comparer les deux fichiers pour voir la
  différence.

Les commits portant la mention `Co-Authored-By: Claude` correspondent à ce travail
d'annotation et de réorganisation — pas à l'écriture des exercices.

---

## La progression du cours

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

## Technologies

`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `seaborn` · `plotly` · `SHAP` · `PyTorch`

## Utilisation

Les notebooks lisent leurs données depuis le dossier `Data/` de leur section
(`pd.read_csv("../Data/fichier.csv")`) — ils s'exécutent directement après un clone.
