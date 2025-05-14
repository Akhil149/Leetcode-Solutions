'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        nums.sort()
        temp = pow(2,31) - 1
        res = 0
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k = len(nums)-1
            while j<k:
                if j> i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                if abs(target - (nums[i]+nums[j]+nums[k])) < temp:
                    temp = abs(target - (nums[i]+nums[j]+nums[k]))
                    res = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < target:
                    j += 1
                else:
                    return nums[i]+nums[j]+nums[k]
        return res