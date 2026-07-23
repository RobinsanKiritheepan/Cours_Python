# Prédiction du poste d'un joueur — FIFA World Cup 2026

Projet de Machine Learning **supervisé et non supervisé**. À partir des statistiques d'un joueur
sur un match, déterminer son **poste** : défenseur, attaquant, gardien ou milieu.

> **Continuité.** L'énoncé demande de reprendre le jeu de données **et la variable cible** de
> l'expérience précédente. Celle-ci était le notebook [`S5_P1_Fifa_Multiclasse`](../01_Exercices_originaux/S5_P1_Fifa_Multiclasse.ipynb),
> où `position` était déjà prédite par un arbre de décision, un KNN et un Naive Bayes —
> meilleur score alors obtenu : **89 % d'accuracy**.

---

## Résultats

| Métrique | Arbre de décision | Random Forest | Gradient Boosting |
|---|---|---|---|
| Accuracy | 0,914 | **0,958** | **0,958** |
| Précision (macro) | 0,918 | **0,961** | 0,960 |
| Rappel (macro) | 0,913 | 0,955 | **0,956** |
| F1 macro | 0,915 | **0,958** | **0,958** |
| ROC-AUC (OvR) | 0,960 | **0,997** | **0,997** |

**95,8 % de F1 macro** contre 89 % pour le KNN de S5 — et avec un split *plus strict* et une fuite
de données en moins. Le gain vient des modèles d'ensemble.

F1 par poste (Random Forest) : Défenseur 0,968 · Gardien 0,960 · Attaquant 0,956 · Milieu 0,948.

---

## Le résultat le plus intéressant

| Approche | Résultat |
|---|---|
| Prédiction **supervisée** du poste | **F1 macro 0,958** |
| **Pureté** des clusters non supervisés | **42,5 %** |

Le poste est donc **très prédictible**, mais **invisible en clustering**. Les silhouettes selon les
postes réels sont nulles voire négatives (PCA −0,008 · ICA +0,039 · t-SNE −0,017).

**Pourquoi ?** Le supervisé *sait quoi chercher* : on lui donne la réponse, il isole les quelques
variables discriminantes et les combine finement. Le non supervisé *suit la variance dominante* :
PCA et KMeans se laissent guider par ce qui varie le plus parmi les 69 variables — ici le **niveau
de performance** sur le match, pas le poste. Le signal existe, mais il est noyé.

> **L'absence de structure visible en clustering ne signifie pas l'absence de signal exploitable.**

---

## Une fuite de données identifiée et écartée

`jersey_number` détermine le poste de façon **déterministe** — les plages ne se chevauchent jamais :

| Poste | Numéros |
|---|---|
| Gardien | 1 – 3 |
| Défenseur | 4 – 12 |
| Milieu | 13 – 20 |
| Attaquant | 21 – 26 |

Une seule règle donnerait **100 % d'accuracy** sans rien apprendre du jeu. Le numéro est attribué
*parce que* le joueur occupe ce poste : ce n'est pas une caractéristique de son jeu. **Variable exclue.**

En revanche les statistiques de gardien (`saves`, `punches`, `clean_sheet`…) sont **conservées** :
ce sont de vraies actions de match. Déduire « ce joueur a fait des arrêts, donc c'est un gardien »
est un raisonnement valide.

---

## Contenu

| Fichier | Description |
|---|---|
| [`projet_poste_fifa.ipynb`](projet_poste_fifa.ipynb) | Le notebook complet, annoté (théorie + lecture des résultats) |
| [`Rapport_Poste_FIFA.pdf`](Rapport_Poste_FIFA.pdf) | Rapport de synthèse (10 pages, 11 figures commentées) |
| [`Presentation_Poste_FIFA.pptx`](Presentation_Poste_FIFA.pptx) | Support de présentation (15 slides) |
| [`resultats/`](resultats/) | Les figures générées + `interpretation.txt` |

---

## Démarche

**Préparation.** 54 600 lignes × 75 colonnes, 1 248 joueurs, aucune valeur manquante.
Exclusion des identifiants, des variables à forte cardinalité et de `jersey_number` (fuite).
Encodage one-hot de `preferred_foot`, `tournament_stage`, `match_result`.

**Séparation train / test par joueur.** Chaque joueur apparaît ~44 fois et **son poste ne change
jamais** : un split ligne par ligne laisserait le modèle mémoriser les joueurs. On sépare les
1 248 joueurs → 43 726 / 10 874 lignes, **zéro joueur en commun**. C'est le point que S5 ne traitait pas.

**Partie 1 — Supervisé.** Arbre, Random Forest, Gradient Boosting réglés par `GridSearchCV`
(`scoring="f1_macro"`, le déséquilibre étant de 3:1). Matrice de confusion, accuracy, précision,
rappel, F1, ROC-AUC one-vs-rest. Interprétation des confusions : l'erreur dominante est
**attaquant ↔ milieu** (239 cas), ce qui reflète une frontière tactique réellement continue.

**Partie 2 — Interprétabilité.** Importance native *et* par permutation — les deux concordent, sur
des variables au sens footballistique évident (`defensive_contribution`, `offensive_contribution`,
`creativity_score`, `total_goals_tournament`, `pass_accuracy`, `height_cm`). Puis SHAP : summary
plot pour la classe Gardien, waterfall plot pour un gardien individuel.

**Partie 3 — Non supervisé.** PCA, ICA et t-SNE comparés, puis KMeans et DBSCAN. La cible est
retirée des données avant standardisation — sans quoi l'analyse serait circulaire.

---

## Stack

`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `seaborn` · `SHAP`

## Utilisation

Le notebook lit les données depuis `../Data/fifa_world_cup_2026_player_performance.csv`.
