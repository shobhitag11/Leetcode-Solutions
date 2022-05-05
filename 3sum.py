nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1,-1,2],[-1,0,1]]

possible_triplets = []
string_list = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print(j)
        if j + 1 == len(nums):
            pass
        else:
            # if nums[i] != nums[j] and nums[j] != nums[j+1] and nums[i] != nums[j+1]:
            possible_triplets.append([nums[i], nums[j], nums[j+1]])
            string_list.append(str(nums[i])+str(nums[j])+str(nums[j+1]))

sum_of_triplets_is_zero = []
for triplets in possible_triplets:
    if sum(triplets) == 0:
        sum_of_triplets_is_zero.append(triplets)

print(sum_of_triplets_is_zero)




