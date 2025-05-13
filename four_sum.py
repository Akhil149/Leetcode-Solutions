'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)-3):
            if a>0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, len(nums)-2):
                if b>a+1 and nums[b] == nums[b-1]:
                    continue
                c = b+1
                d = len(nums)-1
                while c<d:
                    if c> b+1 and nums [c] == nums [c-1]:
                        c +=1
                        continue
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum < target:
                        c +=1
                    elif sum > target:
                        d -=1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c+=1
        
        return res
