# Quantum Bird
Quantum Bird est un jeu de style *Flappy Bird* où le but est d'accumuler le plus de points possible en passant à travers les tuyaux. Cependant, faites gardes aux effects quantiques! Contrôlez plusieurs oiseaux représentant des qubits et voyez les effets de la superposition, l'intrication et la mesure en jeu!

# Installation
Pour installer le jeu, il suffit de cloner le dépôt GitHub. Ensuite, vous devez avoir `python` d installé (3.14 fonctionne, pas testé pour d'autres versions). Par la suite, installez les bibliothèques requises avec votre système de bibliothèque préféré, ou
```
python -m venv .venv
```
suivi de 
```
# Windows
.venv\Scripts\activate
```
```
# Linux (bash)
source .venv/bin/activate
```
et
```
pip install -r requirements.txt
```

# Distinctions importantes
Dans le jeu, il peut exister plusieurs qubits, qui sont différenciés par la couleur. L'état de ces qubits sont représenté par un ou plusieurs oiseaux qui ont tous la même couleur. Seul les tuyaux ayant la même couleur que les oiseaux peuvent faire perdre la partie.

# Contrôles
Lors du début de la partie, vous pourrez contrôler un qubit (groupe d'oiseau de la même couleur). Plus la partie avancera, plus vous aurez des chances de pouvoir controller plusieurs qubits. Pour se faire, vous pouvez utiliser les chiffres *0-9*, avec les chiffres les plus a gauches pour les plus anciens qubits. Aussi, la barre *espace* permet de faire sauter tous les qubits en même temps. Vous pouvez aussi faire pause avec la touche *p*.

# Points
Chaque oiseau passant un tuyaux augmente le pointeur de points de 1.

# Effets
Après avoir atteint un score de 3, des effets apparaissent à un interval régulier. Ces effets font différentes actions sur les oiseaux (qubits) :

| Nom | Representation | Effet |
| --- | -------------- | ----- |
| Porte H | H | Met l'oiseau qui touche l'effet en superposition, c'est-à-dire qu'un autre oiseau contrôllé par la même touche et avec une gravité oposé apparaitera. |
| Porte X | X | Inverse la gravité de l'oiseau qui touche l'effet |
| Mesure | Mètre | Observe l'oiseau qui touche l'effet, c'est-à-dire que l'oiseau pert son effet quantique. L'oiseau disparait du jeu, et les autres oiseaux ont la touche qui les contrôle déplacé de 1 vers la gauche. |
| Nouveau oiseau | Boule bleue | Ajoute un qubit au jeu avec une autre couleur et une autre touche qui contrôle l'oiseau. |
| Porte CX | X avec deux couleurs | Inverse la gravité du qubit ayant la couleur du bas seulement si un oiseau choisit aléatoirement avec la couleur du haut a sa gravité inversée. |
