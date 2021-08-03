# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Input: nums = [1,2,3,1]
# Output: true


def find_dupli(nums):
  dup = {}
  for i in range(len(nums)):
    if nums[i] in dup:
      return True
    else:
      dup[nums[i]] = i
  return False

nums = [1,2,3,1]
print(find_dupli(nums))

 # Method 2 -- Sorting
    # l =  len(nums)
    # if l < 2:
    #     return False
    # nums.sort()
    # for i in range(l-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    # return False
    
    # Method 3 -- Set solution for python
    numsSet =  set(nums)
    if len(nums) == len(numsSet):
        return False
    return True