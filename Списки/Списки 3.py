mass = int(input())
fishermen = int(input())
a = []
b = []
for i in range(fishermen):
    #Масса каждого путешесвенника
    a.append(int(input()))

for o in range(len(a)):
    if a[o] + min(a) <= mass:
        b += [[a[o], min(a)]]
        a[o] += mass
        a[a.index(min(a))] += mass
    else:
        if a[o] > mass:
            continue
        else:
            b += [[a[o]]]
print(len(b))




