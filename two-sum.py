# nums = [2,7,11,15]
# target = 9
# Output = [0,1]

# nums = [3, 2, 4]
# target = 6
# output = [1, 2]

nums = [3, 3]
target = 6
Output= [0, 1]

def two_sum(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)

    return result


print(two_sum(nums, target))






