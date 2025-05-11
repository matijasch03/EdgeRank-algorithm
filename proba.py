from array import array

niz = array('i', [1, 2, 3])
niz.append(1)
#print(niz[3])

def quick(a, b):
    if a > b:
        return
    return a - b

print(quick(3, 3))