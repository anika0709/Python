# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def shift_zero(nums):
  for i, n in enumerate(nums):
    if n == 0:
      nums.remove(n)
      nums.append(0)
  return nums

nums = [0,1,0,3,12]
print(shift_zero(nums))


# Best Soution

def shift_zero(nums):
  j = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      print(i,j, nums[i])
      nums[j],nums[i] = nums[i],nums[j]
      j= j + 1
      print(nums)
  return nums

nums = [0,1,0,3,12]
print(shift_zero(nums))
