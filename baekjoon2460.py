STATIONNUM = 10

def main():
    inOutPsg = getInput()
    max = getMax(inOutPsg)
    print(max)

def getInput():
    inOut = [list(map(int, input().split())) for _ in range(STATIONNUM)]
    return inOut

def getMax(inOut):
    currPsg = 0
    maxPsg = currPsg
    for i in range(STATIONNUM):
        currInOutPsg = inOut[i]
        inPsg, outPsg = currInOutPsg
        currPsg = currPsg + outPsg - inPsg
        if currPsg > maxPsg:
            maxPsg = currPsg
    return maxPsg

if __name__ == "__main__":
    main()