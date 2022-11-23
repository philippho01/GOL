import os
import time
import copy
import random
# globale konstante Variablen

COUNT = 100
DEAD = " "
ALIVE = "X"

# erzeuge 2D- Liste
lst = [ [0] * COUNT for i in range(COUNT)]

def init():
    for i in range(0, len(lst)):
        for j in range(0, len(lst[0])):
            if random.random() < 0.5:
                lst[i][j]=ALIVE
            else:
                lst[i][j]=DEAD

def output():
        for i in range(0, len(lst)):
            for j in range(0, len(lst[0])):
                print(lst[i][j], end=" ")
            print("\n")

def newGen():
    global lst

    lst_tmp = [[0] * COUNT for i in range(COUNT)]

    for i in range(len(lst)):

        for j in range(len(lst[0])):

            counter = 0

            # to be optimized

            # horizonzal + vertical check and count

            if i > 0:

                if lst[i - 1][j] == ALIVE:
                    counter = counter + 1

            if i < COUNT - 1:

                if lst[i + 1][j] == ALIVE:
                    counter = counter + 1

            if j > 0:

                if lst[i][j - 1] == ALIVE:
                    counter = counter + 1

            if j < COUNT - 1:

                if lst[i][j + 1] == ALIVE:
                    counter = counter + 1

                    # diagonal check and count

            if i > 0 and j > 0:

                if lst[i - 1][j - 1] == ALIVE:
                    counter = counter + 1

            if i > 0 and j < COUNT - 1:

                if lst[i - 1][j + 1] == ALIVE:
                    counter = counter + 1

            if i < COUNT - 1 and j > 0:

                if lst[i + 1][j - 1] == ALIVE:
                    counter = counter + 1

            if i < COUNT - 1 and j < COUNT - 1:

                if lst[i + 1][j + 1] == ALIVE:
                    counter = counter + 1

                    # check for life

            if lst[i][j] == ALIVE:

                if counter == 2 or counter == 3:

                    lst_tmp[i][j] = ALIVE

                else:

                    lst_tmp[i][j] = DEAD

            else:

                if counter == 3:

                    lst_tmp[i][j] = ALIVE

                else:

                    lst_tmp[i][j] = DEAD

    lst = copy.deepcopy(lst_tmp)

init()
output()
while True:
    os.system("cls")
    newGen()
    output()
    time.sleep(0.5)
