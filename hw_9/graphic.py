# строим по трем точкам)
import matplotlib.pyplot as plt
n = [1, 2, 3]
T = [0.9234180450439453, 0.8582849502563477, 0.7979207038879395]

f = []
for i in range(3):
    f.append(T[0]/T[i])

plt.plot(n, f, '--', color = '#C71585')
plt.grid()
plt.xlabel('n')
plt.ylabel('T[1]/T[n]')
plt.show()