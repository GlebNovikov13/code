a = [12, 5, 4, 3, 6]
for i in range(0, len(a)):
    for f in range(len(a) - 1, i, -1):
        if a[i] > a[f]:
            c = a[f]
            a[f] = a[i]
            a[i] = c
print(a)