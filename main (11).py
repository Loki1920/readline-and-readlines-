#readline()
f = open('s.txt','r')
d1 =f.readline()
d2 = f.readline()
d3 = f.readline()
print(d1,end='')
print(d2,end='')
print(d3,'\n')

#readlines
g = open('s.txt','r')
d = g.readlines()
print(d,'\n')
for i in d:
  print(i,end='')

