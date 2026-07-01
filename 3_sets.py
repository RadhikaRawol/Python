s = {1, 2, 3, 4, 5 ,55, 78, 90}

e = set()
print(s)
s.add(388)
print(s)
s.remove(55)
print(s)
s.discard(78)
print(s)

s1 = {1 , 2, 44, 67, 86 , 90}
s2 = {66 ,78 , 95 ,45, 30}
print(s1.union(s2))
print(s1.intersection(s2))