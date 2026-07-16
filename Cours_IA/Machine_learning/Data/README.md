# 📊 Data — les datasets

Toutes les données utilisées par les notebooks des dossiers `01_` à `06_`.

| Fichier | Utilisé par | Description |
|---|---|---|
| `Housing_2.csv` | S1, S2, S6 | Prix de maisons (545 lignes, 13 colonnes) — **régression** |
| `Advertising.csv` | S2, S4 | Budgets pub TV/radio/journaux → ventes (200 lignes) |
| `titanic.csv` | S2, S4 | Survie des passagers (1 309) — **classification binaire** |
| `MBA.csv` | S3, S4 | Admissions MBA (6 194) — **classes déséquilibrées 85/15** |
| `spambase.data` | S3 | 4 601 emails, 57 features — **détection de spam** |
| `fifa_world_cup_2026_player_performance.csv` | S5 | 54 600 lignes — **multiclasse** (4 postes) |
| `EEG-Eye-State.csv` | S5 | 14 980 mesures EEG — ⚠️ **série temporelle** (fuite de données !) |
| `credit_risk_dataset.csv` | S7, S9 | 32 581 demandes de prêt — **risque de défaut** |
| `Raisin_Dataset.csv` / `.xlsx` | — | 900 raisins, 7 mesures — classification binaire |
| `heart_disease_health_indicators_BRFSS2015.csv` | — | Indicateurs de santé |
| `housing_kaggle_original.csv` | — | California Housing (dataset Kaggle d'origine) |
| `area_vs_price.png` | S1 | Graphique exporté depuis un notebook |

## ▶️ Comment les notebooks y accèdent

```python
df = pd.read_csv("../Data/Housing_2.csv")          # depuis 01_, 02_, 03_, 04_, 05_
df = pd.read_csv("../../Data/credit_risk_dataset.csv")  # depuis Corrections_expliquees/
```
