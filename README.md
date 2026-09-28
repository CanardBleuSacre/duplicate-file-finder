# duplicate-file-finder

Recherche récursivement les fichiers identiques grâce à leur taille puis à SHA-256. N’efface rien.

Python 3.10 ou plus récent.

## Exemple

```bash
python main.py ~/Documents
python main.py ~/Downloads
```

La recherche ne supprime aucun fichier.

Le script ignore les liens symboliques. Il traite les fichiers à la racine du dossier, sauf le détecteur de doublons et la sauvegarde qui parcourent les sous-dossiers.
