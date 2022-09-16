import random
def hoar(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        L = [elem for elem in arr if elem < q]
        M = [q] * arr.count(q)
        R = [elem for elem in arr if elem > q] 
        return hoar(L) + M + hoar(R)
    
# print(hoar([3,5,1,12,0,5,5,7,1]))