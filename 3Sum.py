def quickSort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    else:
        lower = []
        greater = []
        base = nums[0]

        for i in range(1,len(nums)):
            if nums[i] >= base:
                greater.append(nums[i])
            else: 
                lower.append(nums[i])
        return quickSort(lower) + [nums[0]] + quickSort(greater)

def threeSum(nums):
    result = []
    numz = quickSort(nums)
    
    for i in range(len(numz)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        y = i+1
        z = len(numz) - 1
        while y < z:
            sums = numz[i] + numz[y] + numz[z]
            if sums > 0:
                z -= 1
            elif sums < 0:
                y += 1
            else:
                result.append([numz[i], numz[y], numz[z]])
                while y < len(numz)-1 and numz[y] == numz[y+1]:
                    y += 1
                while z >0 and numz[z] == numz[z-1]:
                    z -= 1
                y += 1
                z -= 1    
    return result

print(threeSum([0,0,0]))



    
