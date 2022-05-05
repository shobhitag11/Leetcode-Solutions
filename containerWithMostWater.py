# https://leetcode.com/problems/container-with-most-water/
def maxArea(height) -> int:

    # approach-1 O(n^2)
    #         maxarea = 0
    #         for i in range(len(height)):
    #             for j in range(i+1, len(height)):
    #                 width = j-i
    #                 maxarea = max(maxarea, min(height[i], height[j]) * width)
    #         return maxarea

    # approach-2 -> Two pointer Approach
    maxarea = 0
    left = 0
    right = len(height) - 1
    while left != right:
        width = right - left
        maxarea = max(maxarea, min(height[left], height[right]) * width)
        if height[left] > height[right]:
            right -= 1
        elif height[left] <= height[right]:
            left += 1
    return maxarea


