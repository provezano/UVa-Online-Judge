import sys


# { 15, 27, 14, 38, 26, 55, 46, 65, 85 }

def sumBoxes(boxes):
    listSums = [sum(box) for box in boxes]
    return [i[0] for i in sorted(zip(boxes, listSums), key=lambda l: l[1])]


def sortBoxes(boxes):
    return [sorted(box) for box in sumBoxes(boxes)]


def comp(box1, box2):
    for i in range(len(box1)):
        if (box1[i] >= box2[i]):
            return 0

    return 1


def LIS2(boxes):
    list = [[] for i in range(len(boxes))]

    list[0].append(boxes[0])

    for i in range(1, len(boxes)):
        for j in range(0, i):
            if (comp(boxes[j], boxes[i])) and (len(list[i]) < len(list[j]) + 1):
                list[i] = list[j].copy()

        list[i].append(boxes[i])

    return list



def convert(boxes, list):
    listIndexes = []
    for i in list:
        listIndexes.append([boxes.index(x)+1 for x in i])
    return max(listIndexes, key=lambda x: len(x))

def LIS(boxes):
    list = [[] for i in range(len(boxes))]

    list[0].append(boxes[0])

    for i in range(1, len(boxes)):
        for j in range(0, i):
            if (boxes[j] < boxes[i]) and (len(list[i]) < len(list[j]) + 1):
                list[i] = list[j].copy()

        list[i].append(boxes[i])

    return list

def hopeItWorks(boxes):
    listBoxes = []
    for i in boxes:
        c = True
        count = 0
        for j in boxes:
            for d in range(len(i)):
                if (i[d] >= j[d]):
                    c = False
                    break

            if (c):
                count+=1
            else:
                c = True

        listBoxes.append([i, count])

    return [x[0] for x in sorted(listBoxes, key=lambda l: l[1], reverse=True)]

def main():

    for line in sys.stdin:
        boxes = []

        x,y = line.split()
        #print(x, y)

        for i in range(int(x)):
            readBox = [int(x) for x in sys.stdin.readline().split()]
            boxes.append(readBox)

        boxes = [sorted(box) for box in boxes]
        boxesCopy = boxes.copy()

        boxes = hopeItWorks(boxes)

        result = LIS2(boxes)
        result = convert(boxesCopy, result)

        print(len(result))
        print(" ".join([str(x) for x in result]))

if __name__ == "__main__":
    main()