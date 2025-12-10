infV = 1.44
pages = 100
lines = 50
symbols = 25
bites = 4
V = bites*symbols*lines*pages
N = int(1024*1024*infV // V)
print("Количество книг, помещающихся на дискету:", N)
