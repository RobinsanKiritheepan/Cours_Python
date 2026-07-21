# Complet — les notebooks annotés

Chaque notebook de `01_Exercices_originaux/` repris **à l'identique**, avec des cellules
markdown intercalées : la théorie, les formules, la lecture des résultats et les pièges.

> ⚠️ **Le code n'est jamais modifié.** Pas une ligne. Seules des explications sont ajoutées
> entre les cellules. Si un bug est présent dans l'original, il est **expliqué** ici — pas
> corrigé. C'est voulu : on apprend mieux en voyant l'erreur et sa conséquence.

## Contenu

| Fichier | Original | Ce que tu y apprends |
|---|---|---|
| `S9_P2_Deep_Learning_cours_complet.ipynb` | S9_P2 | Les tout premiers pas : tenseurs, autograd, `nn.Module` + le journal des corrections GPU |
| `S9_P3_Deep_Learning_cours_complet.ipynb` | S9_P3 | L'escalier en 7 étages, de l'autograd à Lightning. **La boucle d'entraînement à la main** |
| `S9_P4_DL_cours_complet.ipynb` | S9_P4 | **Le pipeline complet** : données → split → scaler → `Dataset` → MLP → `Trainer` → courbes → évaluation |
| `S9_P5_DL_cours_complet.ipynb` | S9_P5 | Les **vraies données** (Air Quality UCI) : le nettoyage est le vrai travail |

## Par où commencer

| Ce que tu cherches | Va voir |
|---|---|
| Comprendre **l'autograd** et la boucle | `S9_P3` — c'est le cœur |
| Monter un **projet complet** | `S9_P4` — le squelette de tout projet DL |
| Gérer des **données sales** | `S9_P5` — le piège des `-200` |

## Les pièges expliqués dans ces notebooks

| Piège | Où | Pourquoi c'est vicieux |
|---|---|---|
| `training_step` sans `return loss` | S9_P3 | la perte reste **parfaitement plate** — rien ne plante |
| `SGD(pure_model.parameters())` | S9_P3 | l'optimiseur met à jour un réseau que Lightning n'utilise pas |
| `val_dataloaders=train_loader` | S9_P4 | tes deux courbes sont la **même** courbe |
| `r2_score(y_pred, y_true)` | S9_P4 | R² **n'est pas symétrique** — MAE et RMSE pardonnent, pas lui |
| `fit_transform(X_val)` | S9_P4 | fuite de données + deux échelles différentes |
| `dropna()` sur des `-200` | S9_P5 | **16 701** valeurs manquantes survivent au nettoyage |

**Leur point commun : aucun ne fait planter le code.** En deep learning, l'absence d'erreur
ne prouve rien.

Le code brut, sans annotation : [`01_Exercices_originaux`](../01_Exercices_originaux/)
Les supports de présentation : [`PowerPoints`](../PowerPoints/)
