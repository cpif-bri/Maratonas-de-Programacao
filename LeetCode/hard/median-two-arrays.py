class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        m=len(nums)
        if m == 0:
            return m
        if m % 2 == 0:
            index = m // 2
            median = (nums[index] + nums[index-1]) / 2
        else:
            median = float(nums[m//2])
        return median