# 🧠 Deep Learning

Le grand saut : fini les modèles tout faits de scikit-learn — avec **PyTorch**, on construit
le réseau brique par brique et on écrit sa propre boucle d'entraînement.

## 📂 Contenu

| Dossier | Description |
|---|---|
| **[01_Exercices_originaux](01_Exercices_originaux/)** | `S9_P2_Deep_Learning.ipynb` — les fondamentaux PyTorch |
| **[03_Cours_detaille](03_Cours_detaille/)** | Le même notebook, **annoté** (théorie + explications) |
| **[Google_Colab](Google_Colab/)** | Démo Colab — données servies par URL GitHub *(voir son README)* |
| **[PowerPoints](PowerPoints/)** | Le support de présentation |
| **Archives** | Sauvegarde d'avant l'adaptation GPU |

## 📚 Les notions couvertes

| Concept | Description |
|---|---|
| **Tenseur** | comme un array NumPy… mais qui peut aller sur le GPU (`.shape` = l'outil de debug n°1) |
| **Device** | `.to(device)` — rien ne part sur le GPU tout seul ; modèle **et** données au même endroit |
| **Autograd** | `requires_grad` + `.backward()` → les dérivées calculées automatiquement |
| **`nn.Module`** | `__init__` déclare les couches, `forward` décrit le chemin |
| **La boucle** | forward → loss → `zero_grad` → backward → step |

## ⚙️ Le GPU

Ce notebook tourne sur un **AMD Radeon 880M** via **ROCm** (`torch 2.9.1+rocm7.2.1`).
L'API garde le nom `cuda` — ROCm imite l'API NVIDIA, donc le code reste identique à un tuto CUDA.

### 🔴 La leçon la plus importante : le GPU est parfois PLUS LENT

Mesuré sur un réseau de **13 paramètres**, 200 epochs :

| Où | Temps |
|---|---|
| CPU | **111 ms** |
| **GPU** | **478 ms** ← 4× plus lent ! |

Ce n'est **pas un bug** : envoyer les données vers la carte coûte plus cher que le calcul
lui-même. Le GPU gagne sur les **CNN**, les **transformers** et les **batchs ≥ 32**
(sur une matmul 4096×4096, il est ×3,6 plus rapide).

> **`.to(device)` est un réflexe à prendre pour la suite, pas une optimisation pour aujourd'hui.**
