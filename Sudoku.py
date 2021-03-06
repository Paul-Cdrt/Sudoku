pts = 0

def OuvFichier() :#permet d'ouvrir les fichiers où se trouvent les grilles et solutions des sudokus
    print("Quel niveau de difficulté voulez-vous faire ? \n Facile = F \n Moyen = M \n Difficile = D \n Expert = E")
    niv = input()
    if niv == 'F' or niv == 'M' or niv == 'D' or niv == 'E':
        gl = open('Grilles.txt', 'r')
        sol = open('Solutions.txt', 'r')
        return gl.read() , sol.read() , niv          
    else :
        print("La commande rentrée n'a pas été comprise")
        return OuvFichier()
        
def OuvFichierSauv() :# permet d'ouvrir les fichiers de la partie sauvegardée
    sol = open('Solutions.txt', 'r')
    sauv = open('Sauvegarde.txt', 'r')
    points=open('points.txt','r')
    niv = sauv.read()[0]
    sauv.close()               #On referme le fichier pour réinitialiser le pointeur du fichier.
    sauv = open('Sauvegarde.txt', 'r')
    a , b, c = sauv.read() , sol.read(), points.read()       #On passe par des variables pour pouvoir fermer les fichiers car on a surtout besoin de refermer la sauvergarde si on veut pouvoir réécrir dedans ensuite.
    sauv.close()
    sol.close()
    points.close()
    return a , b , niv, c 

def tradSudo(abc,niv) :# les fichiers ouverts étant des chaînes de caractères, cela permet de les transformer en liste de liste
    sud = []
    sudo = [[],[],[],[],[],[],[],[],[]]
    k = 0
    verif =  False
    for i in abc :
        if i == niv :    # On lit tout le fichier et on s'arrête à la difficulté demandée en changeant la variable verif
            verif = True
            continue
        if len(sud) < 81 and verif == True and i != '\n' : #  <81 car c'est la taille d'un sudoku et on commence à 0. On commence à remplir la grille dès que verif vaut True, donc qu'on est bien à la bonne difficulté demandée
            sud.append(i)
    for i in sud :#les lignes suivante permettent de créer 9 listes qui correspondent aux lignes du sodoku.
        if len(sudo[k]) == 9 :
            k += 1
            sudo[k].append(i)
        else :
            sudo[k].append(i)
    return sudo

def est_sur_la_colonne(grille,j,k):#permet de savoir si un élément est sur la colonne
    for c in range(9) :
        if grille[c][int(j)] == k :
            return True
    return False

def est_sur_la_ligne(grille,i,k):#permet de savoir si un élément est sur la ligne
    for l in grille[int(i)] :
        if l == k :
            return True
    return False

def est_sur_bloc(grille,i,j,k):#permet de savoir si un élément est sur une matrice 3x3
    a,b=int(i/3),int(j/3)
    for n in range(3):
        for p in range(3):
            if grille[a*3+n][b*3+p] == k :
                return True
    return False

def numero_valide(grille,i,j,k):#permet de savoir les différentes possibilités pour une case (Déjà sur la ligne/colonne/dans la case 3x3) 
    if est_sur_la_colonne(grille,j,k)==False and est_sur_la_ligne(grille,i,k)==False and est_sur_bloc(grille,i,j,k)==False and grille[i][j] == '0' :
        return True
    return False

def aide(grille,i,j):#permet de proposer les différentes possibilités au joueur, c'est une aide au joeur
    L=['1','2','3','4','5','6','7','8','9']
    C=[]
    for q in L :
        if numero_valide(grille,i,j,q) == True :
            C.append(q)
    return C

def verif(solution,nbr,i,j) :#permet de verifier l'élément rentré par le joueur en le comparant à la solution
    if nbr == solution[int(i)][int(j)] :
        return True
    else :
        global pts
        pts += - 10
        return False

def main() :
    global pts
    print('Voulez-vous reprendre la partie sauvegardée ?\nOui / Non')
    var = input()
    if var == 'Oui' or var == 'oui' :# pour la partie enregistrée
        grillestr, solutionstr, niv, pointstr = OuvFichierSauv()
        pts += int(pointstr)
    else : #pour créer une nouvelle partie
        grillestr, solutionstr, niv = OuvFichier()
    solution = tradSudo(solutionstr,niv)   #On change les str en liste de liste
    grille = tradSudo(grillestr,niv)
    while '0' in grille[0] or '0' in grille[1] or '0' in grille[2] or '0' in grille[3] or \
     '0' in grille[4] or '0' in grille[5] or '0' in grille[6] or '0' in grille[7] or '0' in grille[8] :   #Avec cette condition on vérifier que le sudoku n'est pas déjà fini 
        h = 0                    #h nous permet de compter ce qu'on a déjà rempli 3 lignes dans la sudoku.
        for i in range(9) :
            print(str(grille[i][0]) + '  ' + str(grille[i][1]) + '  ' + str(grille[i][2]) + '  |  ' \
                 + str(grille[i][3]) + '  ' + str(grille[i][4]) + '  ' + str(grille[i][5]) +  '  |  ' \
                 + str(grille[i][6]) + '  ' + str(grille[i][7]) + '  ' + str(grille[i][8]))               #Mise en page
            h += 1
            if h % 3 == 0 and h != 9 :        #Ainsi avec h on démarque les cases 3x3 (Mise en page)
            
                print('________________________________ \n')
        print("\nListes des actions possibles : \
\nLes éléments entrés doivent être des chaînes de caractères donc entre guillemets \
\n\n Entrer un chiffre dans la grille : écrire le chiffre et sa position (LigneColonne) \
\n Demander de l'aide (sur une case) : Taper aide dans la console suivi de la position de la case \
\n Vérifier qu'un nombre est bien placé : Taper verif suivi du nombre et de la position \
\n Sauvergarder le sudoku (Effacera la sauvergarde précédente): Taper exit \
\n \n Votre score actuel est de", pts)        #On affiche toutes les commandes possibles
        inst = input()
        if 'aide' in inst :
            pts += -5
            print('la liste des possibilités pour cette case est :\n',aide(grille,int(inst[-2]) - 1,int(inst[-1]) -1))
        if 'verif' in inst :
            print(verif(solution,inst[-3],int(inst[-2]) - 1,int(inst[-1]) - 1))   #La machine comptant de 0 à 8, on fait -1 pour compter de manière naturelle pour nous.
        if len(inst) ==  3 :
            grille[int(inst[-2]) - 1][int(inst[-1]) - 1] = inst[-3]
        if inst == 'exit' :
            sauvstr = niv + '\n'
            for j in range(9) :
                for i in grille[j] :
                    sauvstr += i
            sauv = open('Sauvegarde.txt', 'w')
            sauv.write(sauvstr)
            sauv.close()            #On referme le fichier pour passer du mode lecture au mode écriture
            point= open('points.txt','w')
            point.write(str(pts))
            point.close()
            return None
        if solution == grille :
            print("BBBRRRAAAVVVOOO !!!")
            pts += 50
            print('Votre score de cette session est : ', pts , '\n Voulez-vous continuer ? \n Oui/Non')
            reponse = input()
            if reponse == 'oui' or reponse == 'Oui' :
                return main()

main()