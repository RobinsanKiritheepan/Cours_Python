# PowerPoints — Deep Learning

| Fichier | Notebook | Contenu |
|---|---|---|
| `11_Deep_Learning_PyTorch.pptx` | S9_P2 | Les fondamentaux PyTorch (tenseurs, **autograd**, `nn.Module`, la boucle d'entraînement) + le benchmark **CPU vs GPU** + une diapo « À retenir » |
| `12_S9_P3_PyTorch_Fondamentaux.pptx` | S9_P3 | L'escalier en 7 étages : tenseur → device → **autograd** → `nn.Module` → `DataLoader` → **la boucle** → Lightning. Et les 2 bugs qui se cachent l'un l'autre (`return loss` manquant, mauvais `.parameters()`) |
| `13_S9_P4_Lightning_Pipeline.pptx` | S9_P4 | Le **pipeline complet en 10 étapes** : données → split → scaler → `Dataset` → MLP → `Trainer` → courbes → évaluation. Plus : pourquoi le GPU est **plus lent** ici, et pourquoi `r2_score` n'est pas symétrique |

> Le S9_P5 (vraies données Air Quality) n'a pas encore son deck dédié : le notebook est en
> cours d'écriture. Son contenu est couvert dans le deck général.

Le deck **général** (tout le cours, 51 diapos) : [`Cours_IA/PowerPoints`](../../PowerPoints/).
