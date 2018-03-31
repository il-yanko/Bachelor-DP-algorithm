#!/usr/bin/env python3
import random

def random2DArrayXY (Xsize,Ysize,minValue,maxValue):
    array = []
    # create a suitable array
    for i in range(Ysize):
        part = [0] * Xsize
        array.append(part)
    # fill the array with random numbers
    for i in range(Ysize):
        for j in range(Xsize):
            array[i][j] = random.randint(minValue, maxValue)
    return array

def print2DArray (array):
    Xsize = len(array[0])
    Ysize = len(array)
    for i in range(Ysize):
        string = '|'
        for j in range(Xsize):
            string += '  '
            string += str(array[i][j])
            if (array[i][j] >= 0):
                string += ' '
            string += '  |'
        print(string)

def dynamicProg (array):
    #in this method we found the best path from the lower left corner to the upper right
    Xsize = len(array[0])
    Ysize = len(array)
    # create a suitable array
    path = []
    for i in range(Ysize):
        part = [0] * Xsize
        path.append(part)

    # create the array of the text description of our path
    text = []
    for i in range(Ysize):
        part = ['-'] * Xsize
        text.append(part)

    # fill the dynamic array
    path[0][Xsize-1] = array[0][Xsize-1]
    for index in range(Xsize-1):
        #path for string [0;i]
        realIndex = index + 1
        revIndex = Xsize - 1 - realIndex
        path[0][revIndex] = path[0][revIndex+1] + array[0][revIndex]

    for index in range(Ysize - 1):
        # path for string [i;N-1]
        realIndex = index + 1
        path[realIndex][Xsize-1] = path[realIndex-1][Xsize-1] + array[realIndex][Xsize-1]

    for i in range (Ysize-1):
        for j in range (Xsize-1):
            iReal = i + 1
            jReal = j + 1
            jReversed = Xsize - 1 - jReal
            path[iReal][jReversed] = max(path[iReal - 1]   [jReversed],
                                         path[iReal - 1]   [jReversed + 1],
                                         path[iReal]       [jReversed + 1],
                                        ) + array [iReal][jReversed]

    #go backward pass
    notEnd = True
    x = 0
    y = Ysize - 1
    while (notEnd) :
        if((x == Xsize - 1) and (y == 0)):
            notEnd == False
            break
        if(x == Xsize - 1):
            y -= 1
            text[y][x] = '+'
            continue
        if(y == 0):
            x += 1
            text[y][x] = '+'#
            continue
        a = path[y - 1][x + 1]  # diagonal
        b = path[y - 1][x    ]  # up
        c = path[y    ][x + 1]  # right

        if ((a >= b) and (a >= c)):
            text[y - 1][x + 1] = '+'
            x += 1
            y -= 1
        elif (b >= c):
            text[y - 1][x    ] = '+'
            y -= 1
        else:
            text[y    ][x + 1] = '+'
            x += 1


    text[Ysize-1][0] = '+'
    text[0][Xsize-1] = '+'
    print("\nOur path:\n")
    #print all the path
    for i in range (Ysize):
        string = '|'
        for j in range(Xsize):
            string += '  '
            string += text[i][j]
            string += '  |'
        print(string)
    return path

lengthX = 4
lengthY = 7
myArray = random2DArrayXY(lengthX,lengthY,-1,2)
print("\nOur basic random array:\n")
print2DArray(myArray)
rez = dynamicProg(myArray)
print("\nResults of the dynamic programming:\n")
print2DArray(rez)


