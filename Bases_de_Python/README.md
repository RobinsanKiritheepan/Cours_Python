# 🐍 Bases de Python

Le socle avant l'IA : de la variable `a = 3` jusqu'à **pandas**.

## 📂 Contenu

| Dossier | Description |
|---|---|
| **[01_Exercices_originaux](01_Exercices_originaux/)** | Les notebooks `day1` → `day5` tels que je les ai faits en cours |
| **[02_Cours_detaille](02_Cours_detaille/)** | Les mêmes, **annotés en français** : chaque notion expliquée, chaque piège signalé |
| **[PowerPoints](PowerPoints/)** | Le support de présentation qui résume les 5 jours |

## 📚 Le programme

| Notebook | Notions |
|---|---|
| `day1` | types (`int`/`float`/`bool`/`str`), opérateurs, `math`, erreurs & exceptions, fichiers |
| `day1_2` | conditions `if`/`elif`/`else`, `match`, ternaire, f-strings *(exercices à trous)* |
| `day2` | chaînes, listes, tuples, boucles, **fonctions**, générateurs (`yield`) |
| `day3` | dictionnaires, `*args`/`**kwargs`, **POO** (classes, héritage) |
| `day4` | `enumerate`/`zip`, **décorateurs**, walrus `:=`, **matplotlib** |
| `day5` | **pandas** : DataFrame, `iloc`/`loc`, filtres, `groupby`, valeurs manquantes |

## 🎯 Les pièges classiques couverts

- `b = a` sur une liste **ne copie pas** → il faut `.copy()`
- `elif` ≠ deux `if` séparés
- `file.close` sans parenthèses ne ferme rien
- Un notebook correct passe le **« Restart & Run All »**
