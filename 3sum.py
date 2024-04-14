def threeSum(nums:list[int]) -> list[list[int]]:
    arr = []
    for i in nums:
        for j in nums:
            arr.append([i])
    counter = 0
    counterNums = 0
    while counter < len(arr):
        if counterNums >= len(nums):
            counterNums  = 0
        arr[counter].append(nums[counterNums])
        counterNums += 1
        counter += 1
    counter = 0
    counterNums = 0
    while counter < len(arr):
        if counterNums >= len(nums):
            counterNums  = 0
        arr[counter].append(nums[counterNums])
        counterNums += 1
        counter += 1
    finalArr = []
    for i in arr:
        i.sort()
        if sum(i) == 0 and i not in finalArr:
            finalArr.append(i)
    return finalArr

print(threeSum([-1,0,1,2,-1,-4]))



