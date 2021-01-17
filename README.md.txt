Sudoku
par Paul Coudert et Navannan Kulaveerasingam




INSTALLATION et LANCEMENT :
Télécharger dans un même dossier les fichies Sudoku.py , Grilles.txt , Points.txt , Sauvergarde.txt , Solutions.txt
Ouvrir le fichier Sudoku.py avec le logiciel Visual Studio Code.
Lancer le programme (Sudoku.py) avec la flèche verte en haut à droit ("Run python file in terminal")




REGLES et COMMANDES DU JEU :
Remplir les cases vides avec les chiffres de 1 à 9, de telle sorte qu'ils n'apparaissent qu'une fois par ligne, 
par colonne et par carré de 3x3 cases.
Lorsque vous lancez le jeu pour la première fois, 
tapez "non" et choisissez ensuite une difficulté en tapant la lettre correspondante.
Les commandes s'afficheront ensuite dans le terminal.




Exemples de commandes : 
378
Place le chiffre 3 à la 7ème ligne et à la 8ème colonne.

aide78
Affiche les chiffres qui peuvent être placé à la 7ème ligne 8ème colonne. (Sans comparaison avec la solution)

verif378
Permet de savoir si 3 est bien positionné à la 7ème ligne 8ème colonne. (Comparaison avec la solution)

exit
Sauvergarde votre partie en cours et ferme le jeu.


Le score est compté de la manière suivante : 
-5 par utilisations de la commande aide
-10 lorsque la commande verif vous annonce une faute dans votre sudoku
+50 lorsque vous avez fini le sudoku