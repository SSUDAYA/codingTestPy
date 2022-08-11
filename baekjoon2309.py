ALLDWARFNUM = 9
REALDWARFNUM = 7
TOTALHEIGHTS = 100

def main():
    allHeights = getHeights()
    realDwarfHeights = getRealDwarf(allHeights)
    printArray(realDwarfHeights)
    return 0

def getHeights():
    allHeights = [int(input()) for _ in range(ALLDWARFNUM)]
    allHeights.sort()
    return allHeights

def getRealDwarf(heights):
    exceptionIndexes = getExceptionIndexes()
    realDwarfHeights = []
    for expIdxs in exceptionIndexes:
        filteredHeights = filterArrByIdx(expIdxs, heights)
        totalHeights = sum(filteredHeights)
        if totalHeights != TOTALHEIGHTS:
            continue
        realDwarfHeights = filteredHeights
        break
    return realDwarfHeights

def filterArrByIdx(idxs, arr):
    filteredArr = arr[:]
    filteredArr.pop(idxs[1])
    filteredArr.pop(idxs[0])
    return filteredArr

def getExceptionIndexes():
    exceptionIndexes = []
    for i in range(ALLDWARFNUM):
        for j in range(1, ALLDWARFNUM - i):
            exceptionIndexes.append([i, i+j])
    return exceptionIndexes

def printArray(arr):
    for i in arr:
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()