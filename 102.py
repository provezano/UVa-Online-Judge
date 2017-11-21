import sys
import re
#import random
#import numpy as np
'''
def solve(binsMatrix):
    binsMatrixCopy = binsMatrix.copy()
    # rows = np.array([0,1,2])
    # cols = np.array([0,1,2])
    bins = {}

    for i in range(0, 3):
        xMax, yMax = np.unravel_index(np.argmax(binsMatrix), binsMatrix.shape)
        print(xMax, yMax, np.sum(binsMatrixCopy, 0))
        bins[xMax] = np.sum(binsMatrixCopy, 0)[yMax] - binsMatrixCopy[xMax][yMax]
        binsMatrix[xMax, :] = -1
        binsMatrix[:, yMax] = -1
    return bins
'''


def solve2(binsMatrix):
    availableRows = set([0,1,2])
    availableColumns = [0,1,2]
    min = 99999
    minTuple = []

    for iter1 in range(0, 3):
        for iter in range(0, len(availableColumns)):
            for i in availableRows[:-1]:
                for j in availableRows[+1:]:
                    aux = binsMatrix[i][availableColumns[iter]] + binsMatrix[j][availableColumns[iter]]
                    if (aux < min):
                        min = aux
                        minTuple = [[i,j], availableColumns[iter]]
    availableRows = availableRows - (availableRows - minTuple[0])


    return min

def generateSolutions():
    solutions = []
    setOfPossibilities = ['B', 'G', 'C']

    for i in setOfPossibilities:
        for j in setOfPossibilities:
            if j!=i:
                for w in setOfPossibilities:
                    if (w!=i and w!=j):
                        solutions.append([i,j,w])
    return solutions

def getIndex(letter):
    if   letter == 'B':
        return 0
    elif letter == 'G':
        return 1
    else:
        return 2

def sumColumns(binsMatrix):
    sum = [0,0,0]
    for i in range(0,3):
        for j in range(0,3):
           sum[i] += binsMatrix[i * 3 + j]

    return sum

def solve3(binsMatrix):
    solutions = generateSolutions()
    #print(solutions)
    colSums = sumColumns(binsMatrix)
    bins = {}
    finalState = []
    min = 9999999999

    for s in solutions:
        for i in range(0,3):
            row = getIndex(s[i])
            bins[i] = colSums[i] - binsMatrix[i * 3 + row]

        aux = sum(bins.values())
        print(s, aux)
        if (aux <= min):
            if (aux == min):
                #print(s, min, "EQUAL")
                if ''.join(s) < ''.join(finalState):
                    finalState = s
            else:
                finalState = s

            min = aux

        #print(s, min)


    return [min, finalState]

#def generateProblems(n):
#    solutions = []
#    max = 1001
#    min = 0
#    for i in range(0,n):
#       solutions.append([random.randint(min,max),random.randint(min,max),random.randint(min,max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max)])
#
#    return solutions

def printResult(result):
    print(''.join(result[1]), result[0])


def main():
    #file = open('test.txt', 'w')
    #for i in generateProblems(1000):
    #    file.write("%d %d %d %d %d %d %d %d %d\n" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
    #file.close()

    for line in sys.stdin:
        binsMatrix = [int(x) for x in line.split()]
        #for i in range(0, 3):
        #    for j in range(0, 3):
        #        print(binsMatrix[i * 3 + j]," ", end="")
        #    print()

        #print("Sum", sumColumns(binsMatrix))
        #print(binsMatrix[1*3+1])
            #np.transpose(np.array([int (x) for x in re.findall(r'\d+', line)]).reshape(3,3))
    #binsMatrix = np.array([10,90,16,78,1,2,3,100,1000]).reshape(3,3)
    #binsMatrix = np.transpose(np.array([5,10,5, 20,10,5, 10,20,10]).reshape(3, 3))
    #print(binsMatrix)
        printResult(solve3(binsMatrix))

if __name__ == '__main__':
    main()
