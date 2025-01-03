import random
def generate_maze(x, y):
    t = 0
    start_generated = False
    exit_generated = False
    for i in range(1, y+1):
        for j in range(1, x+1):
            if (j == 1 or j == x) and not(start_generated):
                if random.randint(t, x) == x:
                    print("S", end="")
                    start_generated = True
                    continue
                else:
                    t += 1
            elif (i == 1 or i == y) and not(exit_generated):
                if random.randint(t, y) == y:
                    print("E", end="")
                    exit_generated = True
                    continue
                else:
                    t += 1
            print("#", end="")
        print()
try:
    x = int(input("Entrez la largeur du labyrinthe : "))
    y = int(input("Entrez la longueur du labyrinthe : "))
    generate_maze(x, y)
except:
    pass