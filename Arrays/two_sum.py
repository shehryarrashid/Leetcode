'''
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
'''

def two_sum(nums: list,target: int) -> bool:
    
    nums.sort()
    
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False

print(two_sum([1, 2, 4, 6, 8, 9, 14, 15],10))