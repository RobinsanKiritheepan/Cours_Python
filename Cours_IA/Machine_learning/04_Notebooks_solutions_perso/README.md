# 04 — Mes solutions personnelles

Mes **propres versions corrigées**, quand un notebook d'origine avait un bug bloquant ou
un problème de performance.

| Notebook | Ce qui a été corrigé |
|---|---|
| `S2_P1T_Solution_EEG.ipynb` | Pipeline complet sur l'EEG : LogisticRegression, KNN (recherche du meilleur k), arbre, tableau comparatif |
| `S9_P1_corrige_silhouette.ipynb` | `silhouette_score` en O(n²) : **11 s par k** sur 28 638 lignes → **`sample_size=2000`** → 4 s pour toute la boucle |

👉 Les versions d'origine restent intactes dans [`01_Exercices_originaux`](../01_Exercices_originaux/).
