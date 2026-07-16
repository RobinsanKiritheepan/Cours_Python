# Google Colab — test

Petit notebook pour **vérifier** que Colab marche, avant de lancer un vrai projet.
`Run All` et tu sais.

```
Google_Colab\
├── test_colab.ipynb        ← ouvre celui-ci
└── donnees\Advertising.csv
```

## 🔒 Ça ne touche pas à ton Drive

Tout est sur **ton disque C:**. Sur Colab, tu envoies le CSV **à la main**
(`files.upload()`) : Google ne voit que ce fichier, et **rien ne reste** après la session.

`drive.mount()` n'est **pas** utilisé — il monterait ton « Mon Drive » **en entier**
(photos, vidéos, documents), sans aucun moyen de le limiter à un dossier. C'est tout ou
rien.

> **Le réflexe** : avant de lancer un notebook que tu n'as pas écrit, cherche `drive.mount`
> dedans. S'il y est, il aura accès à **tout ton Drive** pendant qu'il tourne.
>
> Ce que tu as déjà autorisé :
> [myaccount.google.com/permissions](https://myaccount.google.com/permissions)

## Se connecter au T4

Extension **`Google Colab`** requise (`Ctrl+Shift+X`, éditeur **Google**) — installée.

**`Select Kernel`** (en haut à droite) → `Select Another Kernel...` → `Colab` → connexion
Google → `Auto Connect`.

Si tu récupères un CPU : refais-le avec **`New Colab Server` → `GPU` → `T4`**.

> ⚠️ Le menu `Runtime → Change runtime type` n'existe **que sur le Colab web**. Dans
> VS Code, le GPU se choisit **à la création du serveur**.

## Ce que le test vérifie

1. Où tu tournes (ton PC ou Colab)
2. Quel matériel tu as vraiment décroché
3. Que les données arrivent
4. Que le GPU **calcule** — détecter et s'en servir sont deux choses différentes
5. La vitesse, pour comparer entre noyaux

## 📊 Résultats mesurés le 16/07/2026

500 epochs, réseau de 161 paramètres :

| Noyau | Temps |
|---|---|
| `Python 3` (CPU) | **0,27 s** |
| `Python (GPU ROCm)` (Radeon 880M) | **1,09 s** ← **4× plus lent** |

Perte identique des deux côtés : 211,60 → 0,20.

**Le GPU est plus lent, et c'est normal.** 161 paramètres, c'est minuscule : envoyer les
données vers la carte coûte plus cher que le calcul. Il gagne sur les CNN, les
transformers, les batchs ≥ 32.

**Ce notebook ne sert pas à aller vite** — il sert à vérifier que la plomberie marche avant
que tu en aies besoin.

## ⚠️ Pièges connus

- Le noyau `Python (GPU ROCm)` **se fige au démarrage de temps en temps** (0 % de CPU).
  Stack ROCm en preview. `Restart Kernel` et ça repart.
- L'auth de l'extension Colab a des bugs ouverts (`Exchange timeout exceeded`).
- Sur Colab, `/content` est vidé à chaque fermeture : tu devras renvoyer le CSV.

---

*Créé le 16/07/2026. Projet plus complet : `Documents\Projets\Colab\Projet_GPU\`.
GPU local : `Documents\Projets\pytorch-rocm\README.md`.*
