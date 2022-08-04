def main():
    n = int(input())
    nthFib = getFib(0, 0, 0, n)
    print(nthFib)

def getFib(prevFib, currFib, i, n):
    if i == 1:
        currFib = 1

    if i == n:
        return currFib
    
    prevprevFib = prevFib
    
    prevFib = currFib
    currFib = currFib + prevprevFib
    return getFib(prevFib, currFib, i+1, n)


if __name__ == "__main__":
    main()