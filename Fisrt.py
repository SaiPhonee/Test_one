s = [int(i) for i in open('17_21416.txt')]
mn = sum(i for i in s if i < 0)
res = []
for i in range(len(s)-2):
    x,y,z = s[i], s[i+1], s[i+2]
    if max(x, y, z)*min(x, y, z) > mn:
        res.append(x+y+z)
print(len(res), max(res))
