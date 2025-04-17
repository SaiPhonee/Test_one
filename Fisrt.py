def divs(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if prost(i) and i % 1000 == 777:
                s.add(i)
            if prost(n//i)  and n//i % 1000 == 777:
                s.add(n//i)
    return sorted(s)

def prost(n):
    if n ==1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(55_000_000, 56_000_000):
    d = divs(i)
    if len(d)>0:
        print(i, d[0])