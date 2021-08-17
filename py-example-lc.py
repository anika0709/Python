# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

# Add a prefix text to all of the lines in a string

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def output(nums):
  sum = max_val = 0
  for i in range(len(nums)-1):
    print("i is", i)
    j = i
    while j < len(nums):
      
      new_sum = sum + nums[j]
      print(sum, max_val, new_sum, i, j)
      j += 1
      if new_sum < 0:
        break
      if new_sum > max_val:
        max_val = new_sum
        sum = new_sum
        j += 1
  return max_val

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(output(nums))


