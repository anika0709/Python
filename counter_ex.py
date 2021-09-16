from collections import Counter


s = Counter("mahikka")
print(s)
e= Counter(['a','b','a','c','d', 'c', 'b'])
print(Counter(['a','b','a','c','d', 'c', 'b']))
d = Counter({'a':1, 'b':2})
print(d)

# reference from Counter item
c = Counter(cats=4, dogs=7)
print(c)
print(c['cats'])
print(c['rat']) #Output 0, won't throw error
print(c.elements()) # output obj with addr
print(list(c.elements()))
print(set(c.elements()))

print(list(d.elements()))

#important
print(c.most_common(1))  # 1 most common element

print(e.most_common(3)).  # 3 most common, a,b,c= 2 all has same no of elements