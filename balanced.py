# Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

# Examples:

# Input : {[]{()}}
# Output : Balanced

# Input : [{}{}(]
# Output : Unbalanced

ip = "{[]{()}}"
input = "[{}{})"


def is_bal(exp):
  '''Find balanced parenthesis'''
  st = []
  op_l = ["{","(","["]
  cl_l = ["}",")","]"]

  for i in exp:
    if i in op_l:
      st.append(i)
    elif i in cl_l:
      pos = cl_l.index(i)
      if len(st) > 0 and op_l[pos] == st[len(st)-1]:
        #print(f'found,popping{op_l[pos]} from {st}')
        st.pop()
      else:
        return "UnBalanced"
  if len(st) == 0:
    return("Balanced")
  else:
    return("Unbalanced")

print(is_bal(ip))
print(is_bal(input))


def check(exp):
  open_tup = ('[{(')
  close_tup = (']})')
  map = dict(zip(open_tup,close_tup))
  print(map)
  queue = []
  for i in exp:
    if i in open_tup:
      queue.append(map[i])
    elif i in close_tup:
      if not queue or i != queue.pop():
        return "Unbalanced"
  if not queue:
    return ("Balanced")
  else:
    return ("UnBALA")


print(check(iput))
print(check(ip))





