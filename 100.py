import sys
'''
def crazyFuncV1(n, count = 0):
    number = n
    #print(int(number))
    if (number == 1): return count+1;

    if (number % 2 != 0):
        number = 3*n+1
        #print(number)
    else:
        number = n/2
        #print(number/2)
    return crazyFunc(number, count+1)
'''
def crazyFunc(n, dict):
    number = n
    count = 0

    while (number != 1):
        if (number in dict):
            return dict[number] + count;
        else:
            number = (number / 2) if (number % 2 == 0) else (3*number+1)
            count += 1

    return count + 1;

def main():
    dict =  {1:1}

    for line in sys.stdin:
        n1, n2 = line.split()
        n1 = int(n1)
        n2 = int(n2)

        maximumCycleLength = 0

        for i in range(n1 if n1 <= n2 else n2, n2+1 if n2 > n1 else n1+1):
            cycleLength = crazyFunc(i, dict)
            dict[i] = cycleLength
            if (maximumCycleLength < cycleLength):
                maximumCycleLength = cycleLength

        print("%d %d %d" % (n1, n2, maximumCycleLength))

if __name__ == '__main__':
    main()
