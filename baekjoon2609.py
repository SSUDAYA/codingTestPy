def main():
    nums = getInput()
    leastCommonMultiple = getLeastCommonMultiple(nums)
    greatestCommonFactor = getGreatestCommonFactor(nums, leastCommonMultiple)
    
    printArr([leastCommonMultiple, greatestCommonFactor])
    return 0

def getInput():
    a, b = map(int, input().split())
    nums = [a, b]
    nums.sort()
    return nums

def getLeastCommonMultiple(nums):
    smaller = nums[0]
    bigger = nums[1]

    remainder = -1
    while remainder != 0:
        remainder = bigger%smaller
        bigger = smaller
        smaller = remainder

    return bigger

def getGreatestCommonFactor(nums, leastCommonMultiple):
    smaller = nums[0]
    bigger = nums[1]

    smallerShare = smaller//leastCommonMultiple
    biggerShare = bigger//leastCommonMultiple
    greatestCommonFactor = smallerShare * biggerShare * leastCommonMultiple

    return greatestCommonFactor

def printArr(arr):
    for i in arr:
        print(i, end = '\n')

if __name__ == '__main__':
    main()