import random
biomorphe = []
biomorphe=[1, 1, 0, 0, 0]
dec1 = []
dec2 = []

def evolut(dec):
    global biomorphe, dec1, dec2

    # Copie la biomorphe originale dans dec1 et dec2
    dec1 = biomorphe.copy()
    dec2 = biomorphe.copy()

    # Choisit un index aléatoire
    index = random.randint(0, len(biomorphe) - 1)
    change = random.randint(-1, 1)

    if index == 0:
        if biomorphe[index] + change == 5:
            dec1[index] = 4
        elif biomorphe[index] + change == 0:
            dec1[index] = 1
        else:
            dec1[index] = biomorphe[index] + change
    else:
        if biomorphe[index] + change == 4:
            dec1[index] = 3
        elif biomorphe[index] + change == -1:
            dec1[index] = 0
        else:
            dec1[index] = biomorphe[index] + change
    # Choisit un index aléatoire
    index = random.randint(0, len(biomorphe) - 1)
    change = random.randint(-1, 1)

    if index == 0:
        if biomorphe[index] + change == 5:
            dec2[index] = 4
        elif biomorphe[index] + change == 0:
            dec2[index] = 1
        else:
            dec2[index] = biomorphe[index] + change
    else:
        if biomorphe[index] + change == 4:
            dec2[index] = 3
        elif biomorphe[index] + change == -1:
            dec2[index] = 0
        else:
            dec2[index] = biomorphe[index] + change
    #print(dec1)
    #print(dec2)


def reproduct(dec):
    global biomorphe
    biomorphe = dec.copy()


def develope(genes):
    # Assurez-vous que la liste a au moins 5 éléments
    if len(genes) < 5:
        raise ValueError("La liste doit contenir au moins 5 éléments.")

    g1 = genes[0]
    g2 = genes[1]
    g3 = genes[2]
    g4 = genes[3]
    g5 = genes[4]

    grid = [[' ' for _ in range(40)] for _ in range(24)]
    
    x = 20  # Position x initiale
    y = 18   # Position y initiale en bas de la grille
    
    # Gène 2 détermine la longueur de la première branche
    # Gène 1 détermine l'angle de divergence

    #embranchement1 = position du premier embranchement
    embranchement1 = []
    embranchement2 = []
    embranchement3 = []
    embranchement4 = []
    embranchement5 = []
    embranchement6 = []
    embranchement7 = []

    for _ in range(g2):
        y -= 1
        grid[y][x] = 'g'
    embranchement1.append(y)
    embranchement1.append(x)


    # Dessiner les sous-branches en fonction des gènes 3 4 et 5
    if (g1 ==1):
        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            y -= 1
            grid[y][x] = 'g'
            embranchement2.append(y)
            embranchement2.append(x)
            embranchement3.append(y)
            embranchement3.append(x)
        for i in range(g4):
            y -= 1
            grid[y][x] = 'g'
            embranchement4.append(y)
            embranchement4.append(x)
            embranchement5.append(y)
            embranchement5.append(x)
            embranchement6.append(y)
            embranchement6.append(x)
            embranchement7.append(y)
            embranchement7.append(x)
        for i in range(g5):
            y -= 1
            grid[y][x] = 'g'

    elif (g1 ==2):
        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            y -= 1
            x -= 1
            grid[y][x] = 'g'
        embranchement2.append(y)
        embranchement2.append(x)

        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            y -= 1
            x += 1
            grid[y][x] = 'g'
        embranchement3.append(y)
        embranchement3.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            x -= 1
            grid[y][x] = 'g'
        embranchement4.append(y)
        embranchement4.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            y -= 1
            grid[y][x] = 'g'
        embranchement5.append(y)
        embranchement5.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            y -= 1
            grid[y][x] = 'g'
        embranchement6.append(y)
        embranchement6.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            x += 1
            grid[y][x] = 'g'
        embranchement7.append(y)
        embranchement7.append(x)

        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y -= 1
            grid[y][x] = 'g'
        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y += 1
            grid[y][x] = 'g'

        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y -= 1
            grid[y][x] = 'g'
        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y -= 1
            grid[y][x] = 'g'

        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y -= 1
            grid[y][x] = 'g'
        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y -= 1
            grid[y][x] = 'g'

        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y -= 1
            grid[y][x] = 'g'
        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y += 1
            grid[y][x] = 'g'

    elif (g1 ==3):
        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            x += 1
            grid[y][x] = 'g'
            embranchement2.append(y)
            embranchement2.append(x)

        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            x -= 1
            grid[y][x] = 'g'
            embranchement3.append(y)
            embranchement3.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            y += 1
            grid[y][x] = 'g'
            embranchement4.append(y)
            embranchement4.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            y -= 1
            grid[y][x] = 'g'
            embranchement5.append(y)
            embranchement5.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            y += 1
            grid[y][x] = 'g'
            embranchement6.append(y)
            embranchement6.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            y -= 1
            grid[y][x] = 'g'
            embranchement7.append(y)
            embranchement7.append(x)

        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            grid[y][x] = 'g'
        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            grid[y][x] = 'g'

        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            grid[y][x] = 'g'
        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            grid[y][x] = 'g'

        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            grid[y][x] = 'g'
        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            grid[y][x] = 'g'

        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            grid[y][x] = 'g'
        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            grid[y][x] = 'g'


    if (g1 ==4):
        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            y += 1
            x += 1
            grid[y][x] = 'g'
            embranchement2.append(y)
            embranchement2.append(x)

        x = embranchement1[1]  # Position x embranchement initiale
        y = embranchement1[0]   # Position y embranchement initiale
        for i in range(g3):
            y += 1
            x -= 1
            grid[y][x] = 'g'
            embranchement3.append(y)
            embranchement3.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            x += 1
            grid[y][x] = 'g'
            embranchement4.append(y)
            embranchement4.append(x)

        x = embranchement2[1]  # Position x embranchement initiale
        y = embranchement2[0]   # Position y embranchement initiale
        for i in range(g4):
            y += 1
            grid[y][x] = 'g'
            embranchement5.append(y)
            embranchement5.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            y += 1
            grid[y][x] = 'g'
            embranchement6.append(y)
            embranchement6.append(x)

        x = embranchement3[1]  # Position x embranchement initiale
        y = embranchement3[0]   # Position y embranchement initiale
        for i in range(g4):
            x -= 1
            grid[y][x] = 'g'
            embranchement7.append(y)
            embranchement7.append(x)

        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y += 1
            grid[y][x] = 'g'
        x = embranchement4[1]  # Position x embranchement initiale
        y = embranchement4[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y -= 1
            grid[y][x] = 'g'

        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y += 1
            grid[y][x] = 'g'
        x = embranchement5[1]  # Position x embranchement initiale
        y = embranchement5[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y += 1
            grid[y][x] = 'g'

        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x += 1
            y += 1
            grid[y][x] = 'g'
        x = embranchement6[1]  # Position x embranchement initiale
        y = embranchement6[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y += 1
            grid[y][x] = 'g'

        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y += 1
            grid[y][x] = 'g'
        x = embranchement7[1]  # Position x embranchement initiale
        y = embranchement7[0]   # Position y embranchement initiale
        for i in range(g5):
            x -= 1
            y -= 1
            grid[y][x] = 'g'

    for row in grid:
        print(''.join(row))
    # Affichage des valeurs des gènes
    print(g1, g2, g3, g4, g5)  # Assurez-vous que ces variables sont accessibles ici

evolut(biomorphe)

while True:
    choix = input("\nChoisissez le descendant à afficher (1 ou 2) ou a faire évoluer e1 ou e2 : ")
    if choix == "1":
        develope(dec1)

    elif choix == "2":
        develope(dec2)

    elif choix == "e1":
        reproduct(dec1)    
        evolut(biomorphe)
    elif choix == "e2":
        reproduct(dec2)    
        evolut(biomorphe)
    elif choix.lower() == "exit":
        break

    else:
        print("Choix invalide. Le biomorphe initial reste inchangé.")