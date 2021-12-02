# https://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
#I have a list of numbers. I also have a certain sum. The sum is made from a few numbers from my list (I may/may not know how many numbers it's made from). Is there a fast algorithm to get a list of possible numbers? Written in Python would be great, but pseudo-code's good too. (I can't yet read anything other than Python :P )

# Example

# list = [1,2,3,10]
# sum = 12
# result = [2,10]
# NOTE: I do know of Algorithm to find which numbers from a list of size n sum to another number (but I cannot read C# and I'm unable to check if it works for my needs. I'm on Linux and I tried using Mono but I get errors and I can't figure out how to work C# :(
# AND I do know of algorithm to sum up a list of numbers for all combinations (but it seems to be fairly inefficient. I don't need all combinations.)

# S == 0: The only subset of [] has sum 0, so it is a valid subset. Because of this, the function should return 1.
# S != 0: As the only subset of [] has sum 0, there is not a valid subset. Because of this, the function should return 0.
# Then, let's analyze the recursive case (i.e.: v[i:] is not empty). There are two choices: include the number v[i] in the current subset, or not include it. If we include v[i], then we are looking subsets that have sum S - v[i], otherwise, we are still looking for subsets with sum S. The function f might be implemented in the following way:

def f(v, i, S):
  if i >= len(v): 
    return 1 if S == 0 else 0
  count = f(v, i + 1, S)
  count += f(v, i + 1, S - v[i])
  return count

v = [1, 2, 3, 10, 9 ]
s = 12
print(f(v, 0, s))

