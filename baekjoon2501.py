def main():
    n,k = map(int, input().split())
    factors = getFactors(n)
    kFactor = factors[k-1] if len(factors) >= k else 0
    print(kFactor)

def getFactors(n):
    h = n
    factors = []
    for i in range(1, n+1):
        reminder = h%i
        if reminder != 0:
            continue
        factors.append(i)
    return factors

if __name__ == "__main__":
    main()