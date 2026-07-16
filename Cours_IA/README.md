# 🤖 Cours IA

Le parcours Intelligence Artificielle : du premier modèle de régression jusqu'aux réseaux
de neurones.

## 📂 Contenu

| Dossier | Description |
|---|---|
| **[Machine_learning](Machine_learning/)** | Les séances **S1 → S9** : régression, classification, arbres, forêts, clustering |
| **[Deep_learning](Deep_learning/)** | **PyTorch**, GPU (ROCm), Google Colab |
| **[PowerPoints](PowerPoints/)** | Le deck **général** qui couvre tout le cours |

## 🗺️ La progression

```
S1  Régression linéaire  ──►  S2  Régression multiple + classification
                                    │
S3  KNN & Naive Bayes  ◄────────────┘
     │
     └──►  S4  Arbres  ──►  S5  Multiclasse  ──►  S6  Forêts & boosting
                                                       │
S7  ROC/AUC & SHAP  ◄──────────────────────────────────┘
     │
     └──►  S8  Clustering  ──►  S9  Non supervisé réel  ──►  🧠 Deep Learning
```

## 🎯 Le fil rouge du cours

Toutes les séances tournent autour d'une même idée : **mémoire ≠ intelligence**.
Un modèle doit être évalué sur des données **jamais vues** (train/test), et l'`accuracy`
seule est trompeuse — surtout sur des classes déséquilibrées.
