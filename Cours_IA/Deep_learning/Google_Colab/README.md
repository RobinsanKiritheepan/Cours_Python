# Google Colab — test

Petit notebook pour **vérifier** que Colab marche, avant de lancer un vrai projet.
`Run All` et tu sais.

```
Google_Colab\
├── test_colab.ipynb        ← ouvre celui-ci
└── donnees\Advertising.csv ← ta source, poussée sur GitHub
```

## 📦 Comment les données circulent

**Une seule source de vérité : ton dépôt GitHub.** La même URL sur ton PC et sur Colab —
donc le même fichier, le même résultat, toujours. Aucun clic, `Run All` d'un bout à l'autre.

```
donnees/Advertising.csv  →  tu le pousses  →  le notebook le relit par son URL
```

`donnees/` est **ta source** : c'est là que tu déposes tes fichiers. Git les transporte,
l'URL les relit.

### ⚠️ La seule règle

> **Tu modifies un CSV dans `donnees/` → tu pousses avant de relancer.**

Sinon le notebook lit l'ancienne version, **sans rien dire**. C'est le prix d'une source
unique — et c'est aussi ce qui garantit que ton PC et Colab ne divergeront jamais.

### ⚠️ `donnees/` ne doit PAS être dans le `.gitignore`

Le notebook lit les CSV **par leur URL GitHub**. Les ignorer les retirerait du dépôt →
**404** → notebook cassé. C'est écrit dans le `.gitignore` du projet pour que personne
(moi compris) ne le fasse par réflexe.

## 🔒 Ça ne touche pas à ton Drive

Colab fait un simple téléchargement HTTP de 3,8 Ko, comme un navigateur. **Ton Drive n'est
jamais touché**, aucune autorisation demandée, rien monté.

### Ce qui ne marche PAS, et pourquoi

| | Pourquoi |
|---|---|
| `files.upload()` | Fenêtre **JavaScript** qui exige l'interface **web** de Colab. Dans VS Code : widget mort, cellule bloquée. Aucun contournement (c'est dans les *Known Issues* de l'extension). |
| `drive.mount()` | Monterait ton « Mon Drive » **en entier** — photos, vidéos, documents. Impossible de le limiter à un dossier. |
| Un chemin local depuis Colab | *« the remote Colab runtime cannot access local files »*. La machine Google est **vide** : seul le **code** part, pas ton dossier. |

> 💡 **Le réflexe** : avant de lancer un notebook que tu n'as pas écrit, cherche
> `drive.mount` dedans.
>
> Ce que tu as autorisé : [myaccount.google.com/permissions](https://myaccount.google.com/permissions)

## Se connecter au T4

Extension **`Google Colab`** requise (`Ctrl+Shift+X`, éditeur **Google**) — installée.

**`Select Kernel`** (en haut à droite) → `Select Another Kernel...` → `Colab` → connexion
Google → `Auto Connect`.

Si tu récupères un CPU : refais-le avec **`New Colab Server` → `GPU` → `T4`**.

> ⚠️ Le menu `Runtime → Change runtime type` n'existe **que sur le Colab web**. Dans
> VS Code, le GPU se choisit **à la création du serveur**.
>
> ℹ️ L'auth de l'extension a des bugs ouverts (`Exchange timeout exceeded`). Si ça coince,
> réessaie — ça finit par passer.

## Ce que le test vérifie

1. Où tu tournes (ton PC ou Colab)
2. Quel matériel tu as vraiment décroché
3. Que les données arrivent depuis GitHub
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

## ⚠️ Piège connu

Le noyau `Python (GPU ROCm)` **se fige au démarrage de temps en temps** (0 % de CPU).
Stack ROCm en preview. `Restart Kernel` et ça repart.

---

*Créé le 16/07/2026. Projet plus complet : `Documents\Projets\Colab\Projet_GPU\`.
GPU local : `Documents\Projets\pytorch-rocm\README.md`.*
