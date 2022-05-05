
def findMedianSortedArrays(nums1, nums2) -> float:
    resultant_list = nums1 + nums2
    r = sorted(resultant_list)

    if len(r) % 2 != 0:
        before_middle = len(r) // 2
        median = r[before_middle]
        return median
    else:
        before_middle = len(r) // 2
        median = (r[before_middle] + r[before_middle - 1]) / 2
        return median

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))





