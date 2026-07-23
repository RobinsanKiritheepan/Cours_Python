# Prédiction des cartons jaunes — FIFA World Cup 2026

Projet de Machine Learning **supervisé et non supervisé** sur le jeu de données
*Player Performance* de la Coupe du Monde 2026. Objectif : prédire si un joueur
reçoit un **carton jaune** lors d'un match (`yellow_cards` : 0 = non, 1 = oui).

> **Le fil rouge du projet.** La cible est déséquilibrée (~90 % de 0, ~10 % de 1).
> C'est volontaire : ça oblige à raisonner en **précision / rappel / F1** plutôt
> qu'en simple *accuracy* — un modèle qui prédirait toujours « pas de carton »
> atteindrait déjà ~90 % d'accuracy sans rien apprendre.

---

## Contenu

| Fichier | Description |
|---|---|
| [`projet_ml_fifa.ipynb`](projet_ml_fifa.ipynb) | Le notebook complet, **annoté** (cellules markdown : théorie + lecture des résultats) |
| [`Rapport_ML_FIFA.pdf`](Rapport_ML_FIFA.pdf) | Rapport de synthèse (7 pages, figures commentées) |
| [`Presentation_ML_FIFA.pptx`](Presentation_ML_FIFA.pptx) | Support de présentation (11 slides) |
| [`resultats/`](resultats/) | Les figures générées + `interpretation.txt` |

---

## Démarche

**Préparation**
- 54 600 lignes × 75 colonnes, 1 248 joueurs, aucune valeur manquante.
- Encodage one-hot des variables catégorielles utiles ; identifiants et variables
  à forte cardinalité exclus.
- **Séparation train / test par joueur** (et non ligne par ligne) pour éviter la
  fuite de données : un même joueur apparaît ~44 fois.

**Partie 1 — Apprentissage supervisé**
- Arbre de décision · Forêt aléatoire · Gradient Boosting, réglés par `GridSearchCV`.
- Déséquilibre géré par `class_weight="balanced"` (forêt) et `sample_weight` (boosting).
- Métriques : matrice de confusion, accuracy, précision, rappel, F1, ROC-AUC.

**Partie 2 — Interprétabilité**
- Importance native vs **importance par permutation** (met en évidence le biais de cardinalité).
- **SHAP** : summary plot (global) + waterfall plot (un joueur).

**Partie 3 — Apprentissage non supervisé**
- **PCA** (réduction à 2 dimensions) · **KMeans** · **DBSCAN**.
- Les labels ne servent qu'à l'interprétation *a posteriori*.

---

## Résultats

| Métrique | Arbre de décision | Random Forest | Gradient Boosting |
|---|---|---|---|
| Accuracy | 0,816 | 0,661 | 0,643 |
| Précision | 0,100 | 0,116 | 0,111 |
| Rappel | 0,125 | **0,407** | **0,412** |
| F1-score | 0,111 | **0,181** | 0,175 |
| ROC-AUC | 0,506 | 0,546 | 0,543 |

**Conclusion.** Toutes les analyses convergent — corrélation quasi nulle, AUC ≈ 0,5,
importances minuscules, clustering sans lien avec la cible : **les cartons jaunes ne
sont pas prédictibles** à partir de ces variables. Le comportement disciplinaire dépend
probablement de facteurs absents du dataset (décision arbitrale, contexte du match).

C'est un résultat **cohérent et honnête** : un faible pouvoir prédictif, documenté par
une démarche rigoureuse, reste un résultat de data science valable.

---

## Stack

`Python` · `pandas` · `NumPy` · `scikit-learn` · `matplotlib` · `SHAP`

## Utilisation

Le notebook lit les données depuis `../Data/fifa_world_cup_2026_player_performance.csv`
(dossier `Data/` de la section Machine Learning).
