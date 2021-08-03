# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [1,2,4,6,7,11,15]

def get_target(nums):
  for i in range(len(nums)):
    j = i+1
    while j < len(nums)-2:
      if nums[i] + nums[j] == 9:
        return ([i,j])
    ## not sorted array
    #  elif nums[i] + nums[j] > 9:
    #    break
      else:
        j += 1 

print(get_target(nums))


# leetcode way

def twoSum(nums,target):
  check = {}
  for i, num in enumerate(nums):
    print (num,check)
    if target-num in check:
      return ([check[target-num],i] )
    else:
      check[num] = i
nums1 = [2,7,11,15]
target = 9
print(twoSum(nums1,target))