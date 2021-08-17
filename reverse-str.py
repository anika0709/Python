
# reverse string

def reverse_str(str):
  """ this is a method to reverse a string. """
  try:
    for i in range(len(str)-1, -1, -1):
      print(str[i] , end = "")
  except Exception as e:
    print("Fix the {}". format(e))


str = "anika"

reverse_str(str)

#######
Another

def reverse_str(str):
  """ this is a method to reverse a string. """
  #try:
  str = list(str)
  left = 0
  right = len(str)-1
  while left < right:
    temp = str[left]
    str[left] = str[right] 
    str[right] = temp
    left = left +1
    right = right -1
  return str
 # except Exception as e:
  #  print("Fix the {}". format(e))
 
      
str = "AnikaR"

print(reverse_str(str))