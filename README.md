# Jeu du Tic-Tac-Toe en Python

## Description

Ce projet est une implémentation simple du jeu classique Tic-Tac-Toe en Python en utilisant la bibliothèque NumPy. Deux joueurs (Joueur 1 et Joueur 2) s'affrontent pour placer alternativement leurs marques (X ou O) sur un plateau 3x3. Le premier joueur à aligner trois marques (horizontalement, verticalement ou en diagonale) remporte la partie.

## Fonctionnalités

- Placement des marques aléatoire pour les deux joueurs.
- Vérification des victoires en ligne, colonne et diagonale.
- Détection automatique des égalités (match nul).
- Affichage du plateau de jeu dans la console.

## Prérequis

- **Python 3.x**
- **NumPy** pour la manipulation du plateau de jeu.

### Installation de NumPy

Si tu n'as pas NumPy installé, tu peux l'ajouter via `pip` :

```bash
pip install numpy
```

## Comment exécuter le projet

1. **Cloner le dépôt GitHub** :
   ```bash
   git clone  https://github.com/SOULEYMANEHAMANEADJI/python-tic-tac-toe-01.git
   ```

2. **Se rendre dans le répertoire du projet** :
   ```bash
   cd python-tic-tac-toe
   ```

3. **Lancer le jeu** :
   ```bash
   python tic_tac_toe.py
   ```

Le jeu s'exécutera dans la console, affichant le plateau après chaque mouvement, puis annoncera le gagnant ou l'égalité à la fin.

## Fonctionnement du jeu

- Le jeu commence avec un plateau vide.
- À chaque tour, un emplacement aléatoire est choisi pour chaque joueur (1 ou 2).
- Le plateau est affiché après chaque mouvement.
- Le jeu se termine lorsqu'un joueur aligne trois marques ou que le plateau est plein (match nul).

## Exemple d'affichage

Voici un exemple de sortie dans la console :

```
Plateau après 1 mouvement:
[['X' ' ' ' ']
 [' ' ' ' ' ']
 [' ' ' ' ' ']]

Plateau après 2 mouvements:
[['X' 'O' ' ']
 [' ' ' ' ' ']
 [' ' ' ' ' ']]

...

Le gagnant est le joueur : 1
```

## Tests unitaires

Des tests unitaires ont été ajoutés pour vérifier le bon fonctionnement des principales fonctions du jeu (vérification des gagnants, placement aléatoire, etc.). Pour exécuter les tests, utilise la commande suivante :

```bash
python -m unittest test_tic_tac_toe.py
```

## Améliorations futures

- **Interface graphique (GUI)** : Ajouter une interface graphique en utilisant une bibliothèque comme `Tkinter` ou `Pygame`.
- **IA Minimax** : Implémenter une intelligence artificielle basée sur l'algorithme Minimax pour prendre des décisions optimales.
- **Saisie des joueurs** : Permettre aux joueurs de saisir manuellement leurs coups au lieu d'utiliser des mouvements aléatoires.
---
## Auteur : Mine HAS 
