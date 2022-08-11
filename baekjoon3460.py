MAXBITLEN = 20

#create bit array
i = 1
numByLoc = [i]
for _ in range(MAXBITLEN-1):
    i = i*2
    numByLoc.append(i)

def main():
    nums = getInput()
    for num in nums:
        binaryLoc = getBinaryByDecimal(num)
        printArr(binaryLoc)

def getInput():
    len = int(input())
    nums = [ int(input()) for _ in range(len)]
    return nums

def getBinaryByDecimal(decimal):
    binaryLoc = []
    for i in range(MAXBITLEN-1, -1, -1):
        num = numByLoc[i]
        remain = decimal - num
        if remain < 0 :
            continue
        decimal = remain
        binaryLoc.append(i)

    binaryLoc.reverse()
    return binaryLoc

def printArr(arr):
    for i in arr:
        print(i, end = ' ')
    print()

if __name__ == '__main__':
    main()