# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def shift_step(num,k):
  for i in range(0,k):
    last = num[-1]
    for i in range(0,len(num)-1):
      num[len(num)-1-i] = num[len(num)-2-i]
    num[0] = last
  return (nums)


nums = [1,2,3,4,5,6,7]
print(shift_step(nums,2))