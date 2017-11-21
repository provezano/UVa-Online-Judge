import sys

def returnBlocks(blocksWorld, blocksWorldSubList, key):
    for block in reversed(blocksWorldSubList):
        blocksWorld[block][1].append(blocksWorld[key][1].pop())
        blocksWorld[block][0] = block
    return blocksWorld

def moveBlocks(blocksWorld, blocksWorldSubList, keyA, keyB):
    blocksWorld[keyB][1] += blocksWorldSubList
    for i in blocksWorldSubList:
        blocksWorld[keyA][1].pop()
        blocksWorld[i][0] = keyB;

    return blocksWorld

def loc(blocksWorld, block):
    return blocksWorld[block][0]

def sublistBlocks(blocksWorld, block, key):
    if (blocksWorld[key][1][-1] != block):
        return blocksWorld[key][1][blocksWorld[key][1].index(block)+1: len(blocksWorld[key][1])]
    else:
        return []

def sublistBlocks2(blocksWorld, block, key):
    return blocksWorld[key][1][blocksWorld[key][1].index(block): len(blocksWorld[key][1])]


def moveBlock(blocksWorld, a, b, c):
    keyA = loc(blocksWorld, a)
    keyB = loc(blocksWorld, b)
    sublistA = sublistBlocks(blocksWorld, a, keyA)

    if (keyA == keyB): return

    if (c == 1):
        returnBlocks(blocksWorld, sublistA, keyA)
        returnBlocks(blocksWorld, sublistBlocks(blocksWorld, b, keyB), keyB)

        blocksWorld[keyB][1].append(blocksWorld[keyA][1].pop())
        blocksWorld[a][0] = keyB
    elif (c == 2):
        returnBlocks(blocksWorld, sublistA, keyA)

        blocksWorld[keyB][1].append(blocksWorld[keyA][1].pop())
        blocksWorld[a][0] = keyB
    elif (c == 3):
        returnBlocks(blocksWorld, sublistBlocks(blocksWorld, b, keyB), keyB)
        moveBlocks(blocksWorld, sublistBlocks2(blocksWorld, a, keyA), keyA, keyB)
    else:
        moveBlocks(blocksWorld, sublistBlocks2(blocksWorld, a, keyA), keyA, keyB)
    return blocksWorld


def printBlocksWorld(blocksWorld):
    for k, v in blocksWorld.items():
        print(k, ":", sep="", end="")
        for value in v[1]:
            print(" ", value, sep="", end="")
        print()

def main():
    blocksWorld = {}

    n = int(input())
    for i in range(0, n):
        blocksWorld[i] = [i,[i]]

    for line in sys.stdin:
        split = line.split()
        if (len(split) > 1):
            a = int(split[1])
            b = int(split[3])

            if split[0] == 'move' and split[2] == 'onto':
                moveBlock(blocksWorld, a, b, 1)
            elif split[0] == 'move' and split[2] == 'over':
                moveBlock(blocksWorld, a, b, 2)
            elif split[0] == 'pile' and split[2] == 'onto':
                moveBlock(blocksWorld, a, b, 3)
            elif split[0] == 'pile' and split[2] == 'over':
                moveBlock(blocksWorld, a, b, 4)
            else:
                break

    printBlocksWorld(blocksWorld)


if __name__ == '__main__':
    main()
